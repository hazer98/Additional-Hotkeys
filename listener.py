import subprocess
import threading
import time
from typing import TypedDict

import keyboard


class ListenerData(TypedDict):
    key_sequence: str
    path: str


class Listener:
    def __init__(self, data: list[ListenerData]):
        super().__init__()

        self.data = data

        self.listening = True

    def update(self, data: list[ListenerData]):
        self.data = data

    def run(self):
        while True:
            self.listen()
            time.sleep(0.1)

    def start_listening(self):
        self.listening = True

    def stop_listening(self):
        self.listening = False

    def execute(self, path):
        subprocess.call([path])
        threading.Timer(0.1, self.start_listening).start()

    def listen(self):
        if self.listening:
            for e in self.data:
                if e['key_sequence'] and keyboard.is_pressed(e['key_sequence']):
                    self.stop_listening()
                    self.execute(e['path'])
