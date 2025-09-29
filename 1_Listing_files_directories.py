import os

# Set the path you want to list; here, current directory is default
path = "/Users/akhilanto/Desktop/pem"

# Get the list of all files and directories in the specified path
contents = os.listdir(path)

print(f"Contents of the directory '{os.path.abspath(path)}':\n")

for item in contents:
    # Check if item is a file or directory
    full_path = os.path.join(path, item)
    if os.path.isdir(full_path):
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")
