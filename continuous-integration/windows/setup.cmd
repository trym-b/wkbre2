@echo off

set REPO_ROOT_DIR=%~dp0\..\..
set CURRENT_DIR=%cd%

call "%REPO_ROOT_DIR%\continuous-integration\windows\install_uv.cmd" || goto :error
call "%REPO_ROOT_DIR%\continuous-integration\windows\install_vcpkg.cmd" || goto :error

goto :EOF

:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%