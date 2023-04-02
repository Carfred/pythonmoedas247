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
auth_token = 'aa35219bada6cc432cb8f9477d7c2338'
client = Client(account_sid, auth_token)

message = client.messages.create(
            to='[+5521971570367]',
            from_='[+15855318471]',
            body=mensagem)

print('Mensagem enviada! ID:', message.sid)

