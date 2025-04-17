// app.js
// Ce fichier JavaScript gère l'interaction avec l'utilisateur et la communication avec l'API Flask

const fileInput = document.getElementById('file_input');
const previewImage = document.querySelector('.preview_image img');
const resultBox = document.querySelector('.classes_predite');

fileInput.addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    // Afficher l'aperçu de l'image
    const reader = new FileReader();
    reader.onload = () => {
        previewImage.src = reader.result;
    };
    reader.readAsDataURL(file);

    // Préparer la requête pour l'API Flask
    const formData = new FormData();
    formData.append('image', file);

    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error('Erreur lors de la requête à l’API');

        const data = await response.json();
        resultBox.innerHTML = `<p><strong>Prune ${data.prediction}</strong></p>`;
    } catch (error) {
        resultBox.innerHTML = `<p style="color:red;">Erreur : ${error.message}</p>`;
    }
});