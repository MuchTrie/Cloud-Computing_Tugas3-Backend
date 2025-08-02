@echo off
echo ===================================
echo    BACKEND FLASK STARTER SCRIPT
echo ===================================
echo.

REM Pindah ke direktori Backend
cd /d "%~dp0"

echo [INFO] Mengecek Python...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak ditemukan! Pastikan Python sudah terinstall.
    pause
    exit /b 1
)

echo.
echo [INFO] Mengecek pip...
pip --version
if %errorlevel% neq 0 (
    echo [ERROR] pip tidak ditemukan!
    pause
    exit /b 1
)

echo.
echo [INFO] Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo [ERROR] Gagal menginstall dependencies!
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Dependencies berhasil diinstall!
echo.
echo [INFO] Memulai Flask server...
echo [INFO] Backend akan berjalan di: http://localhost:5000
echo [INFO] Tekan Ctrl+C untuk menghentikan server
echo.

python app.py

pause
