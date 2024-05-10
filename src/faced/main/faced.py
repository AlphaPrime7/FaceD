import math

from faced.convert.converters import *
from faced.cv_utils.cv_utils import *
from faced.classifiers.eye_classifier import *
from faced.classifiers.face_classifier import *

def faced(zipf):
    
    unzipped_dir = unzip_files(zipf)
    img_list = create_image_path(unzipped_dir)
    canvas_list = []
    haar_classifier = use_builtin_face_classifier()

    for i in img_list:
        n = cv.imread(i) 
        p=convert_arr_pil(n)
        grayimg=cv.cvtColor(n, cv.COLOR_BGR2GRAY)
        face_cascade = cv.CascadeClassifier(haar_classifier) 
        faces_rect = face_cascade.detectMultiScale(grayimg, scaleFactor=1.3, minNeighbors=3)

        if len(faces_rect) == 0:
            print(f'No images forund in {i}')
        else:
            canvas_control = Image.fromarray(faces_rect)
        
            #canvas building (balanced)
            ncol = math.ceil(len(faces_rect))
            nrow = math.ceil(len(faces_rect))
            canvas = Image.new(canvas_control.mode, (int(nrow*200), int(ncol*200)))
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
            #canvas.show()
            in_display(canvas)
        
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

    #parent_canvas.show()
    in_display(parent_canvas)
    delete_folder(unzipped_dir,empty_folder=False)
    return canvas

