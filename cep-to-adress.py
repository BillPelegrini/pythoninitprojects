import requests
import json

end = '24416230'
r = requests.get('https://cep.awesomeapi.com.br/json/'+end)
z = r.text
l = json.loads(z)
print(type(l))
print(l['city'],l['cep'])