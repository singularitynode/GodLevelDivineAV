import os
import json
import subprocess
import sys

# ------------------- MONITOR FOLDERS -------------------
MONITOR_FOLDERS = [
    r"C:\Users\Darwin\Documents\MonitorThisFolder",
    r"C:\Users\Darwin\Desktop\Important"
]

for folder in MONITOR_FOLDERS:
    os.makedirs(folder, exist_ok=True)
    print(f"✅ Monitor folder ready: {folder}")

# ------------------- LICENSE -------------------
license_text = """MIT License

Copyright (c) 2025 singularitynode

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

... (MIT license full text) ...
"""

with open("LICENSE", "w", encoding="utf-8") as f:
    f.write(license_text)

# ------------------- README.md -------------------
readme_text = """# Primordial Omega AV

**Primordial Omega AV** is the God-Level antivirus prototype with:

- Real-time multi-layered file, process, and behavior monitoring
- Neural predictive threat scoring & divine metrics
- Self-healing backups and integrity verification
- Signature-based and heuristic advanced detection

Folder is auto-populated for immediate use.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_text)

# ------------------- signature_db.json -------------------
signature_db = {
    "primordial_omega_core": "Primordial Omega God-level signature",
    "d41d8cd98f00b204e9800998ecf8427e": "Empty placeholder file",
    "e3b0c44298fc1c149afbf4c8996fb924": "Advanced test signature"
}

with open("signature_db.json", "w", encoding="utf-8") as f:
    json.dump(signature_db, f, indent=2)

# ------------------- primordial_omega.py -------------------
av_code = """(PUT THE FULL UPDATED PRIMORDIAL_OMEGA.PY CODE HERE)
"""

with open("primordial_omega.py", "w", encoding="utf-8") as f:
    f.write(av_code)

# ------------------- CREATE EXE -------------------
print("\n⚡ Building standalone EXE...")
try:
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pyinstaller"], check=True)
    # Build EXE: onefile, console visible
    subprocess.run([
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--noconfirm",
        "primordial_omega.py"
    ], check=True)
    print("✅ EXE build complete! Check the 'dist' folder.")
except subprocess.CalledProcessError as e:
    print("❌ Error during EXE build:", e)

print("\n✅ All God-Level files created and monitor folders ready!")
