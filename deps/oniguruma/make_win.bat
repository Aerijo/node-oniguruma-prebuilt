call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\Common7\Tools\VsDevCmd.bat" -host_arch=amd64 -arch=amd64
call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\Common7\Tools\VsDevCmd.bat" -test

SET ONIG_DIR=%~dp0\src
set THIS_DIR=%~dp0
set BUILD_DIR=%cd%
copy %ONIG_DIR%\config.h.windows.in %BUILD_DIR%\config.h
nmake -f %ONIG_DIR%\Makefile.windows %1
