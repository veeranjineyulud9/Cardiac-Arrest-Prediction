from django.shortcuts import render
from joblib import load
import numpy as np

# Load the model and scaler (ensure you saved the scaler during training)
model =load("./savedModels/model.joblib")

def predictor(request):
    if request.method == "POST":
        # Retrieve form data
        Age_In_Days = int(request.POST["Age_In_Days"])
        Sex = int(request.POST["Sex"])
        ChestPainType = int(request.POST["ChestPainType"])
        RestingBP = int(request.POST["RestingBP"])
        RestingECG = int(request.POST["RestingECG"])
        MaxHR = int(request.POST["MaxHR"])
        ExerciseAngina = int(request.POST["ExerciseAngina"])
        Oldpeak = float(request.POST["Oldpeak"])
        ST_Slope = int(request.POST["ST_Slope"])
        slp = int(request.POST["slp"])
        caa = int(request.POST["caa"])
        thall = int(request.POST["thall"])

        
    

        # Make prediction
        y_pred= model.predict([[Age_In_Days, Sex, ChestPainType, RestingBP, RestingECG,
                                MaxHR, ExerciseAngina, Oldpeak, ST_Slope, slp, caa, thall]])
        #result = "Heart Disease Detected" if y_pred_loaded[0] == 1 else "No Heart Disease"




        if y_pred[0] == 0:
             result = "The baby shows no signs of heart disease."
        else:
             result = "The baby has been diagnosed with heart disease."
        return render(request, "result.html", {"result": result})


        

    return render(request, "index.html")
