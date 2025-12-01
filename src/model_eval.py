import numpy as np
import pandas as pd
import pickle
import json
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.ensemble import RandomForestClassifier

#test_data = pd.read_csv("./data/processed/test_processed.csv")
def load_data(filepath: str) -> pd.DataFrame:
  try:
    return pd.read_csv(filepath)
  except Exception as e:
    raise Exception(f"Error loading data from {filepath}: {e}")

# model = pickle.load(open("model.pkl","rb"))
def load_model(filepath: str) -> RandomForestClassifier:
  try:
    with open(filepath,"rb") as file:
      model = pickle.load(file)
    return model
  except Exception as e:
    raise Exception(f"Error loading model from {filepath}: {e}")

# X_test = test_data.drop(columns=['Potability'],axis=1)
# y_test = test_data['Potability']
def prepare_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
  try:
    X = data.drop(columns=['Potability'],axis=1)
    y = data['Potability']
    return X,y
  except Exception as e:
    raise Exception(f"Error preparing data: {e}")

# y_pred = model.predict(X_test)
def evaluate_model(model: RandomForestClassifier, X: pd.DataFrame, y: pd.Series) -> dict:
  try:
    y_pred = model.predict(X)
    acc = accuracy_score(y,y_pred)
    precision = precision_score(y,y_pred)
    recall = recall_score(y,y_pred)
    f1 = f1_score(y,y_pred)
    metrics_dict = {
      'acc':acc,
      'precision':precision,
      'recall':recall,
      'f1_score':f1
    }
    return metrics_dict
  except Exception as e:
    raise Exception(f"Error evaluating model: {e}")


# with open('metrics.json','w') as f:
#   json.dump(metrics_dict,f)
def save_metrics(metrics_dict: dict, filepath: str) -> None:
  try:
    with open(filepath,'w') as file:
      json.dump(metrics_dict,file, indent=4) #indent=4 for pretty printing
    print(f"Metrics saved to {filepath}")
  except Exception as e:
    raise Exception(f"Error saving metrics to {filepath}: {e}")


def main():
  try:
    test_data_path = "data/processed/test_processed.csv"
    model_path = "model.pkl"
    metrics_path = "metrics.json"

    test_data = load_data(test_data_path)
    X_test, y_test = prepare_data(test_data)
    model = load_model(model_path)
    metrics = evaluate_model(model, X_test, y_test)
    save_metrics(metrics, metrics_path)
  except Exception as e:
    raise Exception(f"Error evaluating model: {e}")
  print("Model evaluation completed successfully")

if __name__ == "__main__":
  main()
