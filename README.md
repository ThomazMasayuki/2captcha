# 2captcha

INTRODUÇÃO

Esta API fornece serviços para resolver diferentes tipos de captchas, incluindo reCAPTCHA v2, reCAPTCHA v3, hCaptcha e Cloudflare. Ela utiliza a plataforma 2Captcha para resolver os captchas e retornar as soluções.

Configuração

Para executar a aplicação, é necessário ter o Python e as bibliotecas Flask e requests instaladas. Além disso, a chave de API do 2Captcha deve ser configurada.

Necessárias instalações para funcionamento

pip install Flask requests

Inicialização

Crie e execute o aplicativo Flask:

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    
Endpoints

Rota: /
Método: GET
Descrição: Fornece uma descrição do serviço.

Resposta:

"Serviço de API do 2Captcha, contendo: Recaptcha (v2,v3), Hcaptcha e Cloudflare."

Resolver reCAPTCHA v2
Rota: /recaptchav2
Método: GET
Parâmetros:
site_key: Chave do site para o reCAPTCHA v2.
page_url: URL da página onde o captcha está presente.
version: Versão do reCAPTCHA (v2 ou v3).
Exemplo de Solicitação:

"http://localhost:5000/recaptchav2?site_key=6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u&page_url=https://2captcha.com/demo/recaptcha-v2&version=v2"

Resposta:

{
  "success": true,
  "captcha_solution": "solution_string"
}
Resolver reCAPTCHA v3
Rota: /recaptchav3
Método: GET
Parâmetros:
site_key: Chave do site para o reCAPTCHA v3.
page_url: URL da página onde o captcha está presente.
Exemplo de Solicitação:

"http://localhost:5000/recaptchav3?site_key=6LfB5_IbAAAAAMCtsjEHEHKqcB9iQocwwxTiihJu&page_url=https://2captcha.com/demo/recaptcha-v3&version=v3"

Resposta:

{
  "success": true,
  "captcha_solution": "solution_string"
}
Resolver hCaptcha
Rota: /hcaptcha
Método: GET
Parâmetros:
site_key: Chave do site para o hCaptcha.
page_url: URL da página onde o captcha está presente.

"http://localhost:5000/hcaptcha?site_key=f7de0da3-3303-44e8-ab48-fa32ff8ccc7b&page_url=https://2captcha.com/demo/hcaptcha"

Resposta:

{
  "success": true,
  "captcha_solution": "solution_string"
}
Resolver Cloudflare
Rota: /cloudflare
Método: GET
Parâmetros:
site_key: Chave do site para o Cloudflare.
page_url: URL da página onde o captcha está presente.

"http://localhost:5000/cloudflare?site_key=0x4AAAAAAAVrOwQWPlm3Bnr5&page_url=https://2captcha.com/demo/cloudflare-turnstile"

Resposta:

{
  "success": true,
  "captcha_solution": "solution_string"
}
Função de Solução de Captcha
A função solve_captcha é usada internamente para enviar uma solicitação ao serviço 2Captcha e obter a solução do captcha.

Notas Importantes
Substitua as chaves de exemplo e URLs pelas suas próprias ao fazer solicitações reais.
As respostas de erro retornam um campo "success": false e uma mensagem de erro.
Certifique-se de que sua chave da API 2Captcha (TWOCAPTCHA_API_KEY) esteja corretamente configurada no código.
