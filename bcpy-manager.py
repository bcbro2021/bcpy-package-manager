import os, sys
import shutil
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

def cprint(color,text,tinput):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDCOLOR = '\033[0m'
    if tinput == False and color == "red":
        print(RED+text+ENDCOLOR)
    elif tinput == False and color == "yellow":
        print(YELLOW+text+ENDCOLOR)
    elif tinput == False and color == "green":
        print(GREEN+text+ENDCOLOR)
    elif tinput == False and color == "blue":
        print(BLUE+text+ENDCOLOR)

    if tinput == True and color == "red":
        input(RED+text+ENDCOLOR)
    elif tinput == True and color == "yellow":
        input(YELLOW+text+ENDCOLOR)
    elif tinput == True and color == "green":
        input(GREEN+text+ENDCOLOR)
    elif tinput == True and color == "blue":
        input(BLUE+text+ENDCOLOR)

def download_and_unzip(url, extract_to='.'):
    try:
        http_response = urlopen(url)
        zipfile = ZipFile(BytesIO(http_response.read()))
        zipfile.extractall(path=extract_to)
        zipfile.close()
    except Exception:
        cprint("red","You either seem to have no internet or the package is not found!",False)
        sys.exit()

#input
mode = sys.argv[1]
package = sys.argv[2]
save_dir = sys.argv[3]

#install function
if mode == "install":
    if package == "":
        cprint("red","Invalid package!",False)
        sys.exit()
    else:
        if save_dir != " ":
            if save_dir == "global":
                for i in os.listdir(os.path.expanduser("~/.local/lib/")):
                    if "python3" in i:
                        site_packages = os.path.join(os.path.expanduser("~/.local/lib/"),i,"site-packages")
                        if not os.path.exists(site_packages+"/"+package+".lib"):
                            download_and_unzip(f"https://bcbro2021.github.io/{package}.zip",site_packages)
                            cprint("green",f"Package, {package} successfully saved to {site_packages}",False)
                        else:
                            cprint("red",f"Package, {package} already exists in {site_packages}",False)
                    else:
                        cprint("red","Python is either not installed or is outdated!")
            else:
                download_and_unzip(f"https://bcbro2021.github.io/{package}.zip",save_dir)
                cprint("green",f"Package, {package} successfully saved to {save_dir}",False)
        else:
            download_and_unzip(f"https://bcbro2021.github.io/{package}.zip")
            cprint("green",f"Package, {package} successfully saved!",False)
#remove function
elif mode == "remove":
    if package == "":
        cprint("red","Package not found!",False)
        sys.exit()
    else:
        if save_dir != " ":
            if save_dir == "global":
                for i in os.listdir(os.path.expanduser("~/.local/lib/")):
                    if "python3" in i:
                        site_packages = os.path.join(os.path.expanduser("~/.local/lib/"),i,"site-packages")
                        if os.path.exists(site_packages+"/"+package+".lib"):
                            os.remove(site_packages+"/"+package+".lib")
                            shutil.rmtree(site_packages+"/"+package)
                            cprint("green",f"Package, {package} successfully removed from {site_packages}!",False)
                        else:
                            cprint("red","Package not found!",False)
                            sys.exit()
                    else:
                        cprint("red","Python is either not installed or is outdated!")
            else:
                if os.path.exists(save_dir+"/"+package+".lib"):
                    os.remove(save_dir+"/"+package+".lib")
                    shutil.rmtree(save_dir+"/"+package)
                    cprint("green",f"Package, {package} successfully removed from {save_dir}!",False)
                else:
                    cprint("red","Package not found!",False)
                    sys.exit()
        else:
            cprint("red","' ' is not a valid directory",False)
else:
    cprint("red",f"invalid function, {mode}!",False)
