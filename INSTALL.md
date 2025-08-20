# Installation Guide - Flood Village Detector QGIS Plugin

## Quick Installation Steps

### 1. Prepare Plugin Files
Ensure you have all required files in the plugin directory:
- `__init__.py`
- `flood_village_detector.py`
- `metadata.txt`
- `README.md`
- `INSTALL.md`
- `EXAMPLE_USAGE.md`

### 2. Install to QGIS

#### Option A: Direct Copy
1. Locate your QGIS plugins directory:
   - **Windows**: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`

2. Create a new folder named `village_plugin`
3. Copy all plugin files into this folder
4. Restart QGIS

#### Option B: ZIP Installation (RECOMMENDED)

**IMPORTANT**: The ZIP file structure is critical for QGIS to recognize the plugin.

##### Correct ZIP Structure:
```
village_plugin.zip
└── village_plugin/                    ← Root folder (must match plugin name)
    ├── __init__.py                    ← Plugin initialization
    ├── flood_village_detector.py     ← Main plugin code
    ├── metadata.txt                   ← Plugin metadata (REQUIRED)
    ├── README.md                      ← Documentation
    ├── INSTALL.md                     ← Installation guide
    └── EXAMPLE_USAGE.md              ← Usage examples
```

##### Step-by-Step ZIP Creation:

**Method 1 - Windows File Explorer:**
1. Create a new folder named `village_plugin`
2. Copy all plugin files (*.py, *.txt, *.md) into this folder
3. Right-click the `village_plugin` folder (not its contents)
4. Select "Send to" → "Compressed (zipped) folder"
5. Rename the ZIP file to `village_plugin.zip`

**Method 2 - Command Line:**
```bash
# From the directory containing village_plugin folder
zip -r village_plugin.zip village_plugin/
```

**Method 3 - 7-Zip or WinRAR:**
1. Right-click the `village_plugin` folder
2. Select "Add to archive..."
3. Set archive name to `village_plugin.zip`
4. Ensure compression format is ZIP

##### Install ZIP in QGIS:
1. Open QGIS
2. Go to `Plugins` → `Manage and Install Plugins`
3. Click "Install from ZIP" tab
4. Click the "..." button to browse
5. Select your `village_plugin.zip` file
6. Click "Install Plugin"
7. You should see "Plugin installed successfully" message

### 3. Enable the Plugin
1. In QGIS, go to `Plugins` → `Manage and Install Plugins`
2. Click on "Installed" tab
3. Find "Flood Village Detector Bisag"
4. Check the box to enable it

### 4. Access the Plugin
- Menu: `Plugins` → `Flood Village Detector`
- Or look for the toolbar icon (if toolbar is enabled)

## ZIP File Validation Checklist

Before creating the ZIP file, verify:
- ✅ All files are inside a folder named `village_plugin`
- ✅ The `metadata.txt` file is present
- ✅ The `__init__.py` file is present
- ✅ The folder structure matches the requirement above
- ✅ No extra nested folders or missing files

## Common ZIP Installation Errors

### Error: "The Zip file is not a valid QGIS python plugin"
**Cause**: Incorrect folder structure in ZIP file

**Solutions**:
1. **Missing root folder**: Ensure all files are inside a `village_plugin` folder
2. **Wrong folder name**: The root folder must be named exactly `village_plugin`
3. **Files in ZIP root**: Don't put plugin files directly in ZIP root

**Correct vs Incorrect Structure**:
```
❌ WRONG:
village_plugin.zip
├── __init__.py           ← Files directly in ZIP root
├── metadata.txt
└── flood_village_detector.py

✅ CORRECT:
village_plugin.zip
└── village_plugin/       ← Root folder required
    ├── __init__.py
    ├── metadata.txt
    └── flood_village_detector.py
```

### Error: "No root folder was found inside"
**Cause**: Files are directly in ZIP root without a containing folder

**Solution**: Create a `village_plugin` folder and put all files inside it before zipping

### Error: Plugin installs but doesn't appear in menu
**Causes & Solutions**:
1. **Missing metadata.txt**: Ensure this file is present and properly formatted
2. **Python errors**: Check QGIS Python console for error messages
3. **Plugin not enabled**: Go to Plugin Manager → Installed and enable it

## Verification

To verify successful installation:
1. The plugin should appear in `Plugins` menu as "Flood Village Detector"
2. No error messages in QGIS startup
3. Plugin dialog opens when clicked

## Troubleshooting Installation

### Plugin Not Appearing
- Check that the ZIP structure matches the requirements above
- Ensure the folder is named exactly `village_plugin`
- Restart QGIS completely
- Check QGIS Python console for error messages

### Import Errors
- Verify QGIS version is 3.16 or higher
- Check Python console: `Plugins` → `Python Console`
- Ensure all required QGIS libraries are available

### Permission Issues
- On Linux/macOS, ensure proper file permissions
- Run QGIS as administrator if necessary (Windows)
- Check that QGIS can write to the plugins directory

## Alternative Installation Methods

### GitHub Installation (if available):
1. Download ZIP from GitHub repository
2. Extract to get the plugin folder
3. Follow ZIP installation steps above

### Development Installation:
1. Clone repository to QGIS plugins directory
2. Restart QGIS
3. Enable plugin in Plugin Manager

## Uninstallation

To remove the plugin:
1. Go to `Plugins` → `Manage and Install Plugins`
2. Find "Flood Village Detector Bisag" in Installed tab
3. Click "Uninstall Plugin"
4. Restart QGIS

Or manually:
1. Disable it in Plugin Manager
2. Delete the `village_plugin` folder from plugins directory
3. Restart QGIS

## System Requirements

- QGIS 3.16 or higher
- Windows 10/macOS 10.14/Linux (recent distributions)
- Minimum 4GB RAM (8GB recommended for large datasets)
- 100MB free disk space for plugin and temporary files

## Support

If installation fails:
1. Check the ZIP structure carefully
2. Review error messages in QGIS Python console
3. Try manual folder installation instead of ZIP
4. Contact: [REDACTED]