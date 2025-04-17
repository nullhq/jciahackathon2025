
# Classeur auto de prune - JCIA Hackathon 2025

**Projet soumis par l'équipe** : FredyTaboutsa  
**Chef d'équipe** : Taboutsa Fredy  
**Membres** :  
- Taboutsa Fredy – Eleve Ingénieur en Intelligence Artificielle a l'ENSPY

---

## Objectif

Concevoir un modèle d'intelligence artificielle permettant de **classifier automatiquement les prunes camerounaises** en 6 catégories à partir d’images :  
- Bonne qualité  
- Non mûre  
- Tachetée  
- Fissurée  
- Meurtrie  
- Pourrie  

Dataset utilisé : [African Plums Dataset (Kaggle)](https://www.kaggle.com/datasets/arnaudfadja/african-plums-quality-and-defect-assessment-data/data)

---

## Compréhension du problème

Le défi est de créer un modèle performant de **vision par ordinateur** pour la classification automatique des prunes à partir d’images, afin de favoriser le tri automatisé dans les chaînes de distribution ou coopératives agricoles, et **réduire les pertes post-récolte**.

## Architecture & Technologies utilisées

| Composant | Choix technique | Justification |
|----------|----------------|----------------|
| Modèle IA | CNN (Convolutional Neural Network) avec RestNet18 via PyTorch | Adapté à la classification d’images avec un bon compromis entre performance et complexité |
| Backend | Flask | Simple, rapide à déployer pour une API ML |
| Frontend (démo) | HTML/CSS/JavaScript | Permet une interface rapide pour tester l’IA |
| Traitement données | Torch, PIL, Pandas | Troch pour appliquer des transformations sur les images existente pour générer de nouvelles, PIL pour la manipulation d'image en locale , Pandas pour gestion du dataset |
| Entraînement | Google Colab + GPU | Pour accélérer l’entraînement avec GPU libre  |
| Evaluation | sklearn | Pour produire un rapport de classification et la matrice de confusion |



## Méthodologie

1. **Prétraitement :**
   - Redimensionnement des images (224x224)
   - Normalisation [0,1]
   - Nettoyage des étiquettes
   - Data augmentation (rotation, zoom, flip horizontal)

2. **Split Dataset :**
   - 70% entraînement
   - 15% validation
   - 15% test

3. **Architecture :**
   - CNN simple (ResNet18)
   - `CrossEntropyLoss` comme fonction de perte

4. **Évaluation :**
   - Accuracy
   - F1 - Score
   - Recall
   - Matrice de confusion
   - Classification report


## Résultats obtenus

| Jeu de données | Accuracy |
|----------------|----------|
| Validation     | 65.46%   |
| Test final     | **65%**  |

> La classe "tachetée" et "meurtrie" sont parfois confondues, mais le modèle reste robuste sur les autres classes.



## Arborescence du projet

```txt
jciahackathon2025/
│
├── backend/  # Fichier du backend et model final 
├── frontend/  # Interface Web en HTML/CSS/JavaScript
├── notebooks/   # Notebook d'entrainement
├── scripts/     # Scripts construit pour équilibrer nos données
├── test_plums/  # Fichiers images de test pour chaque catégorie de prunes
└── README.md
```


## Lancer le projet en local

### 1. Cloner le dépôt

```bash
git clone https://github.com/nullhq/jciahackathon2025
cd jciahackathon2025
```
### 2. Lancer l’interface Web

```bash
cd frontend
open index.html
```

### 3. Lancer l’API Flask (requis pour le bon fonctionnement du backend)

```bash
cd backend
python api.py
```


## Démo vidéo

🔗 [Lien vers la démo YouTube](https://www.youtube.com/watch?v=Zf5_MznreTA)


## Hackathon JCIA 2025

**Thème** : Intelligence Artificielle et Développement Économique  
**Projet** : Tri Automatique des Prunes  
**Soumission** : 17 avril 2025  
