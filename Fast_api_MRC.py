from fastapi import FastAPI , Request
import joblib
import pandas as pd
app = FastAPI()

@app.get("/")
def greet():
    return {"message": "bonjour"}

def load_model():
    model_path = "ramdom_forest_model_MRC.pkl"  # Correction du nom du fichier
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Erreur lors du chargement du modèle : {e}")
        return None

# Chargement du model
model = load_model()

@app.post("/predict")
async def predict(req: Request):
    if model is None:
        return {"error": "Modèle non chargé"}

    data = await req.json()
    
    # Mappage entre vos noms de variables et ceux attendus par le modèle
    feature_mapping = {
        "age": "Age",
        "sexe": "Sexe",
        "enquete_sociale_tabac": "Enquête Sociale/Tabac",
        "etat_general_omi": "Etat Général (EG)/OMI",
        "symptomes_asthenie": "Symptômes/Asthénie",
        "symptomes_nycturie": "Symptômes/Nycturie",
        "uree": "Urée (g/L)",
        "creatinine": "Créatinine (mg/L)",
        "hb": "Hb (g/dL)",
        "na": "Na^+ (meq/L)",
        "k": "K^+ (meq/L)",
        "pathologies_retinopathie_hypertensive": "Pathologies/Rétinopathie hypertensive",
        "pathologies_retinopathie_diabetique": "Pathologies/Rétinopathie diabétique"
    }
    
    # Création d'un DataFrame avec les bons noms de colonnes
    input_data = pd.DataFrame([[
        data["age"],
        data["sexe"],
        data["enquete_sociale_tabac"],
        data["etat_general_omi"],
        data["symptomes_asthenie"],
        data["symptomes_nycturie"],
        data["uree"],
        data["creatinine"],
        data["hb"],
        data["na"],
        data["k"],
        data["pathologies_retinopathie_hypertensive"],
        data["pathologies_retinopathie_diabetique"]
    ]], columns=[feature_mapping[key] for key in [
        "age", "sexe", "enquete_sociale_tabac", "etat_general_omi",
        "symptomes_asthenie", "symptomes_nycturie", "uree", "creatinine",
        "hb", "na", "k", "pathologies_retinopathie_hypertensive",
        "pathologies_retinopathie_diabetique"
    ]])
    
    predictions = model.predict(input_data)
    return {"predictions": int(predictions[0])}