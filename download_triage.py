import os
import shutil

# Ruta correcta para acceder a Windows desde WSL
# os.chdir("/mnt/c/Users/Mauro/Downloads")
os.chdir("/mnt/c/Users/Mauro/Desktop")
print(os.getcwd())

# Check number of files in directory
files = os.listdir()

# Imprimir la lista completa de archivos antes del procesamiento
print("\n" + "="*50)
print("ARCHIVOS ENCONTRADOS:")
print("="*50)
for i, file in enumerate(files, 1):
    if os.path.isfile(file):
        print(f"{i:2d}. {file}")
    else:
        print(f"{i:2d}. {file} (directorio)")
print("="*50)
print(f"Total de elementos: {len(files)}")
print("="*50 + "\n")

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

# Sort to specific folder depend on extensions
def sorting(file):
    keys = list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            if file.lower().endswith(ext.lower()):  # Case insensitive
                return key
    return None

# Crear directorio base si no existe
base_dir = "."
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Analizar qué categorías van a ser necesarias
categories_needed = set()
others_needed = False

for file in files:
    if os.path.isfile(file):  # Solo procesar archivos, no directorios
        category = sorting(file)
        if category:
            categories_needed.add(category)
        else:
            others_needed = True

# Crear solo las carpetas de categorías que van a ser utilizadas
for category in categories_needed:
    category_dir = os.path.join(base_dir, category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)

# Crear directorio "others" solo si es necesario
if others_needed:
    others_dir = os.path.join(base_dir, "others")
    if not os.path.exists(others_dir):
        os.makedirs(others_dir)

# Iterate through each file and move them
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
