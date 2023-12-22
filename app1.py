from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import easyocr

app = Flask(__name__)
upload_folder = os.path.join('static', 'uploads')
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app.config['UPLOAD'] = upload_folder

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        
        img = os.path.join(app.config['UPLOAD'], filename)
        # read the uploaded image usnig opencv
        image = cv2.imread(img)
        #PERFORM OCR
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(image)
        # SAVE THE EXTRACTED TEXT TO A TEXT FILE
        text_file_path = os.path.join(app.config['UPLOAD'], 'extracted_text.txt')
        with open(text_file_path, 'w') as text_file:
            for t in result:
                bbox, text_, score = t
                print(f"text:{text_}")
                if score > 0.25:
                    text_file.write(text_ )
        # pass the image and extracted text to the template
        
        return render_template('image_render.html', img=img, extracted_text =  [a for _,a, score in result if score > 0.25])
    return render_template('image_render.html')

if __name__ == '__main__':
    app.run(debug=True, port=8001)

# [a for _,a,_ in result]