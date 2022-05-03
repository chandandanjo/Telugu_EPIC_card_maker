# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Importing QR Code library
import pyqrcode

# Open an Image
print("Do you want Husband's name or your Father's name on your EPIC card ? ")
option = int(input("Enter 1 for Husband, 2 for Father : "))
while option != 1 and option != 2:
    print('Please enter valid input')
    option = int(input("Enter 1 for Husband, 2 for Father : "))
if option == 1:
    img = Image.open('hn.jpeg')
elif option == 2:
    img = Image.open('fn.jpeg')
sign_opt = int(input("Enter 1 if you want to change the EPIC sign or 2 if you want to keep the original one : "))
while sign_opt != 1 and sign_opt != 2:
    print('Please enter valid input')
    sign_opt = int(input("Enter 1 if you want to change the EPIC sign or 2 if you want to keep the original one : "))
try:
    img_photo = Image.open('image.jpg')
except:
    print('Please put the image.jpg in the required folder')
if sign_opt == 1:
    try:
        img_sign = Image.open('sign.jpg')
    except:
        print('Please put the sign.jpg in the required folder')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFontB = ImageFont.truetype('ARIALNB.TTF', 32)
myFontN = ImageFont.truetype('ARIALN.TTF', 32)
myFontT = ImageFont.truetype('telugu.ttf', 32, encoding='unic')


# Text adding functions
def text_add_bold(text, xcor, ycor):
    I1.text((xcor, ycor), f"{text}", font=myFontB, fill=(0, 0, 0))


def text_add_normal(text, xcor, ycor):
    I1.text((xcor, ycor), f"{text}", font=myFontN, fill=(0, 0, 0))


def text_add_telugu(text, xcor, ycor):
    I1.text((xcor, ycor), f"{text}", font=myFontT, fill=(0, 0, 0))


# Add Text to image

# Name
name = input('Enter your Name : ').strip()
name_telugu = input('Enter your Name (Telugu) : ').strip()
text_add_bold(f'{name}', 600, 588)
text_add_telugu(f'{name_telugu}', 590, 545)

# Husband's Name / Father's Name
if option == 1:
    family_name = input("Enter Husband's Name : ").strip()
    family_name_telugu = input("Enter Husband's Name (Telugu) : ").strip()
    text_add_bold(f'{family_name}', 750, 679.5)
    text_add_telugu(f'{family_name_telugu}', 610, 630)
    qr_opt = "Husband's"
elif option == 2:
    text_add_telugu('తండ్రి పేరు : ', 470, 630)
    family_name = input("Enter Father's Name : ").strip()
    family_name_telugu = input("Enter Father's Name (Telugu) : ").strip()
    text_add_bold(f'{family_name}', 710, 679.5)
    text_add_telugu(f'{family_name_telugu}', 650, 630)
    qr_opt = "Father's"

# EPIC No.
epic = input('Enter your EPIC No. : ').strip()
text_add_bold(f'{epic}', 170, 500)

# Address
# English
address_first = input('Enter address (First row, 65 characters only including space) : ').strip()
while len(address_first) > 66:
    address_first = input('Enter address (First row, 65 characters only including space) : ').strip()
text_add_normal(f'{address_first}', 1490, 562)
address_second = input('Enter address (Second row, 80 characters only including space) : ').strip()
while len(address_second) > 81:
    address_second = input('Enter address (Second row, 80 characters only including space) : ').strip()
text_add_normal(f'{address_second}', 1335, 610)
# Telugu
address_first_telugu = input('Enter address in Telugu (First row, 55 characters only including space) : ')
while len(address_first_telugu) > 56:
    address_first_telugu = input('Enter address in Telugu (First row, 55 characters only including space) : ')
text_add_telugu(f'{address_first_telugu}', 1500, 463)
address_second_telugu = input('Enter address in Telugu (Second row, 65 characters only including space) : ')
while len(address_second_telugu) > 66:
    address_second_telugu = input('Enter address in Telugu (Second row, 65 characters only including space) : ')
text_add_telugu(f'{address_second_telugu}', 1335, 510)

# Gender
gen_opt = int(input('Enter 1 for male or 2 for female : '))
while gen_opt != 1 and gen_opt != 2:
    print('Please enter valid input')
    gen_opt = input('Enter 1 for Male or 2 for Female : ')
if gen_opt == 1:
    text_add_telugu('పు / Male', 1615, 363)
elif gen_opt == 2:
    text_add_telugu('స్త్రీ / Female', 1615, 363)

# DOB
dob = input('Enter your date of birth (DD-MM-YYYY) : ').strip()
text_add_normal(f'{dob}', 1810, 412)

# ERO
ero = input('Enter ERO : ').strip()
text_add_normal(f'{ero}', 1550, 859)
ero_telugu = input('Enter ERO (Telugu) : ').strip()
text_add_telugu(f'{ero_telugu}', 1580, 816)

# Download Date
download_date = input('Enter download date (DD-MM-YYYY) : ').strip()
text_add_normal(f'{download_date}', 1710, 898)

# Resize images
new_img = img_photo.resize((294, 370))
if sign_opt == 1:
    new_sign = img_sign.resize((335, 90))

# Image Paste
Image.Image.paste(img, new_img, (154, 540))
if sign_opt == 1:
    Image.Image.paste(img, new_sign, (1492, 720))

# QR Code
qr_info = f"""EPIC: {epic}
Name: {name}
{qr_opt} Name: {family_name}
Date of Birth: {dob}"""

url = pyqrcode.create(qr_info)
url.png('myqr.png', scale=6)
qr = Image.open('myqr.png').resize((292, 292))
Image.Image.paste(img, qr, (2020, 684))

# Display edited image
img.show()

# Save the edited image
img.save("EPIC.jpg")
