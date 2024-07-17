#Registers all controllers with the Flask application
from src.controllers.face_ctrl import face_bp
from src.controllers.doc_ctrl import doc_bp
from src.controllers.compare_ctrl import compare_bp
from src.controllers.obj_ctrl import obj_bp
from src.controllers.ocr_ctrl import ocr_bp
from src.controllers.account_ctrl import account_bp
from src.controllers.report_ctrl import report_bp

def register_controllers(app):
    app.register_blueprint(face_bp, url_prefix='/api/v1/face-recognition')
    app.register_blueprint(doc_bp, url_prefix='/api/v1/document-extraction')
    app.register_blueprint(compare_bp, url_prefix='/api/v1/face-id-comparison')
    app.register_blueprint(obj_bp, url_prefix='/api/v1/object-detection')
    app.register_blueprint(ocr_bp, url_prefix='/api/v1/text-recognition')
    app.register_blueprint(account_bp, url_prefix='/api/v1/account-management')
    app.register_blueprint(report_bp, url_prefix='/api/v1/analytics')
