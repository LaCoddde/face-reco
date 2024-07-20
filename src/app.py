from flask import Flask, render_template
from config import Config
from controllers.compare_ctrl import compare_bp
from controllers.doc_ctrl import doc_bp
from controllers.face_ctrl import face_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(compare_bp, url_prefix='/api/v1/face-id-comparison')
app.register_blueprint(doc_bp, url_prefix='/api/v1/document-extraction')
app.register_blueprint(face_bp, url_prefix='/api/v1/face-recognition')

# Register test path APIs
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/face-recognition')
def face_recognition():
    return render_template('face_recognition.html')

@app.route('/document-extraction')
def document_extraction():
    return render_template('document_extraction.html')

if __name__ == "__main__":
    app.run(debug=True)
