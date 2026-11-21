import requests
import json

# Les données d'entrée pour la prédiction
data = {
    'diagonal': 5.6,
    'height_left': 3.2,
    'height_right': 4.1,
    'margin_low': 2.5,
    'margin_up': 1.8,
    'length': 6.7
}
# Envoyer la requête POST à l'API
response = requests.post('http://localhost:5001/api/prediction', json=data)

# Récupérer la réponse JSON
prediction = response.json()

# Afficher les résultats
print('Prédiction:', prediction['prediction'])
print('Probabilité:', prediction['probability'])