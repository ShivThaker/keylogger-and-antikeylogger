from pynput import keyboard


class MyExceptiom(Exception): pass

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

"""
    keyboard listener is a threading.Thread
    TO STOP THE LISTENER -> pynput.keyboard.Listener.stop from anywhere, raise StopException or return False
    
    When using the non-blocking version above, the current thread will continue executing. This might be necessary 
    when integrating with other GUI frameworks that incorporate a main-loop, but when run from a script, 
    this will cause the program to terminate immediately.
"""

"""
    If a callback handler raises an exception, the listener will be stopped. Since callbacks run in a dedicated 
    thread, the exceptions will not automatically be reraised. To be notified about callback errors, call Thread.join on 
    the listener instance
    
    from pynput import keyboard

    class MyException(Exception): pass
    
    def on_press(key):
        if key == keyboard.Key.esc:
            raise MyException(key)
    
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press) as listener:
        try:
            listener.join()
        except MyException as e:
            print('{0} was pressed'.format(e.args[0]))
    -> will simply raise an exception when Key.esc is pressed
"""