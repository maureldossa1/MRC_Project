import streamlit as st
import requests
import numpy as np

#https://mrcstade.onrender.com/

# Configuration de la page
st.set_page_config(page_title="MRC", page_icon="📋", layout="wide")

# CSS pour améliorer le design
st.markdown("""
    <style>
        .stTextInput, .stButton > button {
            border-radius: 10px;
        }
        .main {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Simulation d'une base de données utilisateur
users = {"admin": "1234"}  # À remplacer par une vraie base de données

# Authentification
def login():
    st.title("🔐 Connexion")
    st.subheader("Veuillez entrer vos identifiant")

    username = st.text_input("Nom d'utilisateur", placeholder="Entrez votre nom")
    password = st.text_input("Mot de passe", type="password", placeholder="Entrez votre mot de passe")
    
    if st.button("Se connecter"):
        if username in users and users[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.rerun()  # Correction ici
        else:
            st.error("Identifiants incorrects ❌")
    

# Page de gestion des employés
def prédicteur():
    st.title("Prédiction de la Maladie Rénale Chronique (CKD)")

    # Création des champs du formulaire
    Age = st.number_input("Âge", step=1, min_value=0)
    Sexe = st.radio("Sexe", ["Homme", "Femme"])
    enquete_sociale_tabac = st.radio("Fumeur ?", ["Oui", "Non"])
    etat_general_omi = st.radio("Présence d'œdèmes (OMI) ?", ["Oui", "Non"])
    symptomes_asthenie = st.radio("Fatigue excessive (Asthénie) ?", ["Oui", "Non"])
    symptomes_nycturie = st.radio("Nycturie (besoin d'uriner la nuit) ?", ["Oui", "Non"])

    uree = st.number_input("Taux d'urée (mg/dL)")
    creatinine = st.number_input("Taux de créatinine (mg/dL)")
    hb = st.number_input("Hémoglobine (g/dL)")
    na = st.number_input("Sodium (mEq/L)")
    k = st.number_input("Potassium (mEq/L)")

    pathologies_retinopathie_hypertensive = st.radio("Rétinopathie hypertensive ?", ["Oui", "Non"])
    pathologies_retinopathie_diabetique = st.radio("Rétinopathie diabétique ?", ["Oui", "Non"])

    # Convertir les choix en valeurs numériques
    Sexe = 1 if Sexe == "Homme" else 0
    enquete_sociale_tabac = 1 if enquete_sociale_tabac == "Oui" else 0
    etat_general_omi = 1 if etat_general_omi == "Oui" else 0
    symptomes_asthenie = 1 if symptomes_asthenie == "Oui" else 0
    symptomes_nycturie = 1 if symptomes_nycturie == "Oui" else 0
    pathologies_retinopathie_hypertensive = 1 if pathologies_retinopathie_hypertensive == "Oui" else 0
    pathologies_retinopathie_diabetique = 1 if pathologies_retinopathie_diabetique == "Oui" else 0



    # Bouton de prédiction
    if st.button("Prédire"):
        with st.spinner("Prédiction en cours..."):
            try:
                # Données à envoyer à l'API
                data = {
                    "age": Age,
                    "sexe": Sexe,
                    "enquete_sociale_tabac": enquete_sociale_tabac,
                    "etat_general_omi": etat_general_omi,
                    "symptomes_asthenie": symptomes_asthenie,
                    "symptomes_nycturie": symptomes_nycturie,
                    "uree": uree,
                    "creatinine": creatinine,
                    "hb": hb,
                    "na": na,
                    "k": k,
                    "pathologies_retinopathie_hypertensive": pathologies_retinopathie_hypertensive,
                    "pathologies_retinopathie_diabetique": pathologies_retinopathie_diabetique,
                }

                # Appel API
                response = requests.post("https://mrcstade.onrender.com/predict", json=data)

                if response.status_code == 200:
                    # response.raise_for_status()  # Vérifie si l'API répond correctement
                    resultat = response.json()
                else:   
                    resultat = None

                
                # Vérification de la réponse
                if "predictions" in resultat:
                    rec = resultat["predictions"]
                    if rec == 1:
                        st.success(f"Stade CKD prédit : **CKD {rec}** ; ( DFG ≥ 90 mL/min/1,73 m² , Fonction rénale normale ou légèrement réduite, mais avec des signes de dommages rénaux )")
                    elif rec == 2:
                        st.success(f"Stade CKD prédit : **CKD {rec}** ; ( DFG = 60-89 mL/min/1,73 m² , Insuffisance rénale légère avec des signes de dommages rénaux )")
                    elif rec == 3:
                        st.success(f"Stade CKD prédit : **CKD 3a** ; ( DFG = 45-59 mL/min/1,73 m² , Insuffisance rénale modérée )")
                    elif rec == 4:
                        st.success(f"Stade CKD prédit : **CKD 3b** ; (  DFG = 30-44 mL/min/1,73 m² , Insuffisance rénale modérée à sévère )")
                    elif rec == 5:
                        st.success(f"Stade CKD prédit : **CKD 4** ; ( DFG = 15-29 mL/min/1,73 m² , Insuffisance rénale sévère )")
                    elif rec == 6:
                        st.success(f"Stade CKD prédit : **CKD 5** ; ( DFG < 15 mL/min/1,73 m² (ou dialyse) , Insuffisance rénale terminale. Les reins ont perdu la quasi-totalité de leur fonction )")
                    else:
                        st.error(f"Prédiction inconnue")
                else:
                    st.error("Erreur : réponse inattendue de l'API.")

            except requests.exceptions.RequestException as e:
                st.error(f"Erreur de connexion à l'API : {e}")
            except Exception as e:
                st.error(f"Erreur inattendue : {e}")

    if st.button("Déconnexion"):
        st.session_state["authenticated"] = False
        st.rerun()  # Correction ici

# Exécution de l'application
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    prédicteur()

























































































































# import streamlit as st
# import requests
# import numpy as np
# st.title("Prédiction de la Maladie Rénale Chronique (CKD)")

# # Création des champs du formulaire
# Age = st.number_input("Âge", step=1, min_value=0)
# Sexe = st.radio("Sexe", ["Homme", "Femme"])
# enquete_sociale_tabac = st.radio("Fumeur ?", ["Oui", "Non"])
# etat_general_omi = st.radio("Présence d'œdèmes (OMI) ?", ["Oui", "Non"])
# symptomes_asthenie = st.radio("Fatigue excessive (Asthénie) ?", ["Oui", "Non"])
# symptomes_nycturie = st.radio("Nycturie (besoin d'uriner la nuit) ?", ["Oui", "Non"])

# uree = st.number_input("Taux d'urée (mg/dL)")
# creatinine = st.number_input("Taux de créatinine (mg/dL)")
# hb = st.number_input("Hémoglobine (g/dL)")
# na = st.number_input("Sodium (mEq/L)")
# k = st.number_input("Potassium (mEq/L)")

# pathologies_retinopathie_hypertensive = st.radio("Rétinopathie hypertensive ?", ["Oui", "Non"])
# pathologies_retinopathie_diabetique = st.radio("Rétinopathie diabétique ?", ["Oui", "Non"])

# # Convertir les choix en valeurs numériques
# Sexe = 1 if Sexe == "Homme" else 0
# enquete_sociale_tabac = 1 if enquete_sociale_tabac == "Oui" else 0
# etat_general_omi = 1 if etat_general_omi == "Oui" else 0
# symptomes_asthenie = 1 if symptomes_asthenie == "Oui" else 0
# symptomes_nycturie = 1 if symptomes_nycturie == "Oui" else 0
# pathologies_retinopathie_hypertensive = 1 if pathologies_retinopathie_hypertensive == "Oui" else 0
# pathologies_retinopathie_diabetique = 1 if pathologies_retinopathie_diabetique == "Oui" else 0



# # Bouton de prédiction
# if st.button("Prédire"):
#     with st.spinner("Prédiction en cours..."):
#         try:
#             # Données à envoyer à l'API
#             data = {
#                 "age": Age,
#                 "sexe": Sexe,
#                 "enquete_sociale_tabac": enquete_sociale_tabac,
#                 "etat_general_omi": etat_general_omi,
#                 "symptomes_asthenie": symptomes_asthenie,
#                 "symptomes_nycturie": symptomes_nycturie,
#                 "uree": uree,
#                 "creatinine": creatinine,
#                 "hb": hb,
#                 "na": na,
#                 "k": k,
#                 "pathologies_retinopathie_hypertensive": pathologies_retinopathie_hypertensive,
#                 "pathologies_retinopathie_diabetique": pathologies_retinopathie_diabetique,
#             }

#             # Appel API
#             response = requests.post("http://127.0.0.1:8000/predict", json=data)

#             if response.status_code == 200:
#                 # response.raise_for_status()  # Vérifie si l'API répond correctement
#                 resultat = response.json()
#             else:   
#                 resultat = None

            
#             # Vérification de la réponse
#             if "predictions" in resultat:
#                 rec = resultat["predictions"]
#                 if rec == 1:
#                     st.success(f"Stade CKD prédit : **CKD {rec}** ; ( DFG ≥ 90 mL/min/1,73 m² , Fonction rénale normale ou légèrement réduite, mais avec des signes de dommages rénaux )")
#                 elif rec == 2:
#                     st.success(f"Stade CKD prédit : **CKD {rec}** ; ( DFG = 60-89 mL/min/1,73 m² , Insuffisance rénale légère avec des signes de dommages rénaux )")
#                 elif rec == 3:
#                     st.success(f"Stade CKD prédit : **CKD 3a** ; ( DFG = 45-59 mL/min/1,73 m² , Insuffisance rénale modérée )")
#                 elif rec == 4:
#                     st.success(f"Stade CKD prédit : **CKD 3b** ; (  DFG = 30-44 mL/min/1,73 m² , Insuffisance rénale modérée à sévère )")
#                 elif rec == 5:
#                     st.success(f"Stade CKD prédit : **CKD 4** ; ( DFG = 15-29 mL/min/1,73 m² , Insuffisance rénale sévère )")
#                 elif rec == 6:
#                     st.success(f"Stade CKD prédit : **CKD 5** ; ( DFG < 15 mL/min/1,73 m² (ou dialyse) , Insuffisance rénale terminale. Les reins ont perdu la quasi-totalité de leur fonction )")
#                 else:
#                     st.error(f"Prédiction inconnue")
#             else:
#                 st.error("Erreur : réponse inattendue de l'API.")

#         except requests.exceptions.RequestException as e:
#             st.error(f"Erreur de connexion à l'API : {e}")
#         except Exception as e:
#             st.error(f"Erreur inattendue : {e}")
