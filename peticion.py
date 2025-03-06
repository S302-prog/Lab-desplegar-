import requests
import json

url = "http://127.0.0.1:8000/predict"

data = [
    {
        "u": 19.20716,
        "g": 18.04355,
        "r": 17.51539,
        "redshift": 0.000209,
        "rowv": 0.003530,
        "colv": 0.000266,
        "STAR": 1,
        "GALAXY": 0
    }
]

response = requests.post(url, json=data)
if response.status_code == 200:

    print("Predicciones:", response.json())
else:
    print("Error en la solicitud:", response.status_code)


 # },
    # {
    #     "u": 17.88818,
    #     "g": 16.63334,
    #     "r": 16.08460,
    #     "redshift": 0.060579,
    #     "rowv": 0.003194,
    #     "colv": 0.003667,
    #     "STAR": 0,
    #     "GALAXY": 1
    # },
    # {
    #     "u": 19.39626,
    #     "g": 18.26639,
    #     "r": 17.53201,
    #     "redshift": 0.165146,
    #     "rowv": -0.005457,
    #     "colv": -0.004908,
    #     "STAR": 0,
    #     "GALAXY": 1
    # },
    # {
    #     "u": 18.94794,
    #     "g": 16.98951,
    #     "r": 16.07144,
    #     "redshift": 0.073052,
    #     "rowv": -0.001630,
    #     "colv": -0.003412,
    #     "STAR": 0,
    #     "GALAXY": 1
    # },
    # {
    #     "u": 18.36184,
    #     "g": 16.39597,
    #     "r": 15.35190,
    #     "redshift": 0.108423,
    #     "rowv": -0.002339,
    #     "colv": 0.000957,
    #     "STAR": 1,
    #     "GALAXY": 0
    # }