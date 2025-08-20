# Installation Guide

## 🚀 Quick Installation (Recommended)

### Method 1: Download from Releases

1. **Download** the latest `flood_village_detector.zip` from [Releases](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/releases)
2. **Open QGIS** (version 3.16 or higher)
3. Go to `Plugins` → `Manage and Install Plugins`
4. Click **"Install from ZIP"** tab
5. Click the **"..."** button and select the downloaded ZIP file
6. Click **"Install Plugin"**
7. **Enable** the plugin in the "Installed" tab

### Method 2: Manual Installation

1. **Download** or clone this repository
2. **Copy** the plugin folder to your QGIS plugins directory:
   - **Windows**: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
3. **Restart** QGIS
4. **Enable** the plugin in `Plugins` → `Manage and Install Plugins`

## 📋 System Requirements

### Minimum Requirements
- **QGIS**: 3.16 or higher
- **Python**: 3.7+ (included with QGIS)
- **RAM**: 4GB minimum (8GB recommended for large datasets)
- **Storage**: 100MB free space

### Supported Operating Systems
- **Windows**: 10, 11
- **macOS**: 10.14 (Mojave) or higher
- **Linux**: Ubuntu 18.04+, CentOS 7+, or equivalent

### Supported QGIS Versions
- ✅ QGIS 3.16 LTR
- ✅ QGIS 3.22 LTR
- ✅ QGIS 3.28 LTR
- ✅ QGIS 3.34 LTR
- ✅ QGIS 3.40+

## 🔧 Troubleshooting Installation

### Common Issues

#### "The ZIP file is not a valid QGIS python plugin"

**Cause**: Incorrect ZIP file structure

**Solution**:
1. Ensure the ZIP contains a root folder named `flood_village_detector`
2. All plugin files should be inside this root folder
3. Download from the official [Releases](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/releases) page

#### Plugin doesn't appear in menu

**Possible causes and solutions**:

1. **Not enabled**: 
   - Go to `Plugins` → `Manage and Install Plugins` → `Installed`
   - Find "Flood Village Detector" and check the box

2. **Python errors**:
   - Open `Plugins` → `Python Console`
   - Look for error messages
   - Ensure QGIS version is 3.16+

3. **Permission issues**:
   - **Windows**: Run QGIS as administrator
   - **macOS/Linux**: Check file permissions in plugins directory

#### Import errors during startup

**Cause**: Missing dependencies or wrong QGIS version

**Solution**:
1. Check QGIS version: `Help` → `About`
2. Ensure QGIS is 3.16 or higher
3. Try reinstalling QGIS if issues persist

## 🗂️ Plugin Directory Structure

After successful installation, you should see:

```
flood_village_detector/
├── __init__.py              # Plugin initialization
├── flood_village_detector.py   # Main plugin code
├── metadata.txt             # Plugin metadata
├── README.md               # Documentation
├── INSTALLATION.md         # This file
└── CHANGELOG.md           # Version history
```

## 🔄 Updating the Plugin

### Automatic Updates
- QGIS doesn't automatically update plugins installed from ZIP
- Check [Releases](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/releases) for new versions

### Manual Update Process
1. **Download** the latest version
2. **Disable** the old plugin in QGIS
3. **Remove** old plugin files from plugins directory
4. **Install** new version following installation steps above
5. **Restart** QGIS

## 🧪 Development Installation

For developers who want to contribute:

### 1. Clone Repository
```bash
git clone https://github.com/Krushna-007/Qgis_Flood_Village_Detector.git
cd Qgis_Flood_Village_Detector
```

### 2. Create Symbolic Link (Recommended)

**Windows (Admin PowerShell)**:
```powershell
New-Item -ItemType SymbolicLink -Path "%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\flood_village_detector" -Target "C:\path\to\cloned\repo"
```

**macOS/Linux**:
```bash
ln -s /path/to/cloned/repo ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/flood_village_detector
```

### 3. Development Tools
- **Code Editor**: VSCode, PyCharm, or similar
- **QGIS Plugin Builder**: For generating plugin templates
- **Git**: For version control

## 📞 Getting Help

If you encounter installation issues:

1. **Check** the [README.md](README.md) for common solutions
2. **Search** [existing issues](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/issues)
3. **Create** a [new issue](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/issues/new) with:
   - QGIS version
   - Operating system
   - Error messages
   - Installation method used

4. **Contact**: [REDACTED]

## ✅ Verification

After installation, verify the plugin works:

1. **Open** QGIS
2. **Check** that "Flood Village Detector" appears in the `Plugins` menu
3. **Click** the menu item to open the plugin dialog
4. **Load** some test data and try a simple analysis

If everything works correctly, you're ready to use the plugin! 🎉
