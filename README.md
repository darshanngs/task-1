task-1
# Automated File Organizer

## 📌 Description

**Automated File Organizer** is a simple Python program that automatically organizes files in a selected folder into separate categories based on their file extensions.

It helps keep a folder clean and organized by moving files into appropriate subfolders such as **Documents, Images, Python_Code, and Other**.

## ✨ Features

* Organizes files automatically based on extensions.
* Creates category folders if they don't already exist.
* Moves files to the appropriate folders.
* Supports common file types:

  * `.txt` → Documents
  * `.pdf` → Documents
  * `.jpg` → Images
  * `.png` → Images
  * `.py` → Python_Code
* Unknown file types are moved to **Other**.

## 🛠️ Technologies Used

* **Python 3**
* `os` module
* `shutil` module

## 📂 Example

### Before running:

```text
Test_File/
├── notes.txt
├── resume.pdf
├── photo.jpg
├── image.png
├── program.py
└── video.mp4
```

### After running:

```text
Test_File/
├── Documents/
│   ├── notes.txt
│   └── resume.pdf
├── Images/
│   ├── photo.jpg
│   └── image.png
├── Python_Code/
│   └── program.py
└── Other/
    └── video.mp4
```

## ▶️ How to Run

1. Install **Python 3**.
2. Save the program as:

```text
File_Organizer.py
```

3. Open VS Code or Command Prompt.
4. Run:

```bash
python File_Organizer.py
```

5. Enter the folder path when asked:

```text
Enter folder path: C:\Users\darsh\OneDrive\Desktop\Test_File
```

**Do not add quotation marks** around the path.

## 📋 How It Works

The program:

1. Takes the folder path from the user.
2. Reads all files in the folder.
3. Gets each file's extension.
4. Checks the extension against the `categories` dictionary.
5. Creates the required category folder.
6. Moves the file into that folder.
7. Displays:

```text
Files organized successfully!
```

## 👨‍💻 Author

**Darshan G S**
Python File Organization Project
# task-1
autoamatic file organizer
