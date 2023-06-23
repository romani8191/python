import os


source="C:\\Users\\Lenovo\\Desktop\\rel"
destination="C:\\Users\\Lenovo\\Desktop\\art"


from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(destination):
    f.extend(filenames)
    continue
print(f)
