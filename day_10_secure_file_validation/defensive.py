import re
import os

def get_clean_filename(user_input):
    # Remove any path components
    filename = os.path.basename(user_input)

    # Keep only safe characters: alphanum, underscore, dash, period
    filename = re.sub(r'[^A-Za-z0-9_\-\.]', '', filename)

    # Allow only one dot (for the extension)
    if filename.count('.') > 1:
        parts = filename.split('.')
        filename = ''.join(parts[:-1]) + '.' + parts[-1]

    if filename != user_input:
        print(f"Warning: Unsafe filename detected. Cleaned to '{filename}'")

    return filename

if __name__ == "__main__":
    print("Running file!")

