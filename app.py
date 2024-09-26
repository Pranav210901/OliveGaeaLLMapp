from flask import Flask, request, jsonify
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part in the request'
        
        file = request.files['file']
        #print(file.filename)
        if file.filename == '':
            return 'No file selected'
        elif file.filename!='':
            file.filename = "images.jpeg"
        
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            return f'File successfully uploaded to {file_path}'
    return f'{file_path}'

def run_script():
    if request.method == 'GET':
        file = open(r'/home/pranavpokhrel/cogvlm/cogvlm.py', 'r').read()
        locals = {}
        exec(file, globals(), locals)
        res1 = locals['res']
        print(res1)
    return res1
    #return jsonify({"message":res1})
    

@app.route('/api', methods=['GET', 'POST'])
def handle_requests():
    if request.method == 'POST':
        return upload_file()
    else:
        return run_script()

def extract_text():
    text = request.form.get('query', '')  # default to empty if 'text' field is not present
    print(text)
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


