# -*- coding: utf-8 -*-
"""
Flood Village Detector QGIS Plugin
Main plugin implementation with UI dialog and analysis logic.
"""

import os
import csv
import tempfile
import uuid
import time
from typing import List, Tuple, Optional

from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt, QThread, pyqtSignal
from qgis.PyQt.QtGui import QIcon, QPixmap
from qgis.PyQt.QtWidgets import (QAction, QDialog, QVBoxLayout, QHBoxLayout, 
                                QLabel, QComboBox, QSpinBox, QDoubleSpinBox,
                                QLineEdit, QPushButton, QTextEdit, QMessageBox, 
                                QProgressBar, QGroupBox, QFileDialog, QCheckBox,
                                QGridLayout, QFrame)

from qgis.core import (QgsProject, QgsRasterLayer, QgsVectorLayer, QgsGeometry,
                      QgsPointXY, QgsMessageLog, Qgis, QgsApplication, QgsTask, QgsTaskManager,
                      QgsFeature, QgsField, QgsFields, QgsWkbTypes)

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.gui import QgsMapLayerComboBox


class FloodAnalysisTask(QgsTask):
    """Background task for flood analysis to prevent UI freezing."""
    
    def __init__(self, dem_layer, points_layer, polygons_layer, water_level, output_path):
        super().__init__('Flood Village Analysis', QgsTask.CanCancel)
        self.dem_layer = dem_layer
        self.points_layer = points_layer
        self.polygons_layer = polygons_layer
        self.water_level = water_level
        self.output_path = output_path
        self.flooded_points = []
        self.flooded_polygons = []
        self.error_message = None
        
    def run(self):
        """Execute the flood analysis task."""
        try:
            # Check if we have any layers to analyze
            if not self.points_layer and not self.polygons_layer:
                self.error_message = "No village layers provided for analysis"
                return False
            
            # Check if DEM layer is valid
            if not self.dem_layer or not self.dem_layer.isValid():
                self.error_message = "Invalid DEM layer"
                return False
            
            # Create temporary flood mask with unique filename
            temp_dir = tempfile.gettempdir()
            unique_id = str(uuid.uuid4())[:8]
            timestamp = str(int(time.time()))
            mask_filename = f'flood_mask_{timestamp}_{unique_id}.tif'
            mask_path = os.path.join(temp_dir, mask_filename)
            
            # Ensure the temporary file doesn't already exist
            if os.path.exists(mask_path):
                self._cleanup_temp_file(mask_path)
            
            # Create raster calculator entries
            entries = []
            entry = QgsRasterCalculatorEntry()
            entry.ref = f'{self.dem_layer.name()}@1'
            entry.raster = self.dem_layer
            entry.bandNumber = 1
            entries.append(entry)
            
            # Expression: areas below water level = 1, above = 0
            expression = f'("{self.dem_layer.name()}@1" <= {self.water_level}) * 1'
            
            # Calculate flood mask
            calc = QgsRasterCalculator(
                expression,
                mask_path,
                'GTiff',
                self.dem_layer.extent(),
                self.dem_layer.width(),
                self.dem_layer.height(),
                entries
            )
            
            result = calc.processCalculation()
            if result != 0:
                self.error_message = f"Failed to create flood mask. Calculator result: {result}"
                return False
                
            # Load the flood mask
            mask_layer = QgsRasterLayer(mask_path, 'flood_mask')
            if not mask_layer.isValid():
                self.error_message = "Invalid flood mask layer"
                return False
            
            # Analyze points
            if self.points_layer:
                self._analyze_points(mask_layer)
                
            # Analyze polygons
            if self.polygons_layer:
                self._analyze_polygons(mask_layer)
            
            # Export results to CSV
            self._export_to_csv()
            
            # Clean up temporary file with retry mechanism
            self._cleanup_temp_file(mask_path)
                
            return True
            
        except Exception as e:
            # Try to clean up temporary file even if analysis failed
            if 'mask_path' in locals() and os.path.exists(mask_path):
                self._cleanup_temp_file(mask_path)
            self.error_message = str(e)
            return False
    
    def _cleanup_temp_file(self, file_path):
        """Clean up temporary file with retry mechanism for Windows file locking issues."""
        if not os.path.exists(file_path):
            return
        
        max_attempts = 5
        for attempt in range(max_attempts):
            try:
                os.remove(file_path)
                return  # Success
            except (OSError, PermissionError, WindowsError) as e:
                if attempt < max_attempts - 1:
                    # Wait a bit and try again
                    time.sleep(0.5)
                    continue
                else:
                    # Last attempt failed, but don't fail the entire analysis
                    # Log the warning but continue
                    print(f"Warning: Could not delete temporary file {file_path}: {e}")
                    return
    
    def _analyze_points(self, mask_layer):
        """Analyze point features for flooding."""
        for feature in self.points_layer.getFeatures():
            if self.isCanceled():
                return
                
            geom = feature.geometry()
            if geom.type() == QgsWkbTypes.PointGeometry:
                point = geom.asPoint()
                
                # Sample the flood mask at this point
                sample_result = mask_layer.dataProvider().sample(point, 1)
                if sample_result and len(sample_result) > 0:
                    flood_value = sample_result[0]
                    
                    # If flood value > 0.5, consider it flooded
                    if flood_value and flood_value > 0.5:
                        name = f"Point_{feature.id()}"
                        self.flooded_points.append({
                            'name': name,
                            'id': feature.id(),
                            'x': point.x(),
                            'y': point.y()
                        })
    
    def _analyze_polygons(self, mask_layer):
        """Analyze polygon features for flooding (using centroids)."""
        for feature in self.polygons_layer.getFeatures():
            if self.isCanceled():
                return
                
            geom = feature.geometry()
            if geom.type() == QgsWkbTypes.PolygonGeometry:
                centroid = geom.centroid().asPoint()
                
                # Sample the flood mask at centroid
                sample_result = mask_layer.dataProvider().sample(centroid, 1)
                if sample_result and len(sample_result) > 0:
                    flood_value = sample_result[0]
                    
                    # If flood value > 0.5, consider it flooded
                    if flood_value and flood_value > 0.5:
                        name = f"Polygon_{feature.id()}"
                        self.flooded_polygons.append({
                            'name': name,
                            'id': feature.id(),
                            'centroid_x': centroid.x(),
                            'centroid_y': centroid.y()
                        })
    

    
    def _export_to_csv(self):
        """Export results to CSV file."""
        with open(self.output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write headers
            headers = ['Type', 'Name', 'Feature_ID', 'X_Coordinate', 'Y_Coordinate']
            writer.writerow(headers)
            
            # Write flooded points
            for point in self.flooded_points:
                writer.writerow([
                    'Point',
                    point['name'],
                    point['id'],
                    point['x'],
                    point['y']
                ])
            
            # Write flooded polygons
            for polygon in self.flooded_polygons:
                writer.writerow([
                    'Polygon',
                    polygon['name'],
                    polygon['id'],
                    polygon['centroid_x'],
                    polygon['centroid_y']
                ])


class FloodVillageDetectorDialog(QDialog):
    """Main dialog for the Flood Village Detector plugin."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Flood Village Detector")
        self.setMinimumSize(500, 600)
        self.current_task = None
        self.setupUi()
        self.populate_layers()
        
    def setupUi(self):
        """Set up the user interface."""
        layout = QVBoxLayout()
        
        # Title
        title_label = QLabel("Flood Village Detector")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(title_label)
        
        # Input layers group
        input_group = QGroupBox("Input Layers")
        input_layout = QGridLayout()
        
        # DEM layer selection
        input_layout.addWidget(QLabel("DEM Raster Layer:"), 0, 0)
        self.dem_combo = QgsMapLayerComboBox()
        # Set to show only raster layers
        self.dem_combo.setFilters(1)  # 1 = Raster layers
        input_layout.addWidget(self.dem_combo, 0, 1)
        
        # Points layer selection
        input_layout.addWidget(QLabel("Village Points Layer:"), 1, 0)
        self.points_combo = QComboBox()
        input_layout.addWidget(self.points_combo, 1, 1)
        
        # Polygons layer selection
        input_layout.addWidget(QLabel("Village Polygons Layer:"), 2, 0)
        self.polygons_combo = QComboBox()
        input_layout.addWidget(self.polygons_combo, 2, 1)
        
        # Add refresh button to reload layers
        refresh_layout = QHBoxLayout()
        self.refresh_button = QPushButton("Refresh Layers")
        self.refresh_button.clicked.connect(self.populate_layers)
        refresh_layout.addWidget(self.refresh_button)
        refresh_layout.addStretch()
        input_layout.addLayout(refresh_layout, 3, 0, 1, 2)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Parameters group
        params_group = QGroupBox("Analysis Parameters")
        params_layout = QGridLayout()
        
        # Water level input
        params_layout.addWidget(QLabel("Flood Water Level (m):"), 0, 0)
        self.water_level_spin = QDoubleSpinBox()
        self.water_level_spin.setRange(0.0, 1000.0)
        self.water_level_spin.setValue(50.0)
        self.water_level_spin.setDecimals(2)
        self.water_level_spin.setSuffix(" m")
        params_layout.addWidget(self.water_level_spin, 0, 1)
        
        params_group.setLayout(params_layout)
        layout.addWidget(params_group)
        
        # Output group
        output_group = QGroupBox("Output Settings")
        output_layout = QGridLayout()
        
        # Output file path
        output_layout.addWidget(QLabel("Output CSV File:"), 0, 0)
        output_file_layout = QHBoxLayout()
        self.output_path_edit = QLineEdit()
        self.output_path_edit.setText("flooded_villages.csv")
        output_file_layout.addWidget(self.output_path_edit)
        
        self.browse_button = QPushButton("Browse...")
        self.browse_button.clicked.connect(self.browse_output_file)
        output_file_layout.addWidget(self.browse_button)
        
        output_layout.addLayout(output_file_layout, 0, 1)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Control buttons
        button_layout = QHBoxLayout()
        self.run_button = QPushButton("Run Analysis")
        self.run_button.clicked.connect(self.run_analysis)
        self.run_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; padding: 8px; }")
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_analysis)
        self.cancel_button.setEnabled(False)
        
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)
        
        # Status log
        layout.addWidget(QLabel("Analysis Log:"))
        self.status_log = QTextEdit()
        self.status_log.setMaximumHeight(150)
        self.status_log.setReadOnly(True)
        layout.addWidget(self.status_log)
        
        self.setLayout(layout)
        
        # Populate layers after UI is set up
        self.populate_layers()
    
    def populate_layers(self):
        """Populate layer combo boxes with available layers."""
        # Clear existing items
        self.points_combo.clear()
        self.polygons_combo.clear()
        
        # Add a default "Select layer" option
        self.points_combo.addItem("-- Select village points layer --")
        self.polygons_combo.addItem("-- Select village polygons layer --")
        
        # Get all layers from the project
        project = QgsProject.instance()
        layers = project.mapLayers()
        
        vector_layers_found = 0
        
        # Add vector layers to both combo boxes
        for layer_id, layer in layers.items():
            if isinstance(layer, QgsVectorLayer) and layer.isValid():
                layer_name = layer.name()
                layer_source = layer.source()
                
                # Add extra info about the layer type
                geom_type = layer.geometryType()
                if geom_type == 0:  # Point
                    display_name = f"{layer_name} (Points)"
                elif geom_type == 1:  # Line
                    display_name = f"{layer_name} (Lines)"
                elif geom_type == 2:  # Polygon
                    display_name = f"{layer_name} (Polygons)"
                else:
                    display_name = f"{layer_name} (Vector)"
                
                # Add to both combo boxes
                self.points_combo.addItem(display_name, layer_id)
                self.polygons_combo.addItem(display_name, layer_id)
                vector_layers_found += 1
        
        # Log the result
        if vector_layers_found == 0:
            self.log_message("⚠️ No vector layers found in project. Please load shapefiles or other vector layers.")
        else:
            self.log_message(f"📋 Found {vector_layers_found} vector layers in project.")
    
    def browse_output_file(self):
        """Browse for output CSV file location."""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Analysis Results",
            self.output_path_edit.text(),
            "CSV Files (*.csv);;All Files (*)"
        )
        if file_path:
            self.output_path_edit.setText(file_path)
    
    def log_message(self, message, level=Qgis.Info):
        """Add message to status log."""
        self.status_log.append(message)
        QgsMessageLog.logMessage(message, 'Flood Village Detector', level)
    
    def run_analysis(self):
        """Run the flood analysis."""
        # Validate inputs
        dem_layer = self.dem_combo.currentLayer()
        
        # Get selected layers by ID from combo boxes
        points_layer_id = self.points_combo.currentData()
        polygons_layer_id = self.polygons_combo.currentData()
        
        # Only get layers if a valid selection was made (not the default option)
        points_layer = None
        polygons_layer = None
        
        if points_layer_id and self.points_combo.currentIndex() > 0:
            points_layer = QgsProject.instance().mapLayer(points_layer_id)
            
        if polygons_layer_id and self.polygons_combo.currentIndex() > 0:
            polygons_layer = QgsProject.instance().mapLayer(polygons_layer_id)
        
        if not dem_layer:
            QMessageBox.warning(self, "Warning", "Please select a DEM raster layer.")
            return
        
        if not points_layer and not polygons_layer:
            QMessageBox.warning(self, "Warning", "Please select at least one village layer (points or polygons).")
            return
        
        output_path = self.output_path_edit.text().strip()
        if not output_path:
            QMessageBox.warning(self, "Warning", "Please specify an output CSV file path.")
            return
        
        # Clear previous log
        self.status_log.clear()
        self.log_message("Starting flood analysis...")
        
        # Debug logging
        self.log_message(f"DEM Layer: {dem_layer.name() if dem_layer else 'None'}")
        self.log_message(f"Points Layer: {points_layer.name() if points_layer else 'None'}")
        self.log_message(f"Polygons Layer: {polygons_layer.name() if polygons_layer else 'None'}")
        self.log_message(f"Water Level: {self.water_level_spin.value()} meters")
        self.log_message(f"Output Path: {output_path}")
        
        # Create and run the analysis task
        self.current_task = FloodAnalysisTask(
            dem_layer,
            points_layer,
            polygons_layer,
            self.water_level_spin.value(),
            output_path
        )
        
        # Connect task signals
        self.current_task.progressChanged.connect(self.progress_bar.setValue)
        self.current_task.taskCompleted.connect(self.on_analysis_completed)
        self.current_task.taskTerminated.connect(self.on_analysis_terminated)
        
        # Update UI
        self.run_button.setEnabled(False)
        self.cancel_button.setEnabled(True)
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # Indeterminate progress
        
        # Add task to task manager
        self.log_message("📋 Adding task to task manager...")
        QgsApplication.taskManager().addTask(self.current_task)
        self.log_message("📋 Task added successfully")
    
    def cancel_analysis(self):
        """Cancel the running analysis."""
        if self.current_task:
            self.current_task.cancel()
    
    def on_analysis_completed(self):
        """Handle analysis completion."""
        self.log_message("📋 Task completed signal received")
        if self.current_task and self.current_task.error_message:
            self.log_message(f"❌ Analysis failed: {self.current_task.error_message}", Qgis.Critical)
            QMessageBox.critical(self, "Analysis Failed", self.current_task.error_message)
        elif self.current_task:
            self.log_message("✅ Analysis completed successfully!")
            self.log_message(f"📄 Results exported to: {self.output_path_edit.text()}")
            self.log_message(f"🏘️ Flooded village points found: {len(self.current_task.flooded_points)}")
            self.log_message(f"🏗️ Flooded village polygons found: {len(self.current_task.flooded_polygons)}")
            
            QMessageBox.information(
                self, 
                "Analysis Complete",
                f"Analysis completed successfully!\n\n"
                f"Flooded village points: {len(self.current_task.flooded_points)}\n"
                f"Flooded village polygons: {len(self.current_task.flooded_polygons)}\n\n"
                f"Results saved to: {self.output_path_edit.text()}"
            )
        else:
            self.log_message("⚠️ Task completed but current_task is None")
        
        self._reset_ui()
    
    def on_analysis_terminated(self):
        """Handle analysis termination (cancellation)."""
        self.log_message("📋 Task terminated signal received")
        if self.current_task and hasattr(self.current_task, 'error_message') and self.current_task.error_message:
            self.log_message(f"⚠️ Analysis was cancelled due to error: {self.current_task.error_message}")
        else:
            self.log_message("⚠️ Analysis was cancelled.")
        self._reset_ui()
    
    def _reset_ui(self):
        """Reset UI to initial state after analysis."""
        self.run_button.setEnabled(True)
        self.cancel_button.setEnabled(False)
        self.progress_bar.setVisible(False)
        self.current_task = None


class FloodVillageDetector:
    """Main plugin class."""
    
    def __init__(self, iface):
        """Constructor."""
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        
        # Initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'FloodVillageDetector_{}.qm'.format(locale)
        )
        
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)
        
        # Declare instance attributes
        self.actions = []
        self.menu = self.tr('&Flood Village Detector')
        self.dialog = None
    
    def tr(self, message):
        """Get the translation for a string using Qt translation API."""
        return QCoreApplication.translate('FloodVillageDetector', message)
    
    def add_action(self, icon_path, text, callback, enabled_flag=True, add_to_menu=True,
                   add_to_toolbar=True, status_tip=None, whats_this=None, parent=None):
        """Add a toolbar icon to the toolbar."""
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)
        
        if status_tip is not None:
            action.setStatusTip(status_tip)
        
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        
        if add_to_toolbar:
            self.iface.addToolBarIcon(action)
        
        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)
        
        self.actions.append(action)
        return action
    
    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        # Use default QGIS icon instead of custom icon
        self.add_action(
            '',
            text=self.tr('Flood Village Detector'),
            callback=self.run,
            parent=self.iface.mainWindow()
        )
    
    def unload(self):
        """Remove the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(self.tr('&Flood Village Detector'), action)
            self.iface.removeToolBarIcon(action)
    
    def run(self):
        """Run method that performs all the real work."""
        if self.dialog is None:
            self.dialog = FloodVillageDetectorDialog()
        
        # Show the dialog
        self.dialog.show()
        result = self.dialog.exec_()
