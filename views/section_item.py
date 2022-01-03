from PyQt6.QtWidgets import QWidget, QHBoxLayout, QFrame

style = """
    background: #2B2B2B;
    padding: 16px;
    border-radius: 0px;    
    border-left: 1px solid;
    border-right: 1px solid;
    border-bottom: 1px solid;
    border-color: #1D1D1D;
"""


class SectionItem(QFrame):
    def __init__(self, widget):
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)
        #self.setStyleSheet(style)

        self.widget = widget

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.widget)

        self.setLayout(self.layout)

    def delete(self):
        print(self.widget)

    def get_widget(self):
        return self.widget
