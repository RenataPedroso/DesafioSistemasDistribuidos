# type: ignore[assignment]
import rpyc # biblioteca para Python RPC
from rpyc.utils.server import ThreadedServer 
import requests as rs # requisições Web
import json # tratamento do JSON

class MyService(rpyc.Service):
    def exposed_echo(self, text):
        print(text)

    def exposed_soma(self, x, y):
        print('Usaram o recurso de soma')
        return int(x) + int(y)

    def exposed_subtracao(self, x, y):
        return int(x) - int(y)

    def exposed_cep(self, cep):
        api = 'https://cep.awesomeapi.com.br/json'
        
        ret = rs.get(f'{api}/{cep}')
        print('Usaram o recurso de CEP: ', cep)
        return json.loads(ret.text)

if __name__ == "__main__":
    server = ThreadedServer(MyService, hostname='0.0.0.0', port = 18812)
    print('Servidor online')
    server.start()