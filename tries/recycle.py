from datetime import datetime

ct = datetime.now()
print(type(ct))
print(ct)

ct_string = ct.strftime("%d-%b-%Y (%H:%M:%S.%f)")
print(type(ct_string))
print(ct_string)

dateObj = ct.date()
date = dateObj.strftime("%d-%b-%Y")
print(dateObj)
print(type(dateObj))
print(type(date))
print(date)

timeObj = ct.time()
time = timeObj.strftime("%H-%M-%S")
print(type(time))
print(time)

# ts = ct.timestamp()
# print(ts)

#
#
# from PIL import ImageGrab
# im = ImageGrab.grabclipboard()
# im.save('somefile.png','PNG')