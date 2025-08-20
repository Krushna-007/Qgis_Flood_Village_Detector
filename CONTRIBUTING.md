# Contributing to QGIS Flood Village Detector

Thank you for your interest in contributing to the QGIS Flood Village Detector plugin! 🎉

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check the [existing issues](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/issues) to avoid duplicates.

When filing a bug report, please include:

- **QGIS Version**: Your QGIS version (e.g., 3.40.7)
- **Operating System**: Windows/macOS/Linux version
- **Plugin Version**: Version of the plugin you're using
- **Error Messages**: Full error messages and stack traces
- **Steps to Reproduce**: Clear steps to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Screenshots**: If applicable, add screenshots

### Suggesting Features

Feature requests are welcome! Please:

1. Check if the feature already exists or is planned
2. Open a [feature request](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/issues/new)
3. Describe the feature and its use case
4. Explain why it would benefit users

### Code Contributions

#### Development Setup

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/Qgis_Flood_Village_Detector.git
   cd Qgis_Flood_Village_Detector
   ```

3. **Create a development branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Install to QGIS**:
   - Copy plugin files to QGIS plugins directory
   - Restart QGIS and enable the plugin

#### Code Standards

- **Python Style**: Follow PEP 8 guidelines
- **Comments**: Use clear, descriptive comments
- **Docstrings**: Document all functions and classes
- **Error Handling**: Include appropriate try-catch blocks
- **Logging**: Use QGIS logging for debug information

#### Testing

- Test your changes with different QGIS versions (3.16+)
- Test on different operating systems if possible
- Verify compatibility with various data formats
- Check error handling with invalid inputs

#### Pull Request Process

1. **Update documentation** if needed
2. **Test thoroughly** on your local setup
3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add feature: your description"
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** with:
   - Clear title and description
   - Link to any related issues
   - Screenshots/examples if applicable

## 📝 Code Style Guidelines

### Python Code

```python
# Good: Clear function documentation
def analyze_flood_risk(dem_layer, water_level):
    """
    Analyze flood risk based on DEM and water level.
    
    Args:
        dem_layer (QgsRasterLayer): Digital elevation model
        water_level (float): Flood water level in meters
        
    Returns:
        bool: True if analysis successful, False otherwise
    """
    pass

# Good: Error handling
try:
    result = process_data()
except Exception as e:
    self.log_message(f"Error processing data: {e}")
    return False
```

### UI Components

- Use clear, descriptive labels
- Provide helpful tooltips
- Include progress indicators for long operations
- Ensure accessibility (screen readers, keyboard navigation)

## 🐛 Issue Labels

We use these labels to categorize issues:

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `question`: Further information requested

## 🎯 Areas for Contribution

### High Priority
- Performance optimizations
- Additional output formats (GeoJSON, KML)
- Batch processing capabilities
- Better error messages

### Medium Priority
- UI/UX improvements
- Additional analysis algorithms
- Integration with other QGIS plugins
- Multi-language support

### Documentation
- Video tutorials
- Usage examples
- API documentation
- Translation improvements

## 📞 Getting Help

- **Issues**: [GitHub Issues](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Krushna-007/Qgis_Flood_Village_Detector/discussions)
- **Email**: [REDACTED]

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal attacks
- Publishing private information

## 🏆 Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Given contributor badges

Thank you for helping make this plugin better for everyone! 🙏
