import qrcode
import os

def generate_qr(data):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 2,
        border = 0,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()

    qr_path = os.path.join(os.path.dirname(__file__), 'tmp/qr.bmp')
    img.save(qr_path)
