# File Organizer

A small command-line Python script that sorts files in a folder into
extension-based category folders.

## Requirements

- Python 3
- No third-party packages

## Technologies used

- **Python 3** — application language
- **`pathlib`** — path handling and filesystem checks
- **`shutil`** — moving files

## Run

From the project directory, run:

```bash
python3 organizer.py
```

When prompted, enter the path to the folder you want to organize. The script
checks that the path exists and is a directory, then moves files directly
inside it into category subfolders.

## Categories

| Folder | File extensions |
| --- | --- |
| `Documents` | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| `Images` | `.jpg`, `.jpeg`, `.png`, `.gif` |
| `Videos` | `.mp4`, `.mkv`, `.avi`, `.mov` |
| `Audio` | `.mp3`, `.wav`, `.aac` |
| `Applications` | `.exe`, `.dmg` |
| `Unknown` | Any other extension, or files without an extension |

Extensions are matched without regard to case. For example, `PHOTO.JPG` is
categorized as an image.

## Duplicate filenames

If a destination folder already contains a file with the same name, the script
adds a number before the extension until it finds an unused name. For example:
`report.pdf`, `report_1.pdf`, `report_2.pdf`.

## Output and errors

The script prints each successful move and a final count by category. If a move
fails because of permissions or another filesystem error, it prints an error
and continues with the remaining files.

## Notes

- Only files immediately inside the selected folder are processed; nested
  folders are not searched.
- Files are moved, not copied. Review the selected folder before running the
  script if you do not want its contents relocated.

## What I learned

- Working with files and directories in Python.
- Using `pathlib` for filesystem paths and checks.
- Moving files using `shutil`.
- Working with dictionaries and lists.
- Writing reusable functions.
- Using loops and conditional statements.
- Handling exceptions with `try` and `except`.
- Validating user input.
- Handling duplicate filenames.
- Structuring a Python program using functions.
- Using `if __name__ == "__main__":`.
- Using Git for version control.
- Writing project documentation.

# License

- This project was created for learning and educational purposes.


