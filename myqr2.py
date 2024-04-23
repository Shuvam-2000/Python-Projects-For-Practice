import qrcode
from PIL import Image

# making the qrcode and the error_correction
qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border=4,)

# adding data to the qr code
qr.add_data("www.stackoverflow.com")
qr.make(fit=True)

# making of the qrcode image
img = qr.make_image(fill_color="black", back_color="white")
img.save("stackoverflow_web.png")
