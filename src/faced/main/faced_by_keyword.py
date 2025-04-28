from zipfile import *
from PIL import Image
import math

from faced.convert.converters import *
from faced.classifiers.face_classifier import *
from faced.cv_utils.cv_utils import *
from faced.pil_utils.pil_utils import *

def faced_keyword(zfile, keyword=None):
    image_props_dict = {}
    canvas_list = []
    #parent_canvas = Image.new('RGB', (int(0), int(0) ), (0, 0, 0))

    zf_class = ZipFile(zfile, mode='r')
    finfo = ZipFile(zfile, mode='r').infolist()

    for i in finfo:
        with Image.open(zf_class.open(name=i.filename)).convert('RGB') as img:
            img.load()
        image_props_dict[i.filename] = {'pil_obj':img}
        text = pytesseract.image_to_string(img)
        image_props_dict[i.filename]['text'] = text
        faces = extract_faces(img)
        image_props_dict[i.filename]['faces'] = faces

    for img_name in image_props_dict.keys():
        if keyword in image_props_dict[img_name]['text']:
            if len(image_props_dict[img_name]['faces']) != 0:
                print(f'faces and keyword found in file {img_name}')
                p = image_props_dict[img_name]['pil_obj']
                faces_rect = image_props_dict[img_name]['faces']
                canvas_control = Image.fromarray(faces_rect)
        
                #canvas building (balanced)
                ncol = math.ceil(len(faces_rect))
                nrow = math.ceil(len(faces_rect))
                canvas = Image.new(canvas_control.mode, (int(nrow*200), int(ncol*200) ))
                curr_x = 0
                curr_y = 0

                #heuristics
                for x,y,w,h in faces_rect:
                    face = p.crop((x,y,x+w,y+h))
                    face = make_thumbnail(face)
                    canvas.paste(face, (curr_x, curr_y) )
                    if curr_x + face.width == canvas.width:
                        curr_x = 0
                        curr_y = curr_y + face.height
                    else:
                        curr_x = curr_x + face.width

                canvas_list.append(canvas)
                canvas.show()
            
            else:
                print(f'No images found in {img_name}')

            nrows = math.ceil(len(canvas_list)/2)
            ncols = nrows
            template_img = canvas_list[0]
            cx = 0
            cy = 0
            parent_canvas = Image.new('RGB', (int(ncols*template_img.width), int(ncols*template_img.height)), (0,0,0))
            for j in canvas_list:
                parent_canvas.paste(j,(cx, cy))
                if cx + template_img.width == parent_canvas.width:
                    cx = 0
                    cy = cy + template_img.height
                else:
                    cx = cx + template_img.width

    parent_canvas.show()     
    return image_props_dict
            



