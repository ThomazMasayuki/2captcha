from flask import Flask, request, jsonify
from requests.exceptions import JSONDecodeError

class CaptchaAPI:
    def __init__(self, app):
        self.app = app
        self.add_routes()
    
    def __add_routes(self):
        @self.app.route('/')
        def home():
            return "Serviço de API do 2Captcha, contendo: Recaptcha (v2,v3), Hcaptcha e Cloudflare."
        
        @self.app.route('/recaptchav2', methods=['GET'])
        def recaptchav2():
            return RecaptchaV2Route().handle_request()
        
        @self.app.route('/recaptchav3', methods=['GET'])
        def recaptchav3():
            return RecaptchaV3Route().handle_request()

class CaptchaSolverService:
    def __solve(site_key = str, page_url = str, captcha_type = str, version = str):
        return solve_twocaptcha(site_key = str, page_url = str, captcha_type = str, version = str)

class BaseCaptchaRoute:
    def __init__(self, captcha_type = str, version = str):
        self.captcha_type = captcha_type
        self.version = version
    
    def __handle_request(self):
        site_key = request.args.get('site_key')
        page_url = request.args.get('page_url')

        if not site_key or not page_url:
            return jsonify({"success": False, "message": "site_key e page_url não fornecidos"}), 400

        #Corrigir esta parte porque aparentemente não está legal
        result = CaptchaSolverService.solve(site_key, page_url, self.captcha_type, self.version)
        return jsonify(result)
    
    def solve_twocaptcha(site_key = str, page_url = str, captcha_type = str, version = str):
        return {"success": True, "captcha_type": captcha_type, "version": version, "site_key": site_key, "page_url": page_url}

class RecaptchaV2Route(BaseCaptchaRoute):
    def __init__(self):
        super().__init__('userrecaptcha', 'v2')

class RecaptchaV3Route(BaseCaptchaRoute):
    def __init__(self):
        super().__init__('userrecaptcha', 'v3')

class HcaptchaRoute(BaseCaptchaRoute):
    def __init__(self):
        super().__init__('hcaptcha')

class CloudflareRoute(BaseCaptchaRoute):
    def __init__(self):
        super().__init__('cloudflare')