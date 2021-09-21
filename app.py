import requests
import json
import qrcode
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


# Http Request
user_input = (input("Enter the crypto (ex: bitcoin) : \n"))

r = requests.get(f'http://api.coincap.io/v2/assets/{user_input}')
crypto = r.json()

link = crypto["data"]["explorer"]


# Generating QRcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(f"{link}")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

img.save("crypto.png")

print("QRcode generate in folder.")

# Graph with matplotlib
labels = ['p1']
crypto_b = 6929
crypto_e = 415

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, crypto_b, width, label='Bitcoin')
rects2 = ax.bar(x + width/2, crypto_e, width, label='Ethereum')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Crypto')
ax.set_title('Crypto Price')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()