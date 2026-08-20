import os
import sys

# Define patterns that indicate risks
SYSTEM_PROMPT_PATTERNS = ["SYSTEM_PROMPT", "system_message", '"role": "system"']
INJECTION_PHRASES = ["ignore previous instructions", "you are now", "pretend you are"]

def scan_files():
    violations = False
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    for pattern in SYSTEM_PROMPT_PATTERNS + INJECTION_PHRASES:
                        if pattern in content:
                            print(f"[!] VIOLATION in {file}: Found '{pattern}'")
                            violations = True
    if violations:
        sys.exit(1)
    print("Security Gate Passed!")
    sys.exit(0)

if __name__ == "__main__":
    scan_files()
