# QR Code Generator - README

## Required Libraries
Is project mein teen libraries ka use hua hai:

1. **qrcode** - QR Code generate karne ke liye.
   - Yeh library QR Code banane aur save karne ke liye use hoti hai.
   - Yeh library humein QR Codes banane mein madad deti hai. Iska version aur error correction set kar ke hum apne desired QR Code create karte hain.

2. **cv2 (OpenCV)** - QR Code ko scan aur decode karne ke liye.
   - QR Code detect aur decode karne ke liye iska QRCodeDetector function use hota hai.
   - Iska use QR Code ko read aur decode karne ke liye hota hai. Hum OpenCV ka QRCodeDetector function use karte hain.

3. **PIL (Python Imaging Library)** - Image processing aur manipulation ke liye.
   - Yeh library QR Code image ko handle karne mein madad deti hai. Iska use QR Code image ko save karne ke liye hota hai.

---

## Step-by-Step Guide

1. **Libraries ko Import karna:**
   - `import qrcode` - QR Code banane ke liye.
   - `import cv2` - QR Code ko scan aur decode karne ke liye.
   - `from PIL import Image` - Image handling aur save karne ke liye.

2. **QR Code Generate karna:**
   - Function: `create_qr_code(data, filename)`
   - Data ko QR Code mein encode karte hain aur image ko save karte hain.
   - Isme hum version, error correction, box size, aur border set karte hain.

3. **QR Code ko Decode karna:**
   - Function: `decode_qr_code(filename)`
   - File ko read karte hain aur QR Code ko decode karte hain.
   - Agar QR Code sahi detect ho jaye, toh data display hota hai, warna error message show hota hai.

4. **User Input:**
   - Program run karne par user ko 3 options diye jate hain:
     - QR Code generate karna.
     - QR Code decode karna.
     - Program se exit karna.

---

## How to Run
- Python install hona zaroori hai. Agar nahi hai, toh [Python ki official website](https://www.python.org/downloads/) se download karen.
- Command Prompt (CMD) open karen aur command run karen:
  ```bash
  pip install qrcode opencv-python pillow
  ```
- Code ko run karne ke liye `python filename.py` likhen.

Agar koi problem ho ya samajh na aaye, toh zaroor batayein! 😊

