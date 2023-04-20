import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


def remove_non_numerical(data):
  non_floats = []
  for col in data:
      if data[col].dtypes not in [ "float64", "int64" ]:
          non_floats.append(col)
  return data.drop(columns=non_floats)

def get_data():
  data = pd.read_csv("dataset/FedCycleData071012 (2)_fixed.csv",na_values=[' '])

  data = remove_non_numerical(data)

  cols_to_remove=["MensesScoreDaySix","MensesScoreDaySeven","MensesScoreDayEight","MensesScoreDayNine","MensesScoreDayTen","MensesScoreDay11","MensesScoreDay12","MensesScoreDay13","MensesScoreDay14","MensesScoreDay15","PhasesBleeding","IntercourseDuringUnusBleed","AgeM","Maristatus","MaristatusM","Yearsmarried","Wedding","ReligionM","EthnicityM","Schoolyears","SchoolyearsM","OccupationM","IncomeM","Reprocate","Numberpreg","Livingkids","Miscarriages","Abortions","Medvits","LivingkidsM","Boys","Girls","MedvitsM","Breastfeeding","Method","Prevmethod","Methoddate","Whychart","Nextpreg","NextpregM","Spousesame","SpousesameM","Timeattemptpreg","BMI","MensesScoreDayFive","CycleNumber","Group"]
  return data.drop(columns=cols_to_remove)

def get_models():
  data = get_data()
  X=data.drop(columns=['LengthofCycle', 'EstimatedDayofOvulation'])
  Y=data['LengthofCycle']
  # x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

  gbr=GradientBoostingRegressor(random_state=42, max_depth=6, n_estimators=120, learning_rate=0.047, loss='huber', subsample=0.7, criterion='friedman_mse')
  loc_model = Pipeline(steps=[('features', SimpleImputer(strategy='mean')), ('scaler', StandardScaler()), ('model', gbr)])
  loc_model.fit(X, Y)

  # X = data.drop(columns=['EstimatedDayofOvulation'])
  temp = data.dropna(subset=['EstimatedDayofOvulation'])
  X = temp.drop(columns=['EstimatedDayofOvulation', 'LengthofCycle'])
  X['LengthofCycle'] = loc_model.predict(X)
  Y = temp['EstimatedDayofOvulation']
  svr =SVR(kernel='linear', tol=1e-9, epsilon=0.07)
  edo_model = Pipeline(steps=[('features', SimpleImputer(strategy='mean')), ('scaler', StandardScaler()), ('model', svr)])
  edo_model.fit(X, Y)

  return loc_model, edo_model


def main():
   loc_model, eoo_model = get_models()
   print(loc_model, eoo_model)

if __name__ == "__main__":
   main()