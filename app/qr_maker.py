from io import BytesIO
import qrcode
from fastapi import FastAPI,Form
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origin = ["http://localhost:63342"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/qrgen')

def qrgene(data: str = Form(...)):

    qr = qrcode.QRCode(

        version = 1 ,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4

    )

    qr.add_data(data)
    qr.make(fit = True)

    img = qr.make_image(fill_color = 'black' , back_color = 'white')

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")




