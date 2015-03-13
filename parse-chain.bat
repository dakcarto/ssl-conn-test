@echo off
SET OSGEO4W_ROOT=%ProgramFiles(x86)%\Boundless\QGIS\qgis
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
path %OSGEO4W_ROOT%\apps\qgis\bin;%PATH%

set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%

cmd /k python.exe "%~dp0\parse-chain.py" %*
