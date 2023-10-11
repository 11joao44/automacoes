import requests # Biblioteca para fazer requisição
import email.message
import smtplib

requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL") # API Cotação
print(requisicao) # Verificando a resposta da requisição

requisicao_dic = requisicao.json()
cotacao = requisicao_dic['USDBRL']['bid']
print(cotacao)

def enviar_email(cotacao):
    corpo_email = f"""
    <p>Dolar está abaixo de R$ 5.10. Cotação atual: R${cotacao}</p>
    """
    
    msg = email.message.Message()
    msg['Subject'] = "Dolar baixo"
    msg['From'] = "joao.inacio@redeflex.com.br"
    msg['To'] = "joao.inacio@redeflex.com.br"
    password = 'Mt.78115686'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login(msg['From'], password)
    s.login(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
    