import os


def gen_files_path(start_dir="/", target_dir=None, file_type=None):
    for dirpath, dirnames, filenames in os.walk(start_dir):
        if target_dir is not None and target_dir not in dirpath:
            continue
        if file_type is not None:
            filenames = [name for name in filenames if file_type(name)]
        for filename in filenames:
            yield os.path.join(dirpath, filename)


for path in gen_files_path("C:/", "Module25"):
    print(path)


