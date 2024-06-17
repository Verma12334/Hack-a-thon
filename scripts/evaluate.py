# scripts/evaluate.py
import pandas as pd
from sklearn.metrics import roc_auc_score

def evaluate(true_labels_path, predictions_path):
    true_labels = pd.read_csv(true_labels_path)
    predictions = pd.read_csv(predictions_path)
    
    roc_auc = roc_auc_score(true_labels, predictions[['xyz_vaccine', 'seasonal_vaccine']], average='macro')
    print(f'ROC AUC Score: {roc_auc}')
    return roc_auc

if __name__ == "__main__":
    evaluate('/mnt/data/y_test.csv', 'submission.csv')
