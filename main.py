import os

folder = "C:\\Users\\noahm\Music\\yt playlist\\"
os.chdir(folder)
files = os.listdir(folder)
files.sort(key=lambda x: os.path.getctime(x))

# count is the number after most recent
count = 1

for i in range(count - 1, (len(files))):

    source = folder + files[i]
    destination = folder + str(count) + " " + files[i]
    print("DESTINATION:" + destination)

    os.rename(source, destination)
    count += 1


# dont worry about this
# 9, 99, 226 length values

#for i in range(95, len(files)):

#    source = folder + files[i]
#    destination = folder + files[i][1:]
#    print("DESTINATION:" + destination)

#    os.rename(source, destination)
