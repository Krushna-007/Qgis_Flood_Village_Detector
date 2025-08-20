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

# ...existing code from flood_village_detector.py...
