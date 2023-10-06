## How to make a py program to exe using pyinstaller

- the onefile flag will make the exe file into one file
- the add-data flag will add all the images in the images folder to the exe file
- the w flag will make the exe file run in the background and not show the terminal

- create a resource path in the py file to get the image file that is stored in the Meipass folder
```python
# ---------------------------- PATH ------------------------------- #
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
```

```bash
pyinstaller --onefile -w --add-data "images/*.png;." main.py

# after running that command you will get a dist folder and a build folder
# the exe file will be in the dist folder
```