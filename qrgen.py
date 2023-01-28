# Simple QRcode Generator Using Python 
#Coded by CyberDome.........

import qrcode
from PIL import Image
from termcolor import colored

# Define the text to display as the heading
heading_text = "QRcode Generator By CyberDome"
mid_text = "SUBSCRIBE OUR YOUTUBE CHANNEL FOR LATEST TECH HACKS :https://www.youtube.com/@CyberDomeYT "
sub_text = "Don't Forget To SUBSCRIBE OUR YT CHANNEL : https://www.youtube.com/@CyberDomeYT "
success_text = "Your Image IsSuccessfully Saved In The <QRcode generator> directory to see it Type command $ls and see the saved png file"
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



userdata=input("Enter Your Url To Generate QRcode : ")
image_name=input("Enter A Name To Save The QRcode with <.png> [example=yourimagename.png] : ")
qr.add_data(userdata)
qr.make(fit=True)
img=qr.make_image(fill_color="black", back_color="white")
img.show()
print(colored(success_text,"green",attrs=['bold']))
print(colored(sub_text,"red",attrs=['bold']))
img.save(image_name)
