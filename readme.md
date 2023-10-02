# Telugu EPIC Card Image Generator

This Python script allows you to generate an EPIC (Electors' Photo Identity Card) card image with custom details. You can choose to include your name, your father's or husband's name, EPIC number, address, gender, date of birth, and other information on the card.

## Prerequisites

Before running the script, you need to have the following:

1. Python installed on your system.
2. The following Python libraries installed:
   - PIL (Python Imaging Library) for image manipulation.
   - pyqrcode for generating QR codes.

You can install these libraries using pip:

```bash
pip install pillow pyqrcode
```

## Usage

1. Clone this repository to your local machine or download the script.
2. Make sure you have the required libraries installed.
3. Run the script using the following command:

```bash
python epic_card_generator.py
```

4. Follow the on-screen prompts to customize the EPIC card with your details.
5. The edited EPIC card image will be displayed and saved as "EPIC.jpg" in the same directory as the script.

## Customization Options

- You can choose to have either your husband's or father's name on the EPIC card by selecting the appropriate option.
- You can choose to keep the original EPIC sign or replace it with a custom sign.
- Enter your name and name in Telugu (if applicable).
- Enter your EPIC number.
- Enter your address in English and Telugu.
- Specify your gender (male or female).
- Enter your date of birth in DD-MM-YYYY format.
- Enter the ERO (Electoral Registration Officer) details.
- Enter the download date in DD-MM-YYYY format.

## Note

- The script uses the PIL library to manipulate images and add text.
- You can customize the fonts and positions of text as needed.
- The script generates a QR code containing EPIC details and adds it to the card.
- The final edited EPIC card image is displayed and saved as "EPIC.jpg" in the script's directory.

Please ensure that you have the necessary rights and permissions to generate an EPIC card with this script and use it responsibly.
