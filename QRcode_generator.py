import qrcode


def qrcode_generator(text):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
    

    qr.add_data('Some data')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg00001.png")

url = input("\nEnter your url: \n")

qrcode_generator(url)