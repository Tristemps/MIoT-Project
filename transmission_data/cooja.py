import asyncio
import re
import time
import requests
import sys
from aiocoap import Context, Message
from aiocoap.numbers import Code

# Vérification de la présence de l'argument IPv6
if len(sys.argv) != 2:
    print("Usage: python script.py <IPv6_ADDRESS>")
    sys.exit(1)

ipv6_address = sys.argv[1]
coap_uri = f"coap://[{ipv6_address}]/test/power"

# Fonction pour récupérer les données via CoAP
async def get_coap_data():
    protocol = await Context.create_client_context()
    request = Message(code=Code.GET, uri=coap_uri)

    try:
        response = await protocol.request(request).response
        data = response.payload.decode("utf-8")
        print("Received Data:", data)
        return data
    except Exception as e:
        print("CoAP Error:", e)
        return None

# Fonction pour extraire les valeurs de la réponse
def parse_data(response):
    match = re.search(r"voltage\s*:\s*([\d.]+);\s*current\s*:\s*([\d.]+)", response)
    if match:
        voltage, current = match.groups()
        return float(voltage), float(current)
    return None, None

# Fonction pour envoyer les données à InfluxDB 1.x
def send_to_influxdb(voltage, current):
    influxdb_url = "http://localhost:8086/write?db=miot_db"  # InfluxDB 1.x utilise ?db=
    data = f"measurement voltage={voltage},current={current}"

    response = requests.post(influxdb_url, data=data)
    
    if response.status_code == 204:
        print("Données envoyées avec succès à InfluxDB")
    else:
        print(f"Erreur lors de l'envoi: {response.text}")

# Fonction principale qui s'exécute toutes les 5 secondes
async def main():
    while True:
        response = await get_coap_data()
        if response:
            voltage, current = parse_data(response)
            if voltage is not None and current is not None:
                send_to_influxdb(voltage, current)
        await asyncio.sleep(5)

# Exécuter le script
if __name__ == "__main__":
    asyncio.run(main())
