from django.http import HttpResponse
from django.shortcuts import render
from barcode.models import *
import qrcode
from io import BytesIO
from PIL import Image

# Create your views here.

def bkqrcode(request):
    if request.GET.get('data') is not None:
        # The data that you want to store
        data = request.GET.get('data')
    else:
        data = "The Data that you need to store in the QR Code"

    if request.GET.get('size') is not None:
        # The data that you want to store
        size = request.GET.get('size')
    else:
        size = 10

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = size,
        border = 1,
    )

    
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image from the QR Code instance
    img = qr.make_image()
    buffer = BytesIO()
    img.save(buffer)

    #return buffer.getbuffer()
    response = HttpResponse(buffer.getbuffer())
    response['Content-Type'] = "image/png"
    response['Cache-Control'] = "max-age=0"
    return response
    #return HttpResponse(img, content_type="image/jpeg")
        

def index(request):

    return HttpResponse("Hello, barcode is here!!!.")