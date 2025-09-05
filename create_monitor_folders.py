import os

# Listahan ng folders na gusto mong i-monitor
folders_to_create = [
    r"C:\Users\Darwin\Documents\MonitorThisFolder",
    r"C:\Users\Darwin\Desktop\Important"
]

for folder in folders_to_create:
    os.makedirs(folder, exist_ok=True)
    print(f"✅ Folder ready: {folder}")

print("\nAll monitor folders are now created or already exist.")
