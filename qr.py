import qrcode

def generate_qr(data):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 6,
        border = 0,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("tmp/qr.bmp")
