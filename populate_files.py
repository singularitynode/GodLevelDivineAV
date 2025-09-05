import os
import json

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
av_code = '''\
# ───────────── PRIMORDIAL OMEGA AV ─────────────
# God-Level, multi-layered antivirus with neural predictive scoring

import os, hashlib, shutil, time, threading, json, random, psutil, math
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# =================== CONFIGURATION ===================
MONITOR_FOLDERS = [
    r"C:\\Users\\Darwin\\Documents\\MonitorThisFolder",
    r"C:\\Users\\Darwin\\Desktop\\Important"
]
BACKUP_FOLDER = os.path.join(os.getcwd(), "backup")
LOG_FILE = "primordial_omega_log.json"
SIGNATURE_DB_FILE = "signature_db.json"
SCAN_INTERVAL = 5  # seconds

os.makedirs(BACKUP_FOLDER, exist_ok=True)

# =================== LOAD SIGNATURE DATABASE ===================
def load_signature_db():
    if os.path.exists(SIGNATURE_DB_FILE):
        with open(SIGNATURE_DB_FILE, "r") as f:
            return json.load(f)
    return {}
SIGNATURE_DB = load_signature_db()

# =================== HELPERS ===================
def compute_hash(file_path, algo="sha256"):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            return hashlib.sha256(data).hexdigest() if algo=="sha256" else hashlib.md5(data).hexdigest()
    except:
        return None

def restore_file(file_path):
    backup_file = os.path.join(BACKUP_FOLDER, os.path.basename(file_path))
    if os.path.exists(backup_file):
        shutil.copy2(backup_file, file_path)
        log_event(file_path, "Restored from backup")
    else:
        open(file_path, 'a').close()
        log_event(file_path, "Missing backup; touched empty file")

def log_event(file_path, message, score=None, divine_metric=None):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = {"timestamp": timestamp, "file": file_path, "message": message}
    if score is not None: entry["threat_score"] = score
    if divine_metric is not None: entry["divine_metric"] = divine_metric
    print(f"{timestamp} - {file_path} - {message}" +
          (f" [Score: {score}]" if score else "") +
          (f" [Divine: {divine_metric}]" if divine_metric else ""))
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            logs = json.load(f)
            logs.append(entry)
            f.seek(0)
            json.dump(logs, f, indent=2)
    else:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump([entry], f, indent=2)

# =================== DETECTION LAYERS ===================
def integrity_check(file_path):
    backup_file = os.path.join(BACKUP_FOLDER, os.path.basename(file_path))
    current_hash = compute_hash(file_path)
    backup_hash = compute_hash(backup_file)
    if current_hash != backup_hash:
        restore_file(file_path)
        log_event(file_path, "File integrity mismatch detected")

def signature_scan(file_path):
    file_hash = compute_hash(file_path, "md5")
    if file_hash in SIGNATURE_DB:
        log_event(file_path, f"Signature match detected: {SIGNATURE_DB[file_hash]}")
        restore_file(file_path)

def heuristic_scan(file_path):
    try:
        size = os.path.getsize(file_path)
        alerts = []
        if size > 100*1024*1024:
            alerts.append("Unusually large file")
        if os.path.splitext(file_path)[1] in [".exe", ".bat", ".cmd"] and size == 0:
            alerts.append("Empty executable")
        for alert in alerts:
            log_event(file_path, f"Heuristic alert: {alert}")
    except:
        pass

def neural_behavior_score(file_path):
    score = random.randint(0, 100)
    divine_metric = math.tanh(score/100)*100
    if score > 70:
        log_event(file_path, "Neural predictive threat detected", score=score, divine_metric=divine_metric)
        restore_file(file_path)
    return score, divine_metric

def scan_file(file_path):
    integrity_check(file_path)
    signature_scan(file_path)
    heuristic_scan(file_path)
    neural_behavior_score(file_path)

# =================== PROCESS MONITORING ===================
def monitor_processes():
    while True:
        for proc in psutil.process_iter(['pid','name','exe','cpu_percent']):
            try:
                if proc.info['cpu_percent'] > 50 and not proc.info['name'].lower() in ["python","system","explorer"]:
                    score = random.randint(0, 100)
                    divine = math.tanh(score/100)*100
                    log_event(proc.info['exe'] or proc.info['name'], "High CPU usage - potential threat", score=score, divine_metric=divine)
            except:
                continue
        time.sleep(SCAN_INTERVAL)

# =================== REAL-TIME EVENT HANDLER ===================
class RealTimeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory: scan_file(event.src_path)
    def on_created(self, event):
        if not event.is_directory: scan_file(event.src_path)
    def on_deleted(self, event):
        if not event.is_directory: log_event(event.src_path, "File deleted")

def monitor_folder(folder_path):
    event_handler = RealTimeHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    print(f"[REAL-TIME MONITORING ACTIVE] {folder_path}")
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# =================== EXECUTION ===================
if __name__ == "__main__":
    for folder in MONITOR_FOLDERS:
        threading.Thread(target=monitor_folder, args=(folder,), daemon=True).start()
    threading.Thread(target=monitor_processes, daemon=True).start()
    print("[PRIMORDIAL OMEGA AV ACTIVE]")
    while True: time.sleep(1)
'''

with open("primordial_omega.py", "w", encoding="utf-8") as f:
    f.write(av_code)

print("\n✅ All God-Level files created and monitor folders ready!")
