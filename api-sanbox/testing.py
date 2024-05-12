import requests

URL = 'http://127.0.0.1:5000/'

# data =[
#     {'person':'Matias Leal','vehicle':'Etios','service':'1000 km'},
#     {'person':'Antoni Perez','vehicle':'Corrolla','service':'2000 km'},
#     {'person':'Maria Hernandez','vehicle':'Hilux','service':'4000 km'},
#
# ]
#
# for i in range(len(data)):
#     response = requests.put(URL + f"booking/{i}", data[i])
#     print(response.json())

response = requests.get(URL + "booking/1")
print(response.text)
