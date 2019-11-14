import ctypes, os, random
SPI_SETDESKWALLPAPER = 20
image_types = ['.jpg', '.jpeg', '.png', '.gif', '.jfif']
wallpapers = []
wallpaper = None
path = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(os.getcwd()):
    for image_type in image_types:
        if filename.endswith(image_type):
            wallpapers.append(filename)

wallpaper = random.choice(wallpapers)
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path+"\\"+wallpaper , 3)
