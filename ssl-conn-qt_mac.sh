#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd -P)

# For Boundless installations (NOTE: no current Mac install with PKI, yet)
BQGIS=/Applications/QGIS.app/Contents
QGIS_PREFIX_PATH=${BQGIS}/MacOS
export QGIS_PREFIX_PATH
export PATH=${QGIS_PREFIX_PATH}/bin:$PATH
export DYLD_LIBRARY_PATH=${BQGIS}/MacOS/lib:${BQGIS}/PlugIns/qgis
export DYLD_FRAMEWORK_PATH=${BQGIS}/Frameworks:/System/Library/Frameworks
export PYTHONPATH=${BQGIS}/Resources/python:${BQGIS}/Resources/python/plugins:/Library/Python/2.7/site-packages:$PYTHONPATH

# May need...
# export GDAL_DRIVER_PATH=<path-to>/gdalplugins
# export GRASS_PREFIX=<path-to>/grass-64/grass-6.4.4

# For development builds, based off of OSGeo4Mac: https://github.com/OSGeo/homebrew-osgeo4mac
# BQGIS=/Users/larrys/QGIS/github.com/QGIS_APPS_boundless/QGIS.app/Contents
# QGIS_PREFIX_PATH=${BQGIS}/MacOS
# export QGIS_PREFIX_PATH
# export PATH=${QGIS_PREFIX_PATH}/bin:/usr/local/bin:$PATH
# export DYLD_VERSIONED_LIBRARY_PATH=${QGIS_PREFIX_PATH}/lib:${BQGIS}/PlugIns/qgis:/usr/local/opt/sqlite/lib:/usr/local/opt/libxml2/lib:/usr/local/lib
# export DYLD_FRAMEWORK_PATH=/usr/local/Frameworks:/System/Library/Frameworks
# export PYTHONHOME=/usr/local/Frameworks/Python.framework/Versions/2.7
# export PYTHONPATH=${BQGIS}/Resources/python:${BQGIS}/Resources/python/plugins:/usr/local/lib/python2.7/site-packages:$PYTHONPATH
# export PYQGIS_STARTUP=/usr/local/opt/qgis-28/libexec/pyqgis_startup.py
# export GDAL_DRIVER_PATH=/usr/local/lib/gdalplugins
# export GRASS_PREFIX=/usr/local/opt/grass-64/grass-6.4.4

python ${SCRIPT_DIR}/ssl-conn-qt.py
