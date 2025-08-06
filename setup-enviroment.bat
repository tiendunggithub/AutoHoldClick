@echo off

rem Kiểm tra xem Python có tồn tại trong PATH hay không
where python >nul 2>nul
if %errorlevel% equ 0 (
    echo Python is installed.
    python --version
    pip install keyboard
    pip install pyautogui
    pip install pynput
    echo ===Environment setup complete.===
) else (
    echo Python is not installed.
)

pause