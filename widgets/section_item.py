from PyQt6.QtWidgets import QWidget, QHBoxLayout, QFrame

from utils.utils import resource_path


class SectionItem(QFrame):
    def __init__(self, widget):
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName("section_item")

        self.widget = widget

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.widget)

        self.setLayout(self.layout)

        self.load_stylesheet()

    def load_stylesheet(self):
        with open(resource_path('styles/section_item.qss')) as f:
            self.setStyleSheet(f.read())

    def delete(self):
        print(self.widget)

    def get_widget(self):
        return self.widget
