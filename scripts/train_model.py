# scripts/train_model.py
import pandas as pd
import xgboost as xgb
from sklearn.metrics import roc_auc_score
import joblib

def load_preprocessed_data():
    X_train = pd.read_csv('/mnt/data/X_train.csv')
    X_test = pd.read_csv('/mnt/data/X_test.csv')
    y_train = pd.read_csv('/mnt/data/y_train.csv')
    y_test = pd.read_csv('/mnt/data/y_test.csv')
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='auc', use_label_encoder=False)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict_proba(X_test)
    roc_auc = roc_auc_score(y_test, y_pred, average='macro')
    print(f'ROC AUC Score: {roc_auc}')
    return roc_auc

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_preprocessed_data()
    model = train_model(X_train, y_train)
    roc_auc = evaluate_model(model, X_test, y_test)
    joblib.dump(model, '/mnt/data/best_model.pkl')
