import os
import os.path

path = "c:\\"
fileNames = []
for top, dirs, files in os.walk(path):
    for nm in files:
        fileNames.append(os.path.join(top, nm))
    break

onlyFiles =  filter(lambda x: os.path.isfile(x), fileNames)
print(files)

sizes = map(lambda x: os.path.getsize(x), onlyFiles)
print (sizes)

print (reduce(lambda x, y: x+ y, sizes))


