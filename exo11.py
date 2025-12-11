# Exercice 11 : Simulation de Diagnostic (Cx OVID-19)
# Développez un programme qui utilise une fonction et un dictionnaire de symptômes (fievre, toux_seche, etc.) pour évaluer un score de risque et déterminer si le patient doit faire un test, comme décrit dans l'exercice initial.

# Variables (Booléens)
# Les paramètres booléens indiqueront la présence (True) ou l'absence (False) du symptôme
def CalculerRisque(fievre_presente, toux_seche_presente, fatigue_presente): 
    
    score_total = 0
    
    # Évaluation et pondération de chaque symptôme
    # L'accumulation (somme = somme + n) est utilisée pour calculer le score 
    if fievre_presente: 
        score_total = score_total + 3 
    
    if toux_seche_presente:
        score_total = score_total + 2 
    
    if fatigue_presente:
        score_total = score_total + 1
        
    return score_total # La fonction retourne le score calculé 
# Programme Principal (Test et Décision)
# Le corps principal initialise l'état du patient et utilise la structure if/elif/else pour interpréter le score et recommander une action.
# --- Données du Patient (Simulation de Saisie) ---
# Patient 1 : Fièvre et Toux sèche (score 3 + 2 = 5)
P1_FIEVRE = True
P1_TOUX = True
P1_FATIGUE = False

# Patient 2 : Fièvre et Fatigue (score 3 + 1 = 4)
P2_FIEVRE = True
P2_TOUX = False 
P2_FATIGUE = True

# Patient 3 : Toux sèche (score = 1)
P3_FIEVRE = False
P3_TOUX = False
P3_FATIGUE = True
# --- Exécution ---

# 1. Calcul du risque en appelant la fonction

 # Patient 1
risque_patient_1 = CalculerRisque(P1_FIEVRE, P1_TOUX, P1_FATIGUE)

print(f"Score de risque calculé : {risque_patient_1} points")

# Utilisation de la structure if/elif/else pour prendre une décision 
if risque_patient_1 >= 5: 
    print(">>> Recommandation : RISQUE TRÈS ÉLEVÉ. Un test de dépistage (CX OVID-19) est requis immédiatement.")
    
elif risque_patient_1 >= 3: # Gère les scores 3 et 4
    print(">>> Recommandation : RISQUE MODÉRÉ. Auto-isolement strict et consultation médicale sous 48h.")
    
else: # Gère les scores 0, 1 et 2
    print(">>> Recommandation : RISQUE FAIBLE. Surveillance des symptômes et repos.")


  # Patient 2

    risque_patient_2 = CalculerRisque(P2_FIEVRE, P2_TOUX , P2_FATIGUE)

print(f"Score de risque calculé : {risque_patient_2} points")

# Utilisation de la structure if/elif/else pour prendre une décision 
if risque_patient_2 >= 5: 
    print(">>> Recommandation : RISQUE TRÈS ÉLEVÉ. Un test de dépistage (CX OVID-19) est requis immédiatement.")
    
elif risque_patient_2 >= 3: # Gère les scores 3 et 4
    print(">>> Recommandation : RISQUE MODÉRÉ. Auto-isolement strict et consultation médicale sous 48h.")
    
else: # Gère les scores 0, 1 et 2
    print(">>> Recommandation : RISQUE FAIBLE. Surveillance des symptômes et repos.")

    # Patient 3

    risque_patient_3 = CalculerRisque(P3_FIEVRE, P3_TOUX , P3_FATIGUE)

print(f"Score de risque calculé : {risque_patient_3} points")

# Utilisation de la structure if/elif/else pour prendre une décision 
if risque_patient_3 >= 5: 
    print(">>> Recommandation : RISQUE TRÈS ÉLEVÉ. Un test de dépistage (CX OVID-19) est requis immédiatement.")
    
elif risque_patient_3 >= 3: # Gère les scores 3 et 4
    print(">>> Recommandation : RISQUE MODÉRÉ. Auto-isolement strict et consultation médicale sous 48h.")
    
else: # Gère les scores 0, 1 et 2
    print(">>> Recommandation : RISQUE FAIBLE. Surveillance des symptômes et repos.")