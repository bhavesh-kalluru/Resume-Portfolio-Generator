from flask import Flask, render_template, request, redirect, url_for
import os
import random
from werkzeug.utils import secure_filename
from utils.parser import extract_resume_data

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Templates to rotate
TEMPLATES = ['template1.html', 'template2.html', 'template3.html']

def allowed_file(filename):
    # Accept only .pdf or .docx and filename contains 'resume' or 'cv' (case insensitive)
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    name = filename.lower()
    return ext in ALLOWED_EXTENSIONS and ('resume' in name or 'cv' in name)

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return "No file part", 400

        file = request.files['resume']
        if file.filename == '':
            return "No selected file", 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            data = extract_resume_data(filepath)
            selected_template = random.choice(TEMPLATES)

            return render_template(selected_template, **data)

        return "Invalid file format or filename. Please upload a PDF or DOCX resume file containing 'resume' or 'cv' in its name.", 400

    return '''
    <h2>Upload Your Resume (.pdf or .docx)</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="resume" accept=".pdf,.docx" required>
        <br><small>Filename should contain 'resume' or 'cv'</small><br><br>
        <button type="submit">Generate Portfolio</button>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
