from PyQt6.QtWidgets import QLayout, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QFrame, QApplication

from utils.utils import resource_path
from views.section_item import SectionItem


class SectionContainer(QWidget):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.expanded = True
        self.stylesheet = None

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.top_frame = QFrame()
        self.top_frame.setObjectName('top_frame')
        self.top_frame.mouseReleaseEvent = self.on_click
        self.top_frame.setContentsMargins(0, 0, 0, 0)

        self.top_container = QVBoxLayout()
        self.top_container.setSpacing(0)
        self.top_container.setContentsMargins(0, 0, 0, 0)

        self.top_frame.setLayout(self.top_container)
        self.layout.addWidget(self.top_frame)

        self.title = QLabel(title)
        self.top_container.addWidget(self.title)

        self.main_frame = QFrame()
        self.main_frame.setStyleSheet("""padding: 0""")

        self.main_container = QVBoxLayout()
        self.main_container.setSpacing(0)
        self.main_container.setContentsMargins(0, 0, 0, 0)

        self.main_frame.setLayout(self.main_container)
        self.layout.addWidget(self.main_frame)

        self.setLayout(self.layout)

        self.load_stylesheet()

        self.update()

    def load_stylesheet(self):
        with open(resource_path('styles/section_container.qss')) as f:
            self.stylesheet = f.read()

    def on_click(self, event):
        self.expanded = not self.expanded
        self.update()

    def update(self):
        if self.expanded:
            self.main_frame.show()
        else:
            self.main_frame.hide()

        self.top_frame.setProperty("expanded", self.expanded)

        # TODO find a better solution for updating the widget
        self.setStyleSheet(self.stylesheet)

    def set_title(self, title: str):
        self.title.setText(title)

    def add(self, item: SectionItem):
        self.main_container.addWidget(item)
        self.update()
