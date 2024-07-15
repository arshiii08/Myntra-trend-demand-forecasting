from flask import Flask, jsonify, render_template, request
import pandas as pd
import os
import google.generativeai as genai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

gemini_api_key = 'AIzaSyD3v-DKc9cyI6Uhtnt5HSEBIPAjyD0EIb4'  
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_insights(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error fetching insights: {e}")
        return f"Error fetching insights: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        return f"Error reading uploaded file: {e}"

    data_summary = df.describe(include='all').to_string()
    insight_prompt = f"Based on the uploaded fashion data: {data_summary}, provide insights on fashion trends."

    insight = generate_insights(insight_prompt)

    return jsonify({
        'insight': insight
    })

if __name__ == '__main__':
    app.run(debug=True)
