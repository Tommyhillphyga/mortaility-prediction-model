feature_list = ['age', 'gendera', 'BMI', 'hypertensive',
       'atrialfibrillation', 'CHD with no MI', 'diabetes', 'deficiencyanemias',
       'depression', 'Hyperlipemia', 'Renal failure', 'COPD', 'heart rate',
       'Systolic blood pressure', 'Diastolic blood pressure',
       'Respiratory rate', 'temperature', 'SP O2', 'Urine output', 'RBC',
       'MCHC', 'MCV', 'RDW', 'Leucocyte', 'Platelets', 'Basophils',
       'Lymphocyte', 'INR', 'NT-proBNP', 'Creatine kinase', 'Creatinine',
       'Urea nitrogen', 'glucose', 'Blood potassium', 'Blood sodium',
       'Blood calcium', 'Chloride', 'Anion gap', 'Magnesium ion', 'PH',
       'Bicarbonate', 'Lactic acid', 'PCO2', 'EF']

feature_map = {
    'age': 'Patient\'s age',
    'gendera': 'Patient\'s sex, [male-0, female-1] ',
    'BMI': 'Body mass index',
    'hypertensive': 'High blood pressure condition [False-0, True-1]',
    'atrialfibrillation': 'Irregular heart rhythm [False-0, True-1]',
    'CHD with no MI': 'Coronary heart disease, no heart attack [False-0, True-1]',
    'diabetes': 'Blood sugar disorder [False-0, True-1]',
    'deficiencyanemias': 'Low red blood cells [False-0, True-1]',
    'depression': 'Mental health condition [False-0, True-1]',
    'Hyperlipemia': 'High blood fat levels [False-0, True-1]',
    'Renal failure': 'Kidney failure [False-0, True-1]',
    'COPD': 'Chronic obstructive pulmonary disease [False-0, True-1]',
    'heart rate': 'Beats per minute',
    'Systolic blood pressure': 'Top blood pressure reading',
    'Diastolic blood pressure': 'Bottom blood pressure reading',
    'Respiratory rate': 'Breaths per minute',
    'temperature': 'Body temperature',
    'SP O2': 'Blood oxygen saturation',
    'Urine output': 'Volume of urine produced',
    'RBC': 'Red blood cell count',
    'MCHC': 'Mean corpuscular hemoglobin concentration',
    'MCV': 'Mean corpuscular volume',
    'RDW': 'Red cell distribution width',
    'Leucocyte': 'White blood cell count',
    'Platelets': 'Blood clotting cells count',
    'Basophils': 'Basophil white blood cells',
    'Lymphocyte': 'Lymphocyte white blood cells',
    'INR': 'Blood clotting time',
    'NT-proBNP': 'Heart failure biomarker',
    'Creatine kinase': 'Muscle enzyme level',
    'Creatinine': 'Kidney function marker',
    'Urea nitrogen': 'Waste product in blood',
    'glucose': 'Blood sugar level',
    'Blood potassium': 'Potassium ion concentration',
    'Blood sodium': 'Sodium ion concentration',
    'Blood calcium': 'Calcium ion concentration',
    'Chloride': 'Chloride ion concentration',
    'Anion gap': 'Difference in measured ions',
    'Magnesium ion': 'Magnesium ion concentration',
    'PH': 'Blood acidity',
    'Bicarbonate': 'Blood bicarbonate level',
    'Lactic acid': 'Indicator of oxygen deprivation',
    'PCO2': 'Carbon dioxide pressure',
    'EF': 'Ejection fraction (heart function)'
}