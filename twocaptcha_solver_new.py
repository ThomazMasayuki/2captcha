from datetime import datetime, timedelta
from typing import Optional
from requests.exceptions import JSONDecodeError
import requests

class Erros:
    CAPCHA_NOT_READY = 'CAPCHA NÃO ESTÁ PRONTO'
    ERROR_CAPTCHA_UNSOLVABLE = 'ERRO CAPTCHA NÃO SOLUCIONÁVEL'
    ERROR_WRONG_USER_KEY = 'ERRO CHAVE DE USUÁRIO ERRADA'
    ERROR_KEY_DOES_NOT_EXIST = 'CHAVE DE ERRO NÃO EXISTE'
    ERROR_WRONG_ID_FORMAT = 'ID COM FORMATO ERRADO'
    ERROR_WRONG_CAPTCHA_ID = 'ID DO CAPTCHA NO FORMATO ERRADO'
    ERROR_BAD_DUPLICATES = 'NÚMERO MÁXIMO DE TENTATIVAS ATINGIDO'
    ERROR_REPORT_NOT_RECORDED = 'MAIS QUE 15MIN APÓS O ENVIO DO CAPTCHA'
    ERROR_DUPLICATE_REPORT = 'TERÁ ERRO NOVAMENTE SE ENVIAR O MESMO CAPTCHA'
    ERROR_IP_ADDRES = 'ERRO COM O ENDEREÇO DE IP'
    ERROR_TOKEN_EXPIRED = 'AO ENVIAR GEETEST, RETORNA ERRO PELO TEMPO EXPIRADO'
    ERROR_EMPTY_ACTION = 'ERROR_EMPTY_ACTION'
    ERROR_PROXY_CONNECTION_FAILED = 'NENHUM VALOR FOI FORNECIDO PARA O PARÂMETRO'
    ERROR_ZERO_CAPTCHA_FILESIZE = 'TAMANHO DA IMAGEM É MAIOR QUE 100 BYTES'
    TIME_OUT = 'TIME_OUT'
    NONE_TYPE = 'OBJETO VAZIO'

    @classmethod
    def is_valid_error(cls, error_type):
        return hasattr(cls, error_type)

    @classmethod
    def get_error_message(cls, error_type):
        if cls.is_valid_error(error_type):
            return getattr(cls, error_type)
        else:
            return "Erro desconhecido"

class Response:

    @staticmethod
    def get_response_sucess(solution: Optional[str]) -> dict:
        return {"success": True, "message": 'message', "captcha_solution": solution}

    @staticmethod
    def get_response_error(error: Optional[str]) -> dict:

        if error is None:
            error = 'NONE_TYPE'

        return {"success": False, "message": Erros.get_error_message(error), "captcha_solution": None}


class Solver2captcha:

    def __init__(self, site_key: str, key_2captcha: str, method: str, page_url: str, version: str, max_score: str):
        self.__site_key = site_key
        self.__key_2captcha = key_2captcha
        self.__method = method
        self.__page_url = page_url
        self.__version = version
        self.__max_score = max_score
        self.__domain = 'https://2captcha.com'

    def __get_params(self) -> dict:
        return {
            'key': self.__key_2captcha,
            'method': self.__method,
            'googlekey': self.__site_key,
            'pageurl': self.__page_url,
            'version': self.__version,
            'max_score': self.__max_score,
            'json': 1
        }

    def __generate_task_id(self) -> Optional[str]:
        try:
            response_json = requests.get(url=f"{self.__domain}/in.php", params=self.__get_params()).json()
        except (JSONDecodeError, requests.exceptions.RequestException):
            return
        return response_json.get('request', None)

    def __get_result(self, task_id: str) -> Optional[str]:
        try:
            response_json = requests.get(
                url=f"{self.__domain}/res.php?key={self.__key_2captcha}&action=get&id={task_id}&json=1").json()
        except (JSONDecodeError, requests.exceptions.RequestException):
            return
        return response_json.get('request', None)

    def solve(self):
        task_id = self.__generate_task_id()
        if task_id is None or Erros.is_valid_error(task_id):
            return Response.get_response_error(task_id)

        start_time = datetime.now()
        while True:

            if (datetime.now() - start_time) > timedelta(seconds=30):
                return Response.get_response_error('TIME_OUT')

            result = self.__get_result(task_id)

            if result is None:
                continue

            if Erros.is_valid_error(result):
                return Response.get_response_error(result)

            return Response.get_response_sucess(result)

if __name__ == '__main__':
    solver = Solver2captcha('', '', '', '', '', '')
    print(solver.solve())