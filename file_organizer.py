import os
import shutil

def organize_files():
    folder_path = "automation_demo"
    os.makedirs(folder_path, exist_ok=True)

    # Create sample files automatically
    samples = {
        "notes.txt": "This is a sample document.",
        "report.pdf": "Demo PDF file",
        "photo.jpg": "Demo image file"
    }

    for filename, content in samples.items():
        file_path = os.path.join(folder_path, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(content)

    categories = {
        "Documents": [".txt", ".pdf", ".docx"],
        "Images": [".jpg", ".jpeg", ".png"],
        "Others": []
    }

    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)

        if os.path.isfile(source):
            extension = os.path.splitext(filename)[1].lower()
            category = "Others"

            for name, extensions in categories.items():
                if extension in extensions:
                    category = name
                    break

            destination_folder = os.path.join(folder_path, category)
            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(destination_folder, filename)

            if not os.path.exists(destination):
                shutil.move(source, destination)
                print(f"Organized: {filename} -> {category}")

    print("\nAutomation completed successfully!")

if __name__ == "__main__":
    organize_files()