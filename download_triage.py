import os
import shutil

# Ruta correcta para acceder a Windows desde WSL
os.chdir("/mnt/c/Users/Mauro/Desktop/triageTest")
print(os.getcwd())

# Check number of files in directory
files = os.listdir()

# List of extensions (You can add more if you want)
extentions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"]
}

# Crear directorios de destino si no existen
base_dir = "./folder-sorting"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for category in extentions.keys():
    category_dir = os.path.join(base_dir, category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)

# Crear directorio "others" también
others_dir = os.path.join(base_dir, "others")
if not os.path.exists(others_dir):
    os.makedirs(others_dir)

# Sort to specific folder depend on extensions
def sorting(file):
    keys = list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            if file.lower().endswith(ext.lower()):  # Case insensitive
                return key
    return None

# Iterate through each file
for file in files:
    if os.path.isfile(file):  # Solo procesar archivos, no directorios
        dist = sorting(file)
        if dist:
            try:
                shutil.move(file, os.path.join(base_dir, dist, file))
                print(f"Moved {file} to {dist}")
            except FileExistsError:
                print(f"{file} already exists in {dist}")
            except Exception as e:
                print(f"Error moving {file}: {e}")
        else:
            try:
                shutil.move(file, os.path.join(base_dir, "others", file))
                print(f"Moved {file} to others")
            except FileExistsError:
                print(f"{file} already exists in others")
            except Exception as e:
                print(f"Error moving {file}: {e}")
