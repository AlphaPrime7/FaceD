import PIL
from PIL import Image 
import numpy as np
import cv2 as cv
import io

def convert_pil_arr(pil_obj: PIL.Image) -> np.array:
    img_arr = np.array(pil_obj)
    return img_arr

def convert_pil_byte(pil_obj: PIL.Image) -> bytes:
    bytes_obj = pil_obj.tobytes()
    return bytes(bytes_obj)

def convert_pil_bytearr(pil_obj, image_format) -> bytearray:
    img_byte = io.BytesIO()
    pil_obj.save(img_byte, format=image_format, subsampling=0, quality=100)
    img_byte = img_byte.getvalue()
    img_barr = bytearray(img_byte)
    return img_barr

def convert_arr_pil(cv_obj) -> PIL.Image:
    pil_image = Image.fromarray(cv_obj)
    return pil_image
    
def convert_arr_byte(cv_obj: np.array, img_format) -> bytes:
    cv_obj = cv.cvtColor(cv_obj, cv.COLOR_BGR2RGB)
    success, encoded_image = cv.imencode(img_format, cv_obj) 
    content_bytes = encoded_image.tobytes()
    return content_bytes

def convert_arr_bytearr(cv_obj: np.array, img_format) -> bytearray:
    cv_obj = cv.cvtColor(cv_obj, cv.COLOR_BGR2RGB)
    success, encoded_image = cv.imencode(img_format, cv_obj) 
    content_bytes = encoded_image.tobytes()
    barr = bytearray(content_bytes)
    return barr
