@echo off
chcp 437
%SystemRoot%\System32\reg.exe add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f >nul 2>&1
for /f "delims=" %%a in ('powershell -c "Write-Host ([char]27)"') do set "ESC=%%a"
cls
title YBDOS
set YBDOS_VER=1.00
for %%f in (config.bat SafeMod.bat Fsystem.bat COMMAND.COM) do (
    if exist "%%f" (
        echo [OK] %%f found.
    ) else (
        echo [ERROR] %%f is not found!
        echo Entering Safe Mode...
        pause
        call Fsystem.bat
        exit /b
    )
)

echo.
echo YBDOS %YBDOS_VER% startup
echo 1. Normal Mode
echo 2. Boot into Safe Mod.bat
echo 3. Boot without copy files
choice /c 123 /m "Enter a Choice"
set choice=%errorlevel%
if "%choice%"=="1" (
    if not exist ".\Backup" md ".\Backup"
    copy COMMAND.COM .\Backup
    copy config.bat .\Backup
    copy Fsystem.bat .\Backup
    copy SafeMod.bat .\Backup

)
if "%choice%"=="2" (
    	echo starting SafeMod.bat
	call SafeMod.bat
)
if "%choice%"=="3" (
    goto CheckCom
)

goto :eof

:CheckCom
if exist COMMAND.COM (
    call COMMAND.COM
    goto :eof
) else (
    set /p COMMAND_PATH="Bad or missing Command Interpreter. Please enter path> "
    if exist "%COMMAND_PATH%" (
        call "%COMMAND_PATH%"
        goto :eof
    ) else (
        echo Invalid path! Try again...
        goto CheckCom
    )
)
