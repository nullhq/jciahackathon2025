from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
import torchvision.transforms as transforms

app = Flask(__name__)
CORS(app)

# Classes dans l'ordre
classes = ['meurtrie (bruised)', 'fissuré (cracked)', 'pourrie (rotten)', 'tachetée (spotted)', 'de bonne qualité (unaffected)', 'non mûre (unripe)']

# Charger le modèle
# Ici on charge le modèle avec les poids et la structure que nous avons entrainé sur Google Colab
model = torch.load('classeur_de_prunes_v4.pt', map_location=torch.device('cpu'), weights_only=False)
model.eval()

# Transformations comme à l'entraînement on doit les appliquer à l'inférence aussi sinon ça ne marche pas
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])


# La route a disposition du frontend pour faire des prédictions grâce à l'API
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'Aucune image fournis...'}), 400
    
    image_file = request.files['image']
    image = Image.open(image_file.stream).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)  # batch size = 1

    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = torch.max(outputs, 1)
        predicted_class = classes[predicted.item()]

    return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)