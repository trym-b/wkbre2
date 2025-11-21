@echo off

set REPO_ROOT_DIR=%~dp0\..\..

set CURRENT_DIR=%cd%

mkdir "%REPO_ROOT_DIR%\build\3rdParty" || goto :error
cd "%REPO_ROOT_DIR%\build\3rdParty" || goto :error
git clone https://github.com/microsoft/vcpkg.git || goto :error
"%REPO_ROOT_DIR%\build\3rdParty\vcpkg\bootstrap-vcpkg.bat" -disableMetrics || goto :error
cd "%CURRENT_DIR%" || goto :error
goto :EOF

:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%