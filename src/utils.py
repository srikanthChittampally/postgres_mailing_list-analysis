import os


def all_mbox_files(mbox_folder):
    mbox_files = []
    for year_folder in os.listdir(mbox_folder):
        year_path = os.path.join(mbox_folder, year_folder)
        if os.path.isdir(year_path):
            mbox_files.extend(
                os.path.join(year_path, f) 
                for f in os.listdir(year_path)
            )
            
    return mbox_files