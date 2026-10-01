from pathlib import Path
import shutil

def uniquePath(destination):
    counter = 1
    newDestination = destination

    while destination.exists():
        destination = (newDestination.parent / f"{newDestination.stem}_{counter}{newDestination.suffix}")
        counter += 1

    return destination

folder = Path(input("Enter the folder path: "))

if not folder.exists():
    print("Error: The folder does not exist.")
    exit()

if not folder.is_dir():
    print("Error: The path is not a folder.")
    exit()

categories = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Applications": [".exe", ".dmg"],
}

for file in folder.iterdir():
  if file.is_file(): 
     
     extension = file.suffix.lower()
     foundCategory = False

     for category, extensions in categories.items():
          if extension in extensions:
              folderCategory = folder / category
              folderCategory.mkdir(exist_ok=True)

              destination = uniquePath(folderCategory / file.name)

              try:
                shutil.move(file, destination)
                print(file.name, "->", category)
              except PermissionError:
                print(f"Permission denied: {file.name}")
              except Exception as e:
                print(f"Could not move {file.name}: {e}")
              
              foundCategory = True
              break

     if not foundCategory:
        unknownCategory = folder / "Unknown"
        unknownCategory.mkdir(exist_ok=True)

        destination = uniquePath(unknownCategory / file.name)

        try:
            shutil.move(file, destination)
            print(file.name, "->", "Unknown")
        except PermissionError:
            print(f"Permission denied: {file.name}")
        except Exception as e:
            print(f"Could not move {file.name}: {e}")

              

