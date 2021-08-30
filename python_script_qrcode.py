# full video on the topic:
# https://youtu.be/48o-mjgdMsE

#pip install pyqrcode
import pyqrcode # import the required module
img=pyqrcode.create("https://youtu.be/YSNuGEzo2HA") # put the link here
img.png("qrcode.png",scale=10) # If you want to save the file as png
img.show() # if you want to see the qr code once


# if you want to see how you can make a desktop app with python that converts passwords,links,etc to QR code,
# check out this video :  https://youtu.be/YSNuGEzo2HA