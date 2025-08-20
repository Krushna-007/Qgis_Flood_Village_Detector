# 🌊 QGIS Flood Village Detector

[![QGIS Plugin](https://img.shields.io/badge/QGIS-Plugin-green.svg)](https://qgis.org)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0-orange.svg)](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/releases)

A powerful QGIS plugin for **flood risk assessment** and **village vulnerability analysis**. This tool helps identify villages and settlements at risk of flooding based on Digital Elevation Model (DEM) data and customizable water level thresholds.

![Plugin Demo](assets/plugin_demo.png)

## 🎯 Key Features

- 🗺️ **DEM Analysis**: Process Digital Elevation Model raster data
- 🏘️ **Multi-layer Support**: Analyze both point and polygon village layers
- 📊 **Shapefile Compatible**: Full support for shapefiles and other vector formats
- ⚙️ **Customizable Thresholds**: Set specific flood water levels in meters
- 📋 **CSV Export**: Export results with coordinates and feature IDs
- 🔄 **Background Processing**: Non-blocking analysis with real-time progress
- 🪟 **Windows Compatible**: Robust file handling for Windows systems
- 🚀 **Easy Installation**: One-click ZIP installation in QGIS

## 🚀 Quick Start

### Installation

1. **Download** the latest release from [Releases](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/releases)
2. **Open QGIS** (version 3.16 or higher)
3. Go to `Plugins` → `Manage and Install Plugins`
4. Click `Install from ZIP` and select the downloaded file
5. **Enable** the plugin in the Installed plugins list

### Basic Usage

1. **Load your data** in QGIS:
   - DEM raster layer (elevation data)
   - Village points/polygons (shapefiles, etc.)

2. **Open the plugin**: `Plugins` → `Flood Village Detector`

3. **Configure analysis**:
   - Select DEM layer
   - Choose village layers
   - Set flood water level threshold
   - Specify output CSV path

4. **Run analysis** and view results

## 📖 Detailed Documentation

### Prerequisites

- **QGIS Version**: 3.16 or higher
- **Data Requirements**:
  - DEM raster layer (any GDAL-supported format)
  - Village vector layers (shapefiles, GeoPackage, etc.)
- **System**: Windows 10+, macOS 10.14+, or Linux

### Supported Data Formats

| Type | Formats |
|------|---------|
| **Raster** | GeoTIFF, ASCII Grid, NetCDF, HDF, and all GDAL formats |
| **Vector** | Shapefile, GeoPackage, KML, GeoJSON, and all OGR formats |

### Analysis Workflow

1. **Flood Mask Generation**: Creates binary raster based on elevation threshold
2. **Point Analysis**: Samples flood mask at village point locations
3. **Polygon Analysis**: Evaluates flood risk using polygon centroids
4. **Results Export**: Generates CSV with flooded village information

### Output Format

The plugin exports a CSV file with the following structure:

```csv
Type,Name,Feature_ID,X_Coordinate,Y_Coordinate
Point,Point_1,1,72.5123,23.0456
Point,Point_3,3,72.5234,23.0567
Polygon,Polygon_1,1,72.5345,23.0678
```

## 🛠️ Advanced Usage

### Batch Processing

For processing multiple scenarios:

1. Load all required layers
2. Run analysis with different water levels
3. Compare results across scenarios
4. Use CSV outputs for further statistical analysis

### Integration with Other Tools

- **Excel/LibreOffice**: Open CSV results for statistical analysis
- **R/Python**: Import coordinates for advanced spatial analysis
- **Web Maps**: Use coordinates to create online flood risk maps

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/Krushna-007/Qgis_Flood_Village_Detector.git
cd Qgis_Flood_Village_Detector

# Install to QGIS plugins directory
# Windows: %APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\
# macOS: ~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/
# Linux: ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```

### Reporting Issues

Found a bug? Have a feature request? Please [open an issue](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/issues) with:

- QGIS version
- Operating system
- Error messages (if any)
- Steps to reproduce

## 📊 Use Cases

### Disaster Risk Assessment
- **Emergency Planning**: Identify vulnerable settlements
- **Evacuation Routes**: Plan safe evacuation paths
- **Resource Allocation**: Prioritize areas for flood defenses

### Research Applications
- **Climate Studies**: Analyze flood risk under different scenarios
- **Urban Planning**: Assess development suitability
- **Insurance**: Risk assessment for property insurance

### Government & NGOs
- **Policy Making**: Evidence-based flood management policies
- **Community Outreach**: Risk communication to residents
- **Funding Allocation**: Prioritize flood mitigation investments

## 🏆 Acknowledgments

- **QGIS Community**: For the excellent QGIS platform
- **PyQGIS**: For the powerful Python API
- **Contributors**: Everyone who helped improve this plugin

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Krushna Parmar**
- GitHub: [@Krushna-007](https://github.com/Krushna-007)
- Email: [REDACTED]

## 🌟 Support the Project

If this plugin helps your work, please:
- ⭐ **Star** this repository
- 🐛 **Report** any issues you find
- 💡 **Suggest** new features
- 🤝 **Contribute** code improvements

---

<div align="center">

**Made with ❤️ for the QGIS community**

[📥 Download](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/releases) | [📖 Documentation](README.md) | [🐛 Issues](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/issues) | [💬 Discussions](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/discussions)

</div>