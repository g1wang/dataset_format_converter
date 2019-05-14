import os
def getPath(src_dir_path, lines):
    for fpathe, dirs, fs in os.walk(src_dir_path):
        for f in fs:
            childPath = os.path.join(fpathe, f)
            if os.path.isdir(childPath):
                print(childPath)
            else:
                print(childPath)
                line = childPath + '\n'
                lines.append(line)


lines = []
getPath('../JPEGImages', lines)
file = open('../train.txt', 'w+')
print('len', str(len(lines)))
file.writelines(lines)