@echo off

winget install --silent --accept-source-agreements --exact --id astral-sh.uv || goto :error
goto :EOF

:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%