import os
import sys

import PyInstaller.__main__


if __name__ == '__main__':
    PyInstaller.__main__.run([
        'app.py',
        '--onefile',
        '--windowed',
        '--noconsole',
        '--icon=icon.ico',
        '--name=Additional Hotkeys',
        '--add-data=styles;styles',
        '--add-data=assets;assets'
    ])
