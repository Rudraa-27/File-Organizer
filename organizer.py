from pathlib import Path
import shutil

def uniquePath(destination):
    counter = 1
    newDestination = destination

    while destination.exists():
        destination = (newDestination.parent / f"{newDestination.stem}_{counter}{newDestination.suffix}")
        counter += 1

    return destination

def find_category(extension, categories):
    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Unknown"

def move_file(file, destination):
    try:
        shutil.move(file, destination)
        return True

    except PermissionError:
        print(f"Permission denied: {file.name}")

    except Exception as e:
        print(f"Could not move {file.name}: {e}")

    return False

def organize_files(folder, categories):
    summary = {}

    for file in folder.iterdir():

        if not file.is_file():
            continue

        extension = file.suffix.lower()
        category = find_category(extension, categories)

        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)

        destination = uniquePath(
            category_folder / file.name
        )

        if move_file(file, destination):
            print(file.name, "->", category)

            summary[category] = summary.get(category, 0) + 1

    return summary


categories = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Applications": [".exe", ".dmg"],
}

def main():
    folder = Path(input("Enter folder path: "))

    if not folder.exists():
        print("Error: The folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: The path is not a folder.")
        return

    summary =  organize_files(folder, categories)

    print("\nOrganization complete!")

    total_files = sum(summary.values())
    print(f"Files organized: {total_files}")

    for category, count in summary.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()