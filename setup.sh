#!/bin/bash

echo "=== SteganoScan Automated Setup ==="

# Update package lists
sudo apt update

# Install essential system tools
echo "[+] Installing required tools..."
sudo apt install -y binwalk libimage-exiftool-perl foremost steghide default-jre wget

# Check for Ruby (required for zsteg)
if ! command -v ruby &> /dev/null
then
    echo "[!] Ruby not found. Please install Ruby manually to use zsteg:"
    echo "    sudo apt install ruby-full"
else
    echo "[+] Ruby found. Installing zsteg..."
    sudo gem install zsteg
fi

# Download Stegsolve if missing
if [ ! -f "stegsolve.jar" ]; then
    echo "[+] Downloading Stegsolve..."
    wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
else
    echo "[*] Stegsolve.jar already exists. Skipping download."
fi

# Install Python dependencies
pip3 install -r requirements.txt

echo "[+] Setup completed successfully."
echo "[+] Launching SteganoScan..."

sleep 2
python3 main.py
