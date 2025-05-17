# Import module for the qrcode package
import qrcode

def generate_qr_code(website_url, output_file="biox_qrcode.png"):
    """
    This function will create a QR code from a given website URL
    and save it as an image file.

    website_url: The URL to encode in the QR code.
    output_file: The filename for the saved QR code image.
    """

    # Creates a QRCode object with specific parameters
    qr_generator = qrcode.QRCode(
        version=2,  # Controls the size of the QR code (ranges from 1- 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Lowest error correction level
        box_size=10,  # Size of each box in pixels
        border=4  # Thickness of the border (minimum is 4)
    )

    # Adds the URL data to the QR code
    qr_generator.add_data(website_url)

    # Finalizes the QR code construction
    qr_generator.make(fit=True)

    # Generates an image from the QR code using black for code and white for background
    qr_image = qr_generator.make_image(fill_color="black", back_color="white")

    # Saves the image to a file
    qr_image.save(output_file)

    print(f"\n QR Code has been generated and saved as '{output_file}'.")

# Main block
if __name__ == "__main__":
    print("=== QR Code Generator - Biox Systems ===")
    # Prompts the user for a URL
    url_input = input("Enter the URL you want to generate a QR code of : ").strip()

    # Checks that the input is not empty
    if url_input:
        generate_qr_code(url_input)
    else:
        print("You must enter a valid URL.")
