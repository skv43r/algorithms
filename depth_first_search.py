from os import listdir
from os.path import isfile, join
from collections import deque

def print_names(start_dir):
    search_quie = deque()
    search_quie.append(start_dir)
    while search_quie:
        dir = search_quie.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_quie.append(fullpath)


def depth_search(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            depth_search(fullpath)


print_names("files")
print()
depth_search("files")