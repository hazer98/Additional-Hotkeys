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
                if e['key_sequence'] and keyboard.is_pressed(e['key_sequence']):
                    self.stop_listening()
                    self.execute(e['path'])
