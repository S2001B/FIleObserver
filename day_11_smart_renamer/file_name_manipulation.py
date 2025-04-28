import json
import os
from datetime import datetime

def rename_file(filename: str, folder_path: str) -> str:
    """
    Renames a PDF file based on any keyword found in rename_rules.json.
    Replaces {date} with today's date and renames the file on disk.

    Returns the new filename if changed, else returns original.
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    rules_path = os.path.join(current_dir, "rename_rules.json")

    # Load renaming rules from JSON
    with open(rules_path, "r") as rule_file:
        rename_rules = json.load(rule_file)

    if not filename.lower().endswith(".pdf"):
        return filename  # Only renaming .pdf files

    file_date = datetime.now().strftime("%Y-%m-%d")
    filename_lower = filename.lower()

    # Check for a keyword match anywhere in the filename
    for keyword, pattern in rename_rules.items():
        if keyword.lower() in filename_lower:
            new_name = pattern.replace("{date}", file_date)

            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)

            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                # print(f"[Renamer] {filename} → {new_name}")
                return new_name
            else:
                # print(f"[Renamer] WARNING: File '{old_path}' not found.")
                return filename  # Failsafe: return original if file missing

    return filename  # No keyword match, return unchanged
