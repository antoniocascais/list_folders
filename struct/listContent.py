import os


def update_parent(starting_dir, files_by_folder, file, num_files):
    n = 0
    parent = os.path.dirname(file)

    if starting_dir is file:
        return files_by_folder

    if parent in files_by_folder:
        n = files_by_folder[parent]
    files_by_folder[parent] = n + num_files

    return update_parent(starting_dir, files_by_folder, parent, num_files)


def main():
    files_by_folder = dict()
    starting_dir = u"."
    for root, dirs, files in os.walk(starting_dir, topdown=False):
        n_files = len(files)
        files_by_folder = update_parent(starting_dir, files_by_folder, root, n_files)
        if root in files_by_folder:
            n = files_by_folder[root]
        else:
            n = n_files
        print(root, "contains", n, "files")
    return


main()
