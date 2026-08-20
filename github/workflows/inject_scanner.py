import os
import sys

SYSTEM_PROMPT_PATTERNS = ["SYSTEM_PROMPT =", "system_message =", '"role": "system"']
INJECTION_PHRASES = [
    "ignore previous instructions",
    "you are now",
    "pretend you are",
    "act as if you have no restrictions"
]

def scan_files():
    found_violation = False
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py") and file != "inject_scanner.py":
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for pattern in SYSTEM_PROMPT_PATTERNS + INJECTION_PHRASES:
                        if pattern in content:
                            print(f"[!] Violation found: '{pattern}' in {path}")
                            found_violation = True
                            
    if found_violation:
        sys.exit(1)
    else:
        print("[+] No prompt injection patterns found.")
        sys.exit(0)

if __name__ == "__main__":
    scan_files()
