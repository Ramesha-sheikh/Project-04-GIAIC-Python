# Project: Bulk File Renamer
# Yeh project ek folder ke andar mojood tamam files ke naam ek specified pattern ke mutabiq rename karne ke liye hai.

# Required Library:
# is project ke liye aapko `os` install karne ki zaroorat nahi, yeh built-in hoti hai.

import os

def rename_files(folder_path, prefix):
    """Diye gaye folder ke andar mojood tamam files ko naye prefix ke saath rename karega."""
    try:
        files = os.listdir(folder_path)
        for index, file in enumerate(files):
            file_extension = os.path.splitext(file)[1]  # File extension nikalna
            new_name = f"{prefix}_{index+1}{file_extension}"
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
        print("Tamam files successfully rename ho gayi hain!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_path = input("Folder ka path enter karein: ")
    prefix = input("Naya prefix enter karein: ")
    rename_files(folder_path, prefix)
