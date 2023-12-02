import os
import subprocess

def get_file_size(file_path):
    return os.path.getsize(file_path)

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        return result.stdout
    except FileNotFoundError:
        return f"{command[0]} not found. Please install {command[0]}."

def run_zsteg(image_path):
    return run_command(f"zsteg {image_path}")

def run_steghide_extract(image_path, passphrase):
    return run_command(f"steghide extract -sf {image_path} -p {passphrase}")

def run_stegsolve():
    try:
        subprocess.run(['java', '-jar', 'stegsolve.jar'])
    except FileNotFoundError:
        return "Stegsolve not found. Please make sure Java is installed and download stegsolve.jar."

def run_strings(file_path, length=None, word=None):
    strings_cmd = "strings"
    if length:
        strings_cmd += f" -n {length}"
    if word:
        strings_cmd += f" | grep '{word}'"
    return run_command(f"{strings_cmd} {file_path}")

def run_binwalk(file_path):
    return run_command(f"binwalk {file_path}")

def extract_binwalk_files(file_path):
    try:
        output = subprocess.check_output(f"binwalk -e {file_path}", shell=True, stderr=subprocess.STDOUT, text=True)
        extracted_folder = file_path + "_extracted"
        return f"Binwalk extraction successful. Extracted files in: {extracted_folder}"
    except subprocess.CalledProcessError as e:
        return f"Error extracting files: {e.output}"

def run_foremost(file_path):
    return run_command(f"foremost -i {file_path}")
    
def extract_foremost_files(file_path):
    try:
        output = subprocess.check_output(f"foremost -i {file_path} -o foremost_output", shell=True, stderr=subprocess.STDOUT, text=True)
        return "Foremost extraction successful. Extracted files in: foremost_output"
    except subprocess.CalledProcessError as e:
        return f"Error extracting files: {e.output}"

def run_exiftool(file_path):
    return run_command(f"exiftool {file_path}")

def run_hexdump(file_path):
    return run_command(f"hexdump -C {file_path}")
    
logo =''' 
 
███████╗████████╗███████╗ ██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗████╗  ██║██╔═══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
███████╗   ██║   █████╗  ██║  ███╗███████║██╔██╗ ██║██║   ██║███████╗██║     ███████║██╔██╗ ██║
╚════██║   ██║   ██╔══╝  ██║   ██║██╔══██║██║╚██╗██║██║   ██║╚════██║██║     ██╔══██║██║╚██╗██║
███████║   ██║   ███████╗╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
'''
print(logo)                         
print("Welcome to the SteganoScan - Universal Steganography Tool!")
print("Choose the feature you want to use:")
print("1. Strings")
print("2. Binwalk (and extract files)")
print("3. Exiftool")
print("4. Hexdump")
print("5. Stegsolve")
print("6. Steghide")
print("7. Foremost")
print("8. Zsteg")
print("9. Exit")

def get_user_choice():
    choice = input("Enter the number of the feature you want to use: ")
    return int(choice)

def get_file_name():
    file_name = input("Enter the file name/path you want to analyze: ")
    return file_name

# Main functionality
while True:
    feature = get_user_choice()
    if feature in [1, 2, 3, 4, 6, 7, 8]:
        file_name = get_file_name()
        file_size = get_file_size(file_name)
        
        if file_size > 1024 * 1024 * 1024:  # Check if file size is greater than 1 GB
            print("File size exceeds 1 GB. Please select a smaller file.")
            continue

    if feature == 1:
        file_name = get_file_name()
        search_length = input("Do you want to search by length? (y/n): ").lower()
        search_word = input("Do you want to search by a word? (y/n): ").lower()

        if search_length == 'y':
            length = int(input("Enter the string length: "))
        else:
            length = None

        if search_word == 'y':
            word = input("Enter the word to search: ")
        else:
            word = None

        print("Strings Output:")
        print(run_strings(file_name, length, word))

    elif feature == 2:
        file_name = get_file_name()
        print("Binwalk Output:")
        print(run_binwalk(file_name))

        download_choice = input("Do you want to extract files found by Binwalk? (y/n): ").lower()
        if download_choice == 'y':
            extraction_result = extract_binwalk_files(file_name)
            print(extraction_result)
    
    elif feature == 3:
        file_name = get_file_name()
        print("Exiftool Output:")
        print(run_exiftool(file_name))        

    elif feature == 4:
        file_name = get_file_name()
        print("Hexdump Output:")
        print(run_hexdump(file_name))

    elif feature == 5:
        print("Running Stegsolve...")
        stegsolve_result = run_stegsolve()
        if stegsolve_result == "Stegsolve not found.":
            install_stegsolve = input("Stegsolve is not installed. Do you want to install it? (y/n): ").lower()
            if install_stegsolve == 'y':
                subprocess.run(['wget', 'http://www.caesum.com/handbook/Stegsolve.jar', '-O', 'stegsolve.jar'])
                print("Stegsolve installed successfully.")
            else:
                print("Stegsolve is not installed.")

    elif feature == 6:
        file_name = get_file_name()
        image_file = get_file_name()
        passphrase = input("Enter the passphrase: ")
        print("Steghide Extraction Output:")
        print(run_steghide_extract(image_file, passphrase))

    elif feature == 7:
        file_name = get_file_name()
        print("Foremost Output:")
        print(run_foremost(file_name))
        download_choice = input("Do you want to extract files found by Foremost? (y/n): ").lower()
        if download_choice == 'y':
            extraction_result = extract_foremost_files(file_name)
            print(extraction_result)

    elif feature == 8:
        image_file = get_file_name()
        print("Zsteg Output:")
        print(run_zsteg(image_file))

    elif feature == 9:
        print("Exiting SteganoScan.")
        break

    else:
        print("Invalid choice. Please choose a number between 1 and 9 for the feature.")

    run_again = input("Do you want to run another command? (y/n): ").lower()
    if run_again != 'y':
        print("Exiting SteganoScan.")
        break
