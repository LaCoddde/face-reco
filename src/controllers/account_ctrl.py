#Controller for developer account management
from flask import Blueprint, request, jsonify
from src.services.account_svc import create_account, generate_api_key, revoke_api_key, delete_account_id

account_bp = Blueprint('account', __name__)

@account_bp.route('/create', methods=['POST'])
def create():
    data = request.json
    results = create_account(data)
    return jsonify(results)

@account_bp.route('/generate-key', methods=['POST'])
def generate_key():
    data = request.json
    results = generate_api_key(data['username'])
    return jsonify(results)

@account_bp.route('/revoke-key', methods=['POST'])
def revoke_key():
    data = request.json
    results = revoke_api_key(data['username'])
    return jsonify(results)

@account_bp.route('/delete-account', methods=['POST'])
def delete_account():
    data = request.json
    results = delete_account_id(data['username'])
    return jsonify(results)

@account_bp.route('/billing')