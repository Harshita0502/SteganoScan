import os
import tkinter as tk
from tkinter import filedialog
from tools import (
    run_strings, run_binwalk, extract_binwalk_files, run_exiftool, run_hexdump,
    run_zsteg, run_stegsolve
)
from utils import (
    print_banner, validate_file, is_supported_file,
    generate_histogram, analyze_color_channels, check_signatures
)

OUTPUT_DIR = "output"
SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".wav")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def menu():
    print("\nSelect an option:")
    print("1. Strings")
    print("2. Binwalk (and extract)")
    print("3. Exiftool")
    print("4. Hexdump")
    print("5. Zsteg")
    print("6. Histogram Analysis")
    print("7. Color Channel Analysis")
    print("8. Stegsolve")
    print("9. Exit")

def get_choice():
    try:
        return int(input("Enter choice (1-9): "))
    except ValueError:
        return 0

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select file for analysis",
        filetypes=[("Supported files", "*.jpg *.jpeg *.png *.bmp *.wav")]
    )
    return file_path

def analyze_file(file_path, tool):
    try:
        validate_file(file_path)
        if not is_supported_file(file_path, SUPPORTED_EXTENSIONS):
            print(f"[!] Unsupported file type: {file_path}")
            return

        print(f"\nAnalyzing {file_path} with {tool}...\n")

        if check_signatures(file_path):
            print("[!] Suspicious signature detected.\n")

        output = ""

        if tool == "strings":
            word = None
            length = None

            word_filter = input("Do you want to search for a specific word? (y/n): ").lower()
            if word_filter == "y":
                word = input("Enter the word to search for: ")

            length_filter = input("Do you want to filter by string length? (y/n): ").lower()
            if length_filter == "y":
                try:
                    length = int(input("Enter minimum string length: "))
                except ValueError:
                    print("Invalid length. Skipping length filter.")

            output = run_strings(file_path, length, word)

        elif tool == "binwalk":
            output = run_binwalk(file_path)
            print(output)
            extract = input("Do you want to extract hidden files if found? (y/n): ").lower()
            if extract == "y":
                output += f"\n{extract_binwalk_files(file_path)}\n"

        elif tool == "exiftool":
            output = run_exiftool(file_path)
        elif tool == "hexdump":
            output = run_hexdump(file_path)
        elif tool == "zsteg":
            output = run_zsteg(file_path)
        elif tool == "histogram":
            generate_histogram(file_path)
            return
        elif tool == "channels":
            analyze_color_channels(file_path)
            return
        else:
            print("[!] Unknown tool")
            return

        print(output)
        export = input("\nExport output to file? (y/n): ").lower()
        if export == "y" and output:
            export_path = os.path.join(OUTPUT_DIR, f"{os.path.basename(file_path)}_{tool}.txt")
            with open(export_path, "w") as f:
                f.write(output)
            print(f"[+] Output saved to {export_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print_banner()

    while True:
        ask = input("\nDo you want to select a file for analysis? (y/n): ").lower()
        if ask != "y":
            print("Exiting SteganoScan.")
            break

        file_path = select_file()
        if not file_path:
            print("No file selected. Returning to main menu.")
            continue

        while True:
            menu()
            choice = get_choice()

            if choice in [1, 2, 3, 4, 5, 6, 7]:
                tools = {
                    1: "strings",
                    2: "binwalk",
                    3: "exiftool",
                    4: "hexdump",
                    5: "zsteg",
                    6: "histogram",
                    7: "channels"
                }
                analyze_file(file_path, tools[choice])

            elif choice == 8:
                run_stegsolve()

            elif choice == 9:
                print("Returning to file selection menu.")
                break

            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
