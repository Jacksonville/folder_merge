
import os
from time import ctime, strftime, strptime
import shutil
import argparse
try:
    import pyexiv2
except ImportError:
    print ('Unable to import pyexiv2. Please download from http://tilloy.net/dev/pyexiv2/download.html')

class FileCopy:
    def check_dir(self, path):
        return os.path.isdir(path)

    def new_filename(self, filepath, destfilepath, num=0):
        metadata = pyexiv2.ImageMetadata(filepath)
        metadata.read()
        filetime = metadata.get('Exif.Image.DateTime')
        filename = strftime("%Y%m%d_%H%M%S",
                            strptime(filetime,
                                     "%a %b %d %H:%M:%S %Y")) + '_' \
                                     + str(num) + os.path.splitext(filepath)[1]
        if os.path.exists(os.path.join(destfilepath, filename)):
            num += 1
            filename = self.new_filename(filepath, destfilepath, num)
        return os.path.join(destfilepath, filename)

    def copy_file(self, filepath, destfilepath):
        dest_path = self.new_filename(filepath, destfilepath)
        shutil.copy2(filepath, dest_path)


def process_directory(source_dir, dest_dir):
    file_copy = FileCopy()
    if file_copy.check_dir(source_dir) and file_copy.check_dir(dest_dir):
        for file in os.listdir(source_dir):
            if os.path.isdir(os.path.join(source_dir, file)):
                print (('Processing %s in %s' % (file, source_dir)))
                file_copy.copy_file(os.path.join(source_dir, file), dest_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""A simple process to copy and rename files based on date modified.
    For example a file named DCS_2342.jpg with a date modified of 2013-04-05 16:54:32 would be renamed to 20130405_165432_0.jpg.
    If a file of the same name already exists in the specified destination then the name would be 20130405_165432_1.jpg,
    the last number incrimented until there is no conflict""",
                                     epilog="""Good luck :)""")
    parser.add_argument('source_path', help="Source path for copy")
    parser.add_argument('dest_path', help="Destination path for copy")
    args = vars(parser.parse_args())
    source_path = args['source_path']
    dest_path = args['dest_path']
    process_directory(source_path, dest_path)
