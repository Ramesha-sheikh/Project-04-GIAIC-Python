import qrcode  # QR Code banane ke liye library import kar rahe hain
import cv2     # QR Code ko scan aur decode karne ke liye library import kar rahe hain

# Function to create a QR Code - Yeh function QR Code generate karega
def create_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,  # QR Code ka version set kar rahe hain
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level, zyada achi quality ke liye
        box_size=10,  # Har box ka size kitna hoga
        border=4  # Border ka size set kar rahe hain
    )
    qr.add_data(data)  # Data ko QR Code mein daal rahe hain
    qr.make(fit=True)  # Data ke size ke mutabiq QR Code adjust ho raha hai

    # QR Code ka image bana kar save kar rahe hain
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)  # QR Code ko specified filename ke sath save kar rahe hain
    print(f"QR Code saved as {filename}")  # Confirmation message display kar rahe hain


# Function to decode a QR Code - Yeh function QR Code ko read aur decode karega
def decode_qr_code(filename):
    img = cv2.imread(filename)  # QR Code image ko read kar rahe hain
    detector = cv2.QRCodeDetector()  # QR Code detect karne ke liye object bana rahe hain
    data, bbox, _ = detector.detectAndDecode(img)  # QR Code ko detect aur decode kar rahe hain

    # Agar data milta hai tou print karte hain, warna error message dete hain
    if data:
        print("Decoded data:", data)  # Decode hua data display kar rahe hain
    else:
        print("No QR Code found or could not decode.")  # Error message agar QR Code nahi milta


# Main program - User se option lena aur uske mutabiq kaam karna
if __name__ == "__main__":
    while True:
        # User se option select karne ka keh rahe hain
        choice = input("\nSelect an option:\n1. Generate QR Code\n2. Decode QR Code\n3. Exit\nEnter choice (1/2/3): ")

        # QR Code generate karne ka option
        if choice == '1':
            data = input("Enter the data to encode: ")  # QR Code mein jo data dalna hai
            filename = input("Enter filename to save (example: mycode.png): ")  # File ka naam
            create_qr_code(data, filename)  # QR Code generate kar rahe hain

        # QR Code decode karne ka option
        elif choice == '2':
            filename = input("Enter QR Code image filename to decode: ")  # File ka naam jahan QR Code hai
            decode_qr_code(filename)  # QR Code ko read aur decode kar rahe hain

        # Program ko exit karne ka option
        elif choice == '3':
            print("Exiting program.")  # Exit message
            break  # Loop ko terminate kar rahe hain

        else:
            print("Invalid input. Please choose 1, 2, or 3.")  # Invalid input ka error message
