import os
import datetime
import shutil

def backup_files(source,destination):
    today = datetime.time.today()
    backup_file_name=os.path.join(destination,f"backup_<today>.tar.gz")
    #f".." is the formated tring literal
    shutil.make_archive(backup_file_name.replace()'.tar.gz',''),'gztar',source)
    source = "/backup_py"
    destination = "/backup_py/backup_OG"
    backup_files(source,destination)


#Script compatible with python3.6+
