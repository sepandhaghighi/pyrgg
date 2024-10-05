@echo off
FOR /F "tokens=* USEBACKQ" %%F IN (`python --version`) DO (
SET py_version_str=%%F
)
SET py_version=%py_version_str:~7%

echo Your Python Version : %py_version%
echo Recommended Python Version : ^>= 3.6
echo -----
echo -----
python -m PyInstaller PYRGG.spec
pause