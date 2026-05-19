# MRC_Project : Prédiction des stades de la maladie rénale chronique (MRC)

![Machine Learning](https://img.shields.io/badge/-Machine%20Learning-blueviolet)
![Random Forest](https://img.shields.io/badge/-Random%20Forest-success)
![Streamlit](https://img.shields.io/badge/-Streamlit-ff69b4)
![FastAPI](https://img.shields.io/badge/-FastAPI-teal)

## 📌 Description du projet
Ce projet vise à prédire les stades de la maladie rénale chronique (MRC) à l'aide d'un modèle d'apprentissage automatique supervisé basé sur l'algorithme **Random Forest**. Le dataset utilisé est **"Data AI4CKD.xls"** (données confidentielles, ne pas partager).

## 🛠️ Installation et configuration

### Prérequis
- Python 3.8 ou supérieur
- `pip` pour l'installation des dépendances
- Le logiciel **Windows 10 CMake Release Graphviz** ([Télécharger ici](https://graphviz.org/download/))  
  *(Installer la version : `windows_10_cmake_Release_graphviz-install-12.2.1-win64.exe`)*

### Étapes d'installation
1. **Cloner le dépôt**  
   ```bash
   git clone https://github.com/votre_utilisateur/MRC_Project.git
   cd MRC_Project
2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
3. **Vérifier la présence du modèle pré-entraîné**
   Assurez-vous que le fichier `random_forest_model_MRC.pkl est présent dans le répertoire du projet`.

## 🚀 Exécution du projet
1. **Lancer l'API (Backend)**
   Ouvrez un terminal et exécutez :
   ```bash
   uvicorn Fast_api_MRC:app --reload
   ```
L'API sera accessible sur `http://localhost:8000`.

2. **Configurer le Frontend**
   Ouvrez le fichier **frontend.py** et remplacez l'URL à la ligne 96 par : `"https://localhost:8000"`
   
3. **Lancer l'interface utilisateur (Frontend)**
   Dans un nouveau terminal, exécutez :
   ```bash
    streamlit run frontend.py
   ```
   L'application sera accessible dans votre navigateur à l'adresse indiquée dans le terminal.

## 📂 Structure des fichiers
  ```bash
    MRC_Project/
      ├── random_forest_model_MRC.pkl         # Modèle Random Forest sauvegardé
      ├── notebook_fichier.ipynb              # Notebook d'analyse et d'entraînement
      ├── Fast_api_MRC.py                     # API FastAPI pour les prédictions
      ├── frontend.py                         # Interface Streamlit
      ├── requirements.txt                    # Dépendances Python
      └── Data AI4CKD.xls                     # Dataset (confidentiel)
   ```
    
## ⚠️ Confidentialité
Le dataset `"Data AI4CKD.xls"` est strictement confidentiel.

Ne pas partager, publier ou redistribuer les données sans autorisation.

## 📜 License & Copyright
© 2025 - **[DOSSA Maurel]**
Tous droits réservés.
Ce projet est sous licence propriétaire.
