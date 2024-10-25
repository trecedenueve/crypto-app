import json
import pandas as pd
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
import psutil


# Configuración de la API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '10',
    'convert': 'EUR'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'your app code here',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# Obtener la lista de criptomonedas
cryptos = data['data']

# Extraer los datos importantes
data_list = []
for crypto in cryptos:
    data_list.append({
        'id': crypto['id'],
        'name': crypto['name'],
        'symbol': crypto['symbol'],
        'price_eur': crypto['quote']['EUR']['price'],
        'percent_change_1h': crypto['quote']['EUR']['percent_change_1h'],
        'percent_change_24h': crypto['quote']['EUR']['percent_change_24h'],
        'percent_change_7d': crypto['quote']['EUR']['percent_change_7d'],
        'last_updated': crypto['quote']['EUR']['last_updated'],
        'max_supply': crypto['max_supply'],
        'circulating_supply': crypto['circulating_supply'],
    })

# Crear DataFrame
new_df = pd.DataFrame(data_list)

# Nombre del archivo CSV
csv_filename = '/home/user/python/cryptos_data.csv'

# Verificar si el archivo ya existe
if os.path.exists(csv_filename):
    # Leer el CSV existente
    existing_df = pd.read_csv(csv_filename)
    # Concatenar el nuevo DataFrame con el existente
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)
else:
    # Si no existe, usar el nuevo DataFrame
    updated_df = new_df

# Guardar el DataFrame actualizado en el archivo CSV
updated_df.to_csv(csv_filename, index=False)
print(f'Data saved to {csv_filename}')