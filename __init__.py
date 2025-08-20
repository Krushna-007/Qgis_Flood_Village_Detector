# -*- coding: utf-8 -*-
"""
Flood Village Detector QGIS Plugin
A plugin to detect villages flooded at given DEM threshold levels.
"""

def classFactory(iface):
    """Load FloodVillageDetector class from file flood_village_detector.
    
    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .flood_village_detector import FloodVillageDetector
    return FloodVillageDetector(iface)