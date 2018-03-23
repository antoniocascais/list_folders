import os


def contains_subfolders(file):
    if not os.path.isdir(file):
        return False
    path = os.path.realpath(file)
    for f in os.listdir(file):
        sub_file = path + "/" + f
        if os.path.isdir(sub_file):
            return True
    return False


def process_file(visited_files, file):
    print("file",file)
    files = os.listdir(file)
    for f in files:
        path = os.path.realpath(f)
        print("path",path)
        file_with_path = path + "/" + f
        print("file with opath", file_with_path)
        if file_with_path not in visited_files:
            visited_files.append(file_with_path)
            if contains_subfolders(file_with_path):
                process_file(visited_files, file_with_path)
            else:
                print(file_with_path, " contains ", str(len(files)), " files.")
                parent_dir = os.path.dirname(file_with_path)
                process_file(visited_files, parent_dir)
        else:
            path = os.path.realpath(file_with_path)
            print("path", path)
            print("not visited", file_with_path)

            file_with_path = os.path.realpath(file_with_path)
            process_file(visited_files, file_with_path)


def main():
    visited_files = []
    process_file(visited_files, os.curdir)
    return


main()
