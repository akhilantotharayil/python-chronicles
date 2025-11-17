import os
import datetime
import shutil

def backup_files(source, destination):
    # Today's date YYYYMMDD
    today = datetime.date.today().strftime("%Y%m%d")

    # File name (without extension)
    backup_file_name = os.path.join(destination, f"backup_{today}")

    # Create the backup (adds .tar.gz automatically)
    shutil.make_archive(backup_file_name, 'gztar', source)

    print(f"Backup created: {backup_file_name}.tar.gz")


# Run backup
source = "/backup_py"
destination = "/backup_py/backup_OG"

backup_files(source, destination)
