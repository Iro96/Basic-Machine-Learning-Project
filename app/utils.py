import yaml
import pandas as pd

def load_config(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def load_data(path):
    return pd.read_csv(path)

def predict(model, data):
    return model.predict(data)
