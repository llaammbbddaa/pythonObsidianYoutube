import os
import yt_dlp

dirList = os.listdir("/home/arshilegorky/Documents/Obeta/internet/youtube/")
# print(dirList)

links = []
for i in dirList:
    currentName = i
    file = open(("/home/arshilegorky/Documents/Obeta/internet/youtube/" + currentName), "r")
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
titlesS = []
titles = []
for i in links:
    if ("youtu"  in i and "\n" not in i):
        ugh.append(i)
        titlesS.append(dirList[links.index(i)])
print(ugh)
#print(titlesS)
for i in titlesS:
    titles.append(i.removesuffix(".md"))
print(titles)

# Where to save
SAVE_PATH = "/home/arshilegorky/Videos/youtubeObeta"

videoNamesS = os.listdir(SAVE_PATH)
videoNames = []
t = []
u = []
for i in videoNamesS:
    videoNames.append(i.removesuffix(".mp4"))
for i in range(len(titles)):
    if (titles[i] not in videoNames):
        t.append(titles[i])
        u.append(ugh[i])
        print("in")

for i in range(len(u)):
    opts = {"outtmpl": f"{SAVE_PATH}/{t[i]}.mp4", "format": "best", }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(u[i])
    except Exception as e:
        print(f"Error: {e}")

print("process complete :O")
