import os, random

path = os.path.dirname(os.path.realpath(__file__))
image_types = ['.jpg', '.jpeg', '.png', '.gif', '.jfif']
wallpapers = []
wallpaper = None

for filename in os.listdir(path):
    for image_type in image_types:
        if filename.endswith(image_type):
            wallpapers.append(filename)

wallpaper = random.choice(wallpapers)

os.system("gsettings set org.gnome.desktop.background picture-uri file://"+path+"/"+wallpaper)
