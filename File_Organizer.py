import os
import shutil

folder = input("Enter folder path: ")

categories = {
    ".txt": "Documents",
    ".pdf": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".py": "Python_Code"
}

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        category = categories.get(extension, "Other")

        new_folder = os.path.join(folder, category)

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        shutil.move(file_path, os.path.join(new_folder, file))

print("Files organized successfully!")