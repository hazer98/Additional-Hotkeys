from PyQt6.QtWidgets import QLayout, QWidget, QHBoxLayout, QLabel

style = """
    background: #2D2D2D;
    padding: 24px 16px;
    border: 1px solid #1D1D1D;
"""


class SectionContainer(QWidget):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout = QHBoxLayout()

        self.title = QLabel(title)
        self.layout.addWidget(self.title)

        self.setLayout(self.layout)

        self.setStyleSheet(style)

    def set_title(self, title: str):
        self.title.setText(title)

    def add_widget(self, widget):
        self.layout.addWidget(widget)
