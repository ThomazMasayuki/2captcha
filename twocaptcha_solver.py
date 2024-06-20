import requests
import time
from datetime import datetime, timedelta
from config import key

class Solver2captcha: 
    def __init__(self, sitekey, method, version):

        def solve_twocaptcha(site_key, url, method, version=None):
            request_url = f"https://2captcha.com/in.php"
            params = {
                'key': key,
                'method': method,
                'googlekey': site_key,
                'pageurl': url,
                'json': 1
            }
            
            if version == 'v3':
                params['version'] = 'v3'
                params['max_score'] = 0.3

            response = requests.get(request_url, params=params)
            result = response.json()

            if result['status'] != 1:
                return {"success": False, "message": result.get('request', 'Erro ao enviar a solicitação')}

            request_id = result['request']
            fetch_url = f"http://2captcha.com/res.php?key={key}&action=get&id={request_id}&json=1"
            
            start_time = datetime.now()

            while True:
                
                current_time = datetime.now()
                elapsed_time = current_time - start_time # Diminuição do tempo decorrido e gerando a condição do período maior sendo maior que 30s
                
                if elapsed_time > timedelta(seconds=30):
                    return {"success": False, "message": "Timeout: A solução do captcha demorou mais de 30 segundos."}
                
                response = requests.get(fetch_url)
                result = response.json()
                if result['status'] == 1:
                    return {"success": True, "captcha_solution": result['request']}
                elif result['request'] == 'CAPCHA_NOT_READY':
                    time.sleep(5)
                else:
                    return {"success": False, "message": result.get('request', 'Erro desconhecido')}

        #data inicial e data final loop. (dif de tempo no sistema > 30)       
            #while true
                #time.out (30s)
                #"Erro de timeout, tente novamente"
        #      data e hora atual 