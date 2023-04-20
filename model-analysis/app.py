import pandas as pd
from flask import Flask, jsonify, request

from train import get_models

app = Flask(__name__)
loc_model, edo_model = get_models()

def format_prediction(prediction):
  if isinstance(prediction, tuple):
    return prediction
  return prediction.tolist()

@app.route("/predict", methods=["POST"])
def predict():
  # get the data from the request
  data = request.json
  if not data:
    return jsonify({"error": "no data provided"}), 422

  # get the features from the data
  # features = [
  #   [
  #     CycleWithPeakorNot, ReproductiveCategory,
  #     MeanCycleLength, LengthofLutealPhase,
  #     FirstDayofHigh, TotalNumberofHighDays,
  #     TotalHighPostPeak, TotalNumberofPeakDays,
  #     TotalDaysofFertility, TotalFertilityFormula,
  #     LengthofMenses, MeanMensesLength, MensesScoreDayOne,
  #     MensesScoreDayTwo, MensesScoreDayThree, MensesScoreDayFour,
  #     TotalMensesScore, MeanBleedingIntensity,
  #     NumberofDaysofIntercourse, IntercourseInFertileWindow,
  #     UnusualBleeding, Age, Religion, Ethnicity, Height, Weight
  #   ]
  # ]
  features = data["features"]

  features = pd.DataFrame(features, columns=["CycleWithPeakorNot", "ReproductiveCategory", "MeanCycleLength", "LengthofLutealPhase", "FirstDayofHigh", "TotalNumberofHighDays", "TotalHighPostPeak", "TotalNumberofPeakDays", "TotalDaysofFertility", "TotalFertilityFormula", "LengthofMenses", "MeanMensesLength", "MensesScoreDayOne", "MensesScoreDayTwo", "MensesScoreDayThree", "MensesScoreDayFour", "TotalMensesScore", "MeanBleedingIntensity", "NumberofDaysofIntercourse", "IntercourseInFertileWindow", "UnusualBleeding", "Age", "Religion", "Ethnicity", "Height", "Weight"])

  # make the prediction
  lengths_of_cycle = loc_model.predict(features)
  features["LengthofCycle"] = lengths_of_cycle

  # make the prediction
  estimated_day_of_ovulation = edo_model.predict(features)

  # return the prediction based on if model returns ndarray or list
  return jsonify({"LengthofCycle": format_prediction(lengths_of_cycle), "EstimatedDayofOvulation": format_prediction(estimated_day_of_ovulation)}), 200

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

print("Server has started")