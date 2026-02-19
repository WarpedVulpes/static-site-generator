import os
import shutil

def copy_static_files(source_dir, dest_dir):

    shutil.rmtree(dest_dir, ignore_errors=True)

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            dest_item = os.path.join(dest_dir, item)

            if os.path.isfile(source_item):
                shutil.copy(source_item, dest_item)
            else:
                copy_static_files(source_item, dest_item)