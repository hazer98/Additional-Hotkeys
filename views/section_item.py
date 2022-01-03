from PyQt6.QtWidgets import QWidget, QLayout, QHBoxLayout

style = """
    background: #2D2D2D;
    padding: 16px;
    border-radius: 0px;    
    border: 1px solid #1D1D1D;
"""


class SectionItem(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.layout)
        self.setStyleSheet(style)

    def set_widget(self, widget):
        self.layout.addWidget(widget)
