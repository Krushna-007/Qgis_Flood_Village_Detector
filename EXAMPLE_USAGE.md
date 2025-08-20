# Example Usage - Flood Village Detector Plugin

## Sample Workflow

This guide demonstrates how to use the Flood Village Detector plugin with sample data.

### Prerequisites

Before starting, ensure you have:
1. QGIS 3.16+ installed
2. The Flood Village Detector plugin installed and enabled
3. Sample data loaded (DEM raster and village vector layers)

### Sample Data Requirements

For testing the plugin, you'll need:

#### 1. DEM Raster Layer
- **Format**: GeoTIFF, ASCII Grid, or any GDAL-supported raster format
- **Content**: Elevation values in meters
- **Coordinate System**: Any projected or geographic CRS
- **Example**: SRTM DEM, ASTER GDEM, or local topographic data

#### 2. Village Points Layer (Optional)
- **Format**: Shapefile, GeoPackage, or any OGR-supported vector format
- **Geometry**: Point features
- **Recommended Attributes**:
  - `name` or `village_name`: Village names
  - `population`: Population data (optional)
  - `id`: Unique identifier

#### 3. Village Polygons Layer (Optional)
- **Format**: Shapefile, GeoPackage, or any OGR-supported vector format
- **Geometry**: Polygon features
- **Recommended Attributes**:
  - `name` or `area_name`: Area names
  - `area_km2`: Area in square kilometers (optional)
  - `id`: Unique identifier

### Step-by-Step Example

#### Step 1: Load Data in QGIS
```
1. Open QGIS
2. Add your DEM raster: Layer → Add Layer → Add Raster Layer
3. Add village points: Layer → Add Layer → Add Vector Layer
4. Add village polygons: Layer → Add Layer → Add Vector Layer
```

#### Step 2: Open the Plugin
```
1. Go to Plugins → Flood Village Detector
2. The plugin dialog will open
```

#### Step 3: Configure Input Layers
```
1. DEM Raster Layer: Select your elevation model
2. Village Points Layer: Select your points layer
3. Village Polygons Layer: Select your polygons layer
4. Points Name Field: Choose "name" or "village_name"
5. Polygons Name Field: Choose "name" or "area_name"
```

#### Step 4: Set Analysis Parameters
```
1. Flood Water Level: Enter a realistic value (e.g., 50 meters)
   - Consider your DEM's elevation range
   - Start with a moderate value for testing
```

#### Step 5: Configure Output
```
1. Output CSV File: Choose a location like "C:\temp\flood_results.csv"
2. Or use the Browse button to select a location
```

#### Step 6: Run Analysis
```
1. Click "Run Analysis"
2. Monitor progress in the log area
3. Wait for completion message
```

### Expected Results

#### Console Output Example:
```
Starting flood analysis...
✅ Analysis completed successfully!
📄 Results exported to: C:\temp\flood_results.csv
🏘️ Flooded village points found: 12
🏗️ Flooded village polygons found: 8
```

#### CSV Output Example:
```csv
Type,Name,Feature_ID,X_Coordinate,Y_Coordinate
Point,Riverside Village,1,77.2345,28.1234
Point,Lowland Settlement,3,77.2456,28.1345
Point,Valley Town,7,77.2567,28.1456
Polygon,Flood Plain District,2,77.2678,28.1567
Polygon,Riverside Area,5,77.2789,28.1678
```

### Interpreting Results

#### Understanding the Output:
- **Type**: Indicates whether the feature is a point or polygon
- **Name**: Village/area name from your selected field
- **Feature_ID**: Unique identifier from the source layer
- **X_Coordinate**: Longitude (for points) or centroid X (for polygons)
- **Y_Coordinate**: Latitude (for points) or centroid Y (for polygons)

#### Analysis Insights:
1. **Count of flooded areas**: Total number of vulnerable locations
2. **Spatial distribution**: Geographic pattern of flood risk
3. **Coordinate data**: Precise locations for emergency planning

### Common Test Scenarios

#### Scenario 1: Coastal Flood Risk
```
- DEM: Coastal elevation model
- Water Level: 2-5 meters (sea level rise)
- Villages: Coastal settlements
- Expected: Low-lying coastal areas identified
```

#### Scenario 2: River Flood Analysis
```
- DEM: River basin elevation model
- Water Level: 10-50 meters (flood stage)
- Villages: Riverside communities
- Expected: Floodplain settlements identified
```

#### Scenario 3: Urban Flood Risk
```
- DEM: Urban area elevation model
- Water Level: 1-3 meters (storm surge)
- Villages: Urban districts/neighborhoods
- Expected: Low-lying urban areas identified
```

### Validation Tips

#### Check Your Results:
1. **Visual Inspection**: Load results back into QGIS and overlay on DEM
2. **Elevation Verification**: Check that identified areas are indeed below threshold
3. **Logical Assessment**: Ensure results make geographic sense

#### Quality Control:
1. **DEM Quality**: Ensure your DEM has reasonable elevation values
2. **Coordinate Systems**: Verify all layers use compatible CRS
3. **Data Completeness**: Check for missing or invalid geometries

### Advanced Usage

#### Batch Processing:
- Run analysis with different water levels
- Compare results across multiple scenarios
- Export multiple CSV files for comparative analysis

#### Integration with Other Tools:
- Import CSV results into GIS for further analysis
- Use coordinate data for emergency response planning
- Combine with population data for impact assessment

### Troubleshooting Common Issues

#### No Results Found:
- Check if water level is too low/high for your area
- Verify DEM elevation range matches your threshold
- Ensure village layers have valid geometries

#### Unexpected Results:
- Review DEM data quality and units
- Check coordinate reference systems
- Validate village layer attribute fields

#### Performance Issues:
- Use smaller DEM extents for testing
- Reduce DEM resolution if processing is slow
- Ensure adequate system memory
