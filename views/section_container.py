from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QFrame

import cvars
from utils.utils import resource_path
from views.section_item import SectionItem
from widgets.hotkey_widget import HotkeyWidget


class SectionContainer(QFrame):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setObjectName('section_container')

        self.expanded = True
        self.stylesheet = None
        self.title = title
        self.items = []

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.top_frame = QFrame()
        self.top_frame.setObjectName('top_frame')
        self.top_frame.mouseReleaseEvent = self.on_click
        self.top_frame.setContentsMargins(0, 0, 0, 0)

        self.top_container = QHBoxLayout()
        self.top_container.setSpacing(0)
        self.top_container.setContentsMargins(0, 0, 0, 0)

        self.top_frame.setLayout(self.top_container)
        self.layout.addWidget(self.top_frame)

        self.title_label = QLabel(self.title)
        self.top_container.addWidget(self.title_label)

        self.indicator_icon = QLabel()
        self.indicator_icon.setMaximumWidth(16)
        self.top_container.addWidget(self.indicator_icon)

        self.item_frame = QFrame()
        self.item_container = QVBoxLayout()
        self.item_container.setSpacing(0)
        self.item_container.setContentsMargins(0, 0, 0, 0)

        self.item_frame.setLayout(self.item_container)
        self.layout.addWidget(self.item_frame)

        self.setLayout(self.layout)

        self.load_stylesheet()

        self.update()

    def load_stylesheet(self):
        with open(resource_path('styles/section_container.qss')) as f:
            self.stylesheet = f.read()

    def on_click(self, event):
        if len(self.items) > 0:
            self.expanded = not self.expanded
            self.update()

    def update(self):
        if self.expanded:
            self.item_frame.show()
        else:
            self.item_frame.hide()

        self.top_frame.setProperty("expanded", self.expanded)

        self.indicator_icon.setPixmap(
            QPixmap(resource_path(cvars.COLLAPSE_ICON) if self.expanded else resource_path(
                cvars.EXPAND_ICON)).scaledToWidth(12))

        self.title_label.setText(self.title + ' ' + f'({len(self.items)})')

        # TODO find a better solution for updating the widget style
        self.setStyleSheet(self.stylesheet)

    def set_title(self, title: str):
        self.title_label.setText(title)

    def remove_widget(self, widget):
        for i, item in enumerate(self.items):
            section_item = item["section_item"]
            widget_item = item["widget"]
            if widget_item == widget:
                self.item_container.removeWidget(section_item)
                section_item.deleteLater()
                widget_item.deleteLater()
                self.items.remove(item)

        self.update()

    def add_widget(self, widget):
        section_item = SectionItem(widget)
        self.item_container.addWidget(section_item)
        self.items.append({
            "section_item": section_item,
            "widget": widget
        })
        self.update()
