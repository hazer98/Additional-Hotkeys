from listener import Listener

combinations = {
    'ctrl+alt+t': 'wt.exe',
}


def main():
    listener = Listener(combinations)
    listener.run()


if __name__ == '__main__':
    main()
