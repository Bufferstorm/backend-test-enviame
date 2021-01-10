import requests
import json

url = "https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries"

payload = "{\n    \"shipping_order\": {\n        \"n_packages\": \"1\",\n        \"content_description\": \"ORDEN 255826267\",\n        \"imported_id\": \"255826267\",\n        \"order_price\": \"24509.0\",\n        \"weight\": \"0.98\",\n        \"volume\": \"1.0\",\n        \"type\": \"delivery\"\n    },\n    \"shipping_origin\": {\n        \"warehouse_code\": \"401\"\n    },\n    \"shipping_destination\": {\n        \"customer\": {\n            \"name\": \"Bernardita Tapia Riquelme\",\n            \"email\": \"b.tapia@outlook.com\",\n            \"phone\": \"977623070\"\n        },\n        \"delivery_address\": {\n            \"home_address\": {\n                \"place\": \"Puente Alto\",\n                \"full_address\": \"SAN HUGO 01324, Puente Alto, Puente Alto\"\n            }\n        }\n    },\n    \"carrier\": {\n        \"carrier_code\": \"\",\n        \"tracking_number\": \"\"\n    }\n}"
headers = {
    'Accept': 'application/json',
    'api-key': 'ea670047974b650bbcba5dd759baf1ed',
    'Content-Type': 'application/json'
}


def create_shipping_order(payload, url, headers):
    # Generar el post al endpoint
    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)
    # Guardar en una variable la respuesta
    data = response.text
    # Guardar en un archivo la respuesta
    with open('data.txt', 'w') as output_file:
        json.dump(data, output_file)
    # Retornar el status_code
    return response.status_code


print(create_shipping_order(payload, url, headers))
