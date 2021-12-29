import sys

from PyQt6.QtWidgets import QApplication

from listener import Listener
from ui.window import Window

combinations = {
    'ctrl+alt+t': 'wt.exe',
}


def main():
    # listener = Listener(combinations)
    # listener.run()
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
