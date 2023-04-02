from twilio.rest import Client
import requests

cotacoes = requests.get(r'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')


cotacoes_dic = cotacoes.json()
cotacao_dolar = cotacoes_dic['USDBRL']['bid']
cotacao_euro = cotacoes_dic['EURBRL']['bid']
cotacao_btc = cotacoes_dic['BTCBRL']['bid']

mensagem = f'\nDólar: R$ {cotacao_dolar}\nEuro: R$ {cotacao_euro}\nBTC: R$ {cotacao_btc}'
print(mensagem)


account_sid = 'AC1adda40fd1457e6c23b44636602ae458'
auth_token = '40d7905e9788d748456acaf91b3c5fe8'
client = Client(account_sid, auth_token)

message = client.messages.create(
            to='[+5521971570367]',
            from_='[+15855318471]',
            body=mensagem)
