import PyInstaller.__main__

if __name__ == '__main__':
    PyInstaller.__main__.run([
        'app.py',
        '--onefile',
        '--windowed',
        '--icon=icon.ico',
        '--name=Additional Hotkeys'
    ])
