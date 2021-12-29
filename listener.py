import keyboard
import subprocess
import threading
import time


# This class listens to key inputs from the user and executes executables based on specified combinations
# Instance of this class is executed on a separate thread
class Listener(threading.Thread):
    def __init__(self, combinations):
        super(Listener, self).__init__()

        self.combinations = combinations

        self.daemon = True
        self.cancelled = False
        self.listening = True

    def run(self):
        while not self.cancelled:
            self.listen()
            time.sleep(0.1)

    def cancel(self):
        self.cancelled = True

    def start_listening(self):
        self.listening = True

    def stop_listening(self):
        self.listening = False

    def execute(self, path):
        subprocess.call([path])
        threading.Timer(0.1, self.start_listening).start()

    def listen(self):
        if self.listening:
            for key, path in self.combinations.items():
                if keyboard.is_pressed(key):
                    self.stop_listening()
                    self.execute(path)
