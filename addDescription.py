import json
import yt_dlp
import os
import re

path = "/home/arshilegorky/Documents/Obeta/internet/youtube/"
dirList = os.listdir(path)
links = []
for i in dirList:
    currentName = i
    file = open((path + currentName), "r")
    content = file.read()
    link = ""
    if ("(" in content):
        for j in content:
            if (j == "("):
                link = link + j
            elif (j == ")"):
                break
    else:
        link = content
    links.append(link)
    file.close()

ugh = []
titles = []
for i in links:
    if ("youtu"  in i and "\n" not in i):
        ugh.append(i)
        titles.append(dirList[links.index(i)])
print(ugh)
print(titles)

for i in range(len(titles)):
    name = (path + titles[i])
    file = open(name, "a")

    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(ugh[i], download=False)
        dump = json.dumps(ydl.sanitize_info(info))
        desc = dump[dump.index("description") + 15:dump.index("channel_id") - 4]

        # clean up
        desc = desc.encode("utf-8", errors="ignore").decode("utf-8")
        desc = re.sub(r'[\uDC80-\uDCFF]', '', desc)
        desc = re.sub(r'\s+', ' ', desc).strip()

    print("\n\ndesc >> " + str(desc))
    print("\n" + str(titles[i]) + " >> " + str(ugh[i]))
    file.write(str(desc))


    #file.write(desc)
    file.close()
