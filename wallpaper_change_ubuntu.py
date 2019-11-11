import os, random

path = os.path.dirname(os.path.realpath(__file__))
wallpapers = []
wallpaper = None

for filename in os.listdir(path):
    if not filename.endswith(".py"):
        wallpapers.append(filename)

wallpaper = random.choice(wallpapers)

os.system("gsettings set org.gnome.desktop.background picture-uri file://"+path+"/"+wallpaper)
