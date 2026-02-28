#!/usr/bin/env python3
import qrcode
import base64

# Instagram QR
ig_qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
ig_qr.add_data('https://instagram.com/ashfield_mobile_repair')
ig_qr.make(fit=True)
ig_img = ig_qr.make_image(fill_color='black', back_color='white')
ig_img.save('instagram_qr.png')

# TikTok QR
tt_qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
tt_qr.add_data('https://www.tiktok.com/@ashfield_mobile_repair')
tt_qr.make(fit=True)
tt_img = tt_qr.make_image(fill_color='black', back_color='white')
tt_img.save('tiktok_qr.png')

# Convert to base64
for filename in ['instagram_qr.png', 'tiktok_qr.png']:
    with open(filename, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    with open(f'{filename[:-4]}_base64.txt', 'w') as f:
        f.write(f'data:image/png;base64,{b64}')

print('✓ QR codes created and converted')
