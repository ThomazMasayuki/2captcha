from flask import request, jsonify
from utils.twocaptcha_solver import solve_twocaptcha

def add_routes(app):
    @app.route('/')
    def home():
        return "Serviço de API do 2Captcha, contendo: Recaptcha (v2,v3), Hcaptcha e Cloudflare."
    
    @app.route('/recaptchav2', methods=['GET'])
    def recaptchav2():
        site_key = request.args.get('site_key')
        page_url = request.args.get('page_url')
        version = 'v2'

        if not site_key or not page_url:
            return jsonify({"success": False, "message": "site_key e page_url não fornecidos"}), 400
        
        result = solve_twocaptcha(site_key, page_url, 'userrecaptcha', version)
        return jsonify(result)

    @app.route('/recaptchav3', methods=['GET'])
    def recaptchav3():
        site_key = request.args.get('site_key')
        page_url = request.args.get('page_url')
        version = 'v3'

        if not site_key or not page_url:
            return jsonify({"success": False, "message": "site_key e page_url não fornecidos"}), 400

        result = solve_twocaptcha(site_key, page_url, 'userrecaptcha', version)
        return jsonify(result)

    @app.route('/hcaptcha', methods=['GET'])
    def hcaptcha():
        site_key = request.args.get('site_key')
        page_url = request.args.get('page_url')
        if not site_key or not page_url:
            return jsonify({"success": False, "message": "site_key e page_url não fornecidos"}), 400

        result = solve_twocaptcha(site_key, page_url, 'hcaptcha')
        return jsonify(result)

    @app.route('/cloudflare', methods=['GET'])
    def cloudflare():
        site_key = request.args.get('site_key')
        page_url = request.args.get('page_url')
        if not site_key or not page_url:
            return jsonify({"success": False, "message": "site_key e page_url não fornecidos"}), 400

        result = solve_twocaptcha(site_key, page_url, 'cloudflare')
        return jsonify(result)