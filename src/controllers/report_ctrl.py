#Controller for analytics and reporting
from flask import Blueprint, jsonify
from src.services.report_svc import get_analytics

report_bp = Blueprint('report', __name__)

@report_bp.route('/', methods=['GET'])
def analytics():
    results = get_analytics()
    return jsonify(results)
