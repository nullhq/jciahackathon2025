import os
from PIL import Image
from torchvision import transforms
import random

# le chemin vers le répertoire contenant les images
base_dir = "../african_plums"

# Le nombre d'images par classe après augmentation
target_count = 1721 # 800 pour cracked, 1721 pour les autres classes

# Transformations pour la data augmentation
transform_augmentation = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    transforms.RandomVerticalFlip(),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
    transforms.GaussianBlur(3, sigma=(0.1, 2.0)),
])

# Classes à augmenter
# cracked a déjà été augmenté jusqu'a 800 avec ce meme script
# pour éviter le surapprentissage (overfitting) sur les images de la classe cracked
augment_classes = ['bruised', 'rotten', 'spotted', 'unripe']

for cls in augment_classes:
    class_dir = os.path.join(base_dir, cls)
    images = sorted([f for f in os.listdir(class_dir) if f.endswith('.png')])
    current_count = len(images)
    print(f"{cls}: {current_count} images")

    needed = target_count - current_count
    print(f"  ➜ Génération de {needed} nouvelles images...")

    if needed <= 0:
        print("  ➜ Déjà équilibré.")
        continue

    # Trouver le dernier numéro utilisé
    last_num = max([
        int(f.split('_plum_')[1].split('.')[0])
        for f in images if '_plum_' in f
    ])

    for i in range(needed):
        img_name = random.choice(images)
        img_path = os.path.join(class_dir, img_name)

        with Image.open(img_path) as img:
            img = img.convert("RGB")
            augmented_img = transform_augmentation(img)

            # Générer le nom en incrementant le dernier numéro
            # et en ajoutant un suffixe pour éviter les collisions
            new_index = last_num + i + 1
            new_name = f"{cls}_plum_{new_index}.png"
            new_path = os.path.join(class_dir, new_name)

            augmented_img.save(new_path)

    print(f"{cls} maintenant à {target_count} images.")

print("\n Augmentation terminée avec succes.")
