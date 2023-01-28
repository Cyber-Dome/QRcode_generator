# Simple QRcode Generator Using Python 
#Coded by CyberDome.........

import qrcode
from PIL import Image
from termcolor import colored

# Define the text to display as the heading
heading_text = "QRcode Generator By CyberDome"
mid_text = "SUBSCRIBE OUR YOUTUBE CHANNEL FOR LATEST TECH HACKS :https://www.youtube.com/@CyberDomeYT "
logo = """

░█████╗░██╗░░░██╗██████╗░███████╗██████╗░██████╗░░█████╗░███╗░░░███╗███████╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝
██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝██║░░██║██║░░██║██╔████╔██║█████╗░░
██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║██╔══╝░░
╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║██████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

"""
# Use the colored function to display the heading in a specific color
print(colored(heading_text, 'red', attrs=['bold']))
print(colored(mid_text,'green', attrs=['bold']))
print(logo)
qr=qrcode.QRCode(version=1,
error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)



userdata=input("Enter Your Url To Generate QRcode ")
image_name=input("Enter A Name To Save The QRcode with <.png> [example=yourimagename.png]")
qr.add_data(userdata)
qr.make(fit=True)
img=qr.make_image(fill_color="black", back_color="white")

img.save(image_name)
