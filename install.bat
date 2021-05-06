:: fchooser.bat
:: launches a folder chooser and outputs choice to the console
:: https://stackoverflow.com/a/15885133/1683264

@echo off
setlocal

set "psCommand="(new-object -COM 'Shell.Application')^
.BrowseForFolder(0,'Please choose a folder.',0,0).self.path""

for /f "usebackq delims=" %%I in (`powershell %psCommand%`) do set "folder=%%I"

setlocal enabledelayedexpansion

copy ultimate.py "%folder%\ultimate.py"
copy fast_encryption.py "%folder%\fast_encryption.py"

echo python "%folder%\ultimate.py" > "%folder%"\efs.bat

echo python "%folder%\fast_encryption.py" > "%folder%"\fast_encryption1.bat

endlocal
