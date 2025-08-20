# QGIS Compatibility Notes - Flood Village Detector Plugin

## Version Compatibility

### Supported QGIS Versions
- **Minimum**: QGIS 3.16
- **Maximum**: QGIS 3.99
- **Tested**: QGIS 3.40.7-Bratislava

## Import Changes for QGIS 3.40+

### Fixed Import Issues

The plugin has been updated to resolve multiple import and API errors in QGIS 3.40.7. The following changes were made:

#### Issue 1: Raster Calculator Import
**Before (Causing Errors):**
```python
from qgis.core import QgsRasterCalculator, QgsRasterCalculatorEntry
```

**After (Fixed):**
```python
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
```

#### Issue 2: Layer Combo Box Filters
**Before (Causing Errors):**
```python
self.dem_combo.setFilters(QgsMapLayerComboBox.RasterLayer)
self.points_combo.setFilters(QgsMapLayerComboBox.VectorLayer)
```

**After (Fixed):**
```python
self.dem_combo.setFilters(1)  # 1 = Raster layers
self.points_combo.setFilters(2)  # 2 = Vector layers
```

### Background
In newer QGIS versions (3.40+), multiple API changes were implemented:
1. Raster calculation classes were moved from `qgis.core` to `qgis.analysis` module
2. The filter constants for `QgsMapLayerComboBox` were changed or removed, requiring the use of integer values

## Error Resolution

### Previous Errors:

**Error 1 - Import Error:**
```
ImportError: cannot import name 'QgsRasterCalculator' from 'qgis.core'
```

**Error 2 - Attribute Error:**
```
AttributeError: type object 'QgsMapLayerComboBox' has no attribute 'RasterLayer'
```

### Solutions Applied:
1. **Fixed imports**: Moved `QgsRasterCalculator` and `QgsRasterCalculatorEntry` from `qgis.core` to `qgis.analysis`
2. **Fixed filter constants**: Replaced enum constants with integer values for layer filtering
3. **Updated ZIP file**: Created new version with all compatibility fixes

## Installation Notes

### For QGIS 3.40.7+ Users:
- Use the updated `village_plugin.zip` file
- The plugin should now load without import errors
- All functionality remains the same

### For Older QGIS Versions (3.16-3.39):
- The current version should still work
- If you encounter issues, please report them

## Testing Checklist

After installation, verify:
- [ ] Plugin appears in Plugins menu without errors
- [ ] Dialog opens successfully 
- [ ] Layer combo boxes populate correctly
- [ ] Analysis runs without Python errors

## Troubleshooting

### If Import Errors Persist:
1. Check QGIS version: `Help` → `About`
2. Ensure you're using the latest plugin ZIP file
3. Check Python console for specific error messages
4. Try manual installation instead of ZIP

### Common Issues:
- **Old ZIP file**: Ensure you're using the updated version
- **Cache issues**: Restart QGIS completely
- **Python path**: Check if QGIS Python environment is properly set up

## Development Notes

### Module Locations by QGIS Version:

| QGIS Version | QgsRasterCalculator Location |
|--------------|------------------------------|
| 3.16-3.39    | qgis.core (legacy)          |
| 3.40+        | qgis.analysis (current)     |

### Future Compatibility:
The plugin uses the modern import structure and should be compatible with future QGIS versions that maintain the current API organization.

## Support

For compatibility issues:
- Email: [REDACTED]
- Include QGIS version and error messages
- Attach Python console output if available
