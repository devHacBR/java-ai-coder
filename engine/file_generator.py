# engine/file_generator.py

import os

def save_project_structure(files):
    """
    Save each file to disk inside a 'generated_projects' folder.
    """
    base_dir = "generated_projects"
    os.makedirs(base_dir, exist_ok=True)

    for file in files:
        file_path = os.path.join(base_dir, file["path"])
        with open(file_path, "w") as f:
            f.write(file["content"])
        print(f"💾 Saved: {file_path}")
