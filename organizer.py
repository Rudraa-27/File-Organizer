from pathlib import Path
import shutil

folder = Path(input("Enter the folder path: "))

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

     for category, extensions in categories.items():
          if extension in extensions:
              folderCategory = folder / category
              folderCategory.mkdir(exist_ok=True)

              shutil.move(file, folderCategory / file.name)
              
              print(file.name, "->", category)

              


