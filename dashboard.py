import requests
import os
from PIL import Image
from datetime import datetime
class new:

    def datasharing(self):

        inp = input("Enter the url: ")

        response = requests.post("http://127.0.0.1:9000/qrgen",data={"data" : inp})

        print("wait some time qr is generating")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"

        with open(filename , "wb") as f:
            f.write(response.content)

        img = Image.open(filename)
        img.show()


n = new()

while True:

    ope = input("Want to create_qr oe exit: ")

    if ope =='create_qr':
        n.datasharing()
    if ope == 'exit':
        break