# SteganoScan - Steganography-Focused Analysis Framework

SteganoScan is a modular, menu-driven steganography analysis toolkit designed to assist in the detection and extraction of hidden data within media files. Developed as part of my final-year cybersecurity project, this tool consolidates commonly used steganalysis utilities into a single, automated workflow tailored for forensic analysts, CTF participants, and security researchers.

---

## 🎯 Project Overview

**Objective:**  
To provide a focused, reliable, and beginner-friendly framework for detecting and analyzing steganography in images and audio files. SteganoScan aims to reduce manual effort in forensic investigations while maintaining strict adherence to steganography-specific techniques.

**Why SteganoScan?**  
Existing forensic tools often mix general-purpose file analysis with stego detection, leading to bloated workflows. SteganoScan addresses this by isolating and automating proven steganalysis techniques in a controlled, interactive environment.

---

## ✅ Key Features

- 🔍 **Strings Analysis**  
  Extract printable strings with optional keyword search and length filtering.

- 🛠 **Binwalk Integration**  
  Scan files for embedded data and optionally extract hidden content.

- 🗂 **ExifTool Metadata Extraction**  
  Identify hidden metadata within supported file formats.

- 🧩 **Hexdump Viewer**  
  Byte-level inspection for manual anomaly detection.

- 🟡 **Zsteg Automation**  
  Detect LSB-based steganography in PNG files.

- 📊 **Histogram Generation**  
  Visualize pixel distributions to reveal hidden patterns.

- 🎨 **Color Channel Separation**  
  Analyze individual RGB channels for stego artifacts.

- 🖼 **Stegsolve Integration**  
  Launch Stegsolve for advanced layer and color space inspection.

- 🚩 **Signature-Based Suspicion Alerts**  
  Lightweight detection of known suspicious patterns or steganography markers.

- 🖥 **Intuitive Menu-Driven Workflow**  
  Designed for beginners and professionals — no CLI arguments required.

---

## 🧰 Supported File Formats

- Image: `.jpg`, `.jpeg`, `.png`, `.bmp`  
- Audio: `.wav`  

---

## 🏗 Technical Stack
```bash
| Component      | Purpose                                 |
|----------------|-----------------------------------------|
| Python 3.x     | Core application and logic framework    |
| `binwalk`      | Detection of hidden files and data      |
| `exiftool`     | Metadata extraction                    |
| `foremost`     | File carving and data recovery          |
| `steghide`     | Hidden data extraction from images/audio|
| `zsteg`        | LSB steganography detection (PNG)       |
| `Stegsolve.jar`| Visual layer and filter inspection      |

> The setup script handles automatic installation of all dependencies where possible.
```
---

## 🚀 Quick Setup & Execution

### 1. Clone the Repository

```bash
git clone https://github.com/Harshita0502/SteganoScan.git
cd SteganoScan
```
2. Automated Setup & Launch
```bash
./setup.sh
```
### The setup script:
- Installs required system tools
- Installs zsteg if Ruby is available
- Downloads Stegsolve.jar if missing
- Installs Python dependencies
- Launches the application

### Typical Use Case:
Launch SteganoScan
Select a target file via interactive dialog
Choose desired steganalysis tool from the menu
Review results directly or export them to the /output folder
Optional: Visual analysis via Stegsolve

### 📁 Project Structure
```bash
SteganoScan/
├── main.py            # Main application logic (menu-driven)
├── tools.py           # External tool integrations
├── utils.py           # File validation, visualization, helpers
├── requirements.txt   # Python dependencies
├── setup.sh           # Automated setup and launcher
├── stegsolve.jar      # Visual stego inspection tool (auto-downloaded)
├── output/            # Stores exported results
└── README.md          # Project documentation
```
## POC:
- Automated Download:
[Screenshots/Screenshot 2025-06-27 020547.png](https://github.com/Harshita0502/SteganoScan/blob/main/Screenshots/Screenshot%202025-06-27%20020547.png)
- SteganoScan Initialisation:

- Menu Driven Tool:

- Demo Histogram Scan:

- Demo Stegsolve Scan:


## 💡 Technical Learning & Development Takeaways
This project strengthened my understanding of:
- Practical application of steganography detection techniques
- Integration of external security tools into automated Python workflows
- Secure file handling, validation, and basic anomaly detection principles
- Interactive tool design suitable for forensic workflows
- The importance of minimizing manual steps in real-world stego analysis
- Visual steganalysis techniques (histograms, color channels, Stegsolve)
- Building modular, scalable security tools for practical environments

## 🔧 Future Enhancements (Planned)
- Batch analysis mode for large datasets
- Advanced anomaly detection using stego-specific heuristics
- Risk scoring system for suspicious files
- Report generation (e.g., PDF summaries)
- Optional GUI wrapper for non-technical users
- Expanded signature database for pattern detection
