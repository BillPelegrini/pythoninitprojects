import requests
import json



end = input("Digite o CEP: ")
#end = '24416230'
r = requests.get('https://cep.awesomeapi.com.br/json/'+end)
z = r.text
l = json.loads(z)
print(l)
print(l['address_type'], l['address_name'],l['city'],l['district'],l['state'])