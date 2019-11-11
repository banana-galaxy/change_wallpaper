import ctypes, os, random
SPI_SETDESKWALLPAPER = 20
wallpapers = []
wallpaper = None
path = os.getcwd()

for filename in os.listdir(os.getcwd()):
    if not filename.endswith(".py"):
        wallpapers.append(filename)

wallpaper = random.choice(wallpapers)
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path+"\\"+wallpaper , 3)
