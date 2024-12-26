import requests

url = 'https://docs.google.com/spreadsheets/d/17mmfgPAcVCeHW3548BlFtuurAvF3jeffRVO1NW7rVgQ/export?format=csv'


headers = {'User-Agent': 'Mozilla/5.0'}

content = requests.get(url, headers=headers).content

with open('caso_full.csv.csv','wb') as file:
    file.write(content)
print(content)