from flask import Flask
from src.config import Config
from src.controllers.compare_ctrl import compare_bp
from src.controllers.doc_ctrl import doc_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(compare_bp, url_prefix='/api/v1/face-id-comparison')
app.register_blueprint(doc_bp, url_prefix='/api/v1/document-extraction')

if __name__ == "__main__":
    app.run(debug=True)
