import subprocess
import threading
import time
from typing import TypedDict

import keyboard


class ListenerData(TypedDict):
    key_sequence: str
    path: str


class Listener:
    def __init__(self, data_store):
        super().__init__()

        self.data_store = data_store

        self.listening = True

    def run(self):
        while True:
            self.listen()
            time.sleep(0.05)

    def start_listening(self):
        self.listening = True

    def stop_listening(self):
        self.listening = False

    def execute(self, path):
        try:
            subprocess.call([path])
        except FileNotFoundError:
            print('ERROR: could not find: "%s"' % path)

        threading.Timer(0.01, self.start_listening).start()

    def listen(self):
        if self.listening:
            for e in self.data_store.get_listener_data():
                key_sequence = e['key_sequence']
                path = e['path']

                try:
                    keyboard.is_pressed(key_sequence)
                    valid = True
                except ValueError:
                    valid = False

                if valid and path and keyboard.is_pressed(key_sequence):
                    self.stop_listening()
                    self.execute(path)
