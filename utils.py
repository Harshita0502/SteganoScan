import os
from PIL import Image
import matplotlib.pyplot as plt

# Simple known stego signature patterns (expandable)
STEGO_SIGNATURES = [
    b"STEGO",
    b"HIDDEN",
    b"SECRET",
    b"\x00\x00\x00\x1Cftyp",  # Example suspicious file header in unexpected places
]

def print_banner():
    banner = r'''
███████╗████████╗███████╗ ██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗████╗  ██║██╔═══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
███████╗   ██║   █████╗  ██║  ███╗███████║██╔██╗ ██║██║   ██║███████╗██║     ███████║██╔██╗ ██║
╚════██║   ██║   ██╔══╝  ██║   ██║██╔══██║██║╚██╗██║██║   ██║╚════██║██║     ██╔══██║██║╚██╗██║
███████║   ██║   ███████╗╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
'''
    print(banner)
    print("Welcome to SteganoScan - Universal Steganography Tool\n")

def validate_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"File is empty: {file_path}")

def is_supported_file(file_path, extensions):
    return file_path.lower().endswith(extensions)

def check_signatures(file_path):
    try:
        with open(file_path, "rb") as f:
            content = f.read()
            for sig in STEGO_SIGNATURES:
                if sig in content:
                    return True
        return False
    except Exception as e:
        print(f"[!] Error checking signatures: {e}")
        return False

def generate_histogram(file_path):
    try:
        img = Image.open(file_path)
        plt.figure(figsize=(10, 4))
        plt.title("Image Histogram")
        plt.xlabel("Pixel value")
        plt.ylabel("Frequency")
        plt.hist(list(img.convert("L").getdata()), bins=256, color='gray', alpha=0.7)
        plt.show()
    except Exception as e:
        print(f"[!] Histogram generation failed: {e}")

def analyze_color_channels(file_path):
    try:
        img = Image.open(file_path)
        channels = img.split()
        colors = ["Red", "Green", "Blue"]

        for i, channel in enumerate(channels):
            plt.figure()
            plt.title(f"{colors[i]} Channel")
            plt.imshow(channel, cmap='gray')
            plt.axis("off")
        plt.show()
    except Exception as e:
        print(f"[!] Color channel analysis failed: {e}")
