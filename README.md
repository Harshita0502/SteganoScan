# StegnoScan
StegnoScan is a Python-based digital forensics tool designed for steganography analysis and forensic examinations. This versatile tool assists in uncovering hidden information within various file types while providing a range of forensic analysis capabilities.

## Features:
Steganography Analysis: Detects and extracts concealed data within images, audio, videos, and documents.

Forensic Examination: Inspects binary data, metadata, and file structures for comprehensive forensic analysis.

Toolset: Integrates multiple steganography and forensic tools, including strings, hexdump, binwalk, steghide, zsteg, exiftool, and foremost.

User-Friendly Interface: Simple prompts enable easy file input and choice of forensic or steganographic analysis.

## Features Overview:
Strings Analysis: Extract readable text from binary files, search for specific words or strings of certain lengths.

Binwalk Tool: Identify and extract embedded files within other files, uncover hidden data structures.

Exiftool Insights: Extract metadata embedded within multimedia files, reveal camera details, timestamps, and geolocation data.

Hexdump Analysis: Display file contents in hexadecimal or ASCII formats, providing detailed binary insights.

Stegsolve Tool: Visualize hidden data within images using color plane manipulation techniques.

Steghide Functionality: Extract concealed data utilizing steganography, providing passphrase-based decryption.

Foremost Analysis: Assist in file carving and data recovery from digital media, essential in forensic investigations.

Zsteg Analysis: Detect hidden data in images through LSB steganography, revealing covert communication payloads.

## Why StegnoScan?
Security Enhancement: Reveals hidden content, fortifying security measures against covert communication methods.

Forensic Assistance: Aids in uncovering concealed evidence or activities in forensic investigations.

Versatility: Supports various file formats for steganographic and forensic analysis.

## Usage:
Installation: Ensure Python and required libraries are installed (see requirements.txt).
###### pip install -r requirements.txt
Run StegnoScan: Execute the python file and follow the prompts to input file paths and select analysis options.
###### python StegnoScan.py
Analysis Results: View extracted information or forensic analysis outputs for the chosen file.

## Limitations:
Effectiveness may vary based on the file type and steganographic method used.
Specific tools within StegnoScan may be more suitable for certain file formats.

## Requirements:
Python 3.6 or above
Libraries: subprocess, os

## Disclaimer:
StegnoScan is intended for educational and forensic purposes. Users should comply with legal regulations and ethical considerations. The tool's effectiveness may differ based on file types and hidden data nature.
