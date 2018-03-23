import os


def update_parent(files_by_folder, file, num_files):
    n = 0
    parent = os.path.dirname(file)
    if parent in files_by_folder:
        n = files_by_folder[parent]
    files_by_folder[parent] = n + num_files
    return


def main():
    files_by_folder = dict()
    for root, dirs, files in os.walk(u".", topdown=False):
        n_files = len(files)
        update_parent(files_by_folder, root, n_files)
        if root in files_by_folder:
            print(root, "contains", files_by_folder[root], "files")
        else:
            print(root, "contains", n_files, "files")
    return


main()
