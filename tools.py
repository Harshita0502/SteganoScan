import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        return result.stdout.strip()
    except Exception as e:
        return f"[!] Error running command: {e}"

def run_strings(file_path, length=None, word=None):
    cmd = f"strings"
    if length:
        cmd += f" -n {length}"
    cmd += f" {file_path}"
    if word:
        cmd += f" | grep '{word}'"
    return run_command(cmd)

def run_binwalk(file_path):
    return run_command(f"binwalk {file_path}")

def extract_binwalk_files(file_path):
    try:
        output = subprocess.check_output(f"binwalk -e {file_path}", shell=True, stderr=subprocess.STDOUT, text=True)
        return "[+] Binwalk extraction completed."
    except subprocess.CalledProcessError as e:
        return f"[!] Binwalk extraction error:\n{e.output}"

def run_exiftool(file_path):
    return run_command(f"exiftool {file_path}")

def run_hexdump(file_path):
    return run_command(f"hexdump -C {file_path}")

def run_zsteg(file_path):
    return run_command(f"zsteg {file_path}")

def run_stegsolve():
    try:
        subprocess.run(['java', '-jar', 'stegsolve.jar'])
    except FileNotFoundError:
        print("[!] Stegsolve or Java not found. Please ensure stegsolve.jar is in the same directory and Java is installed.")
