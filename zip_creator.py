import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed1.zip")
    with zipfile.ZipExtFile(dest_path, 'w') as archive:
        #filepath = pathlib.Path(filepath)
        for filepath in filepaths:
            archive.write(filepath) #, archive=filepaths)


if __name__ == "__main__":
    make_archive(filepaths=["test1.txt", "test2.txt"], dest_dir="test")