# scripts/predict.py
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

def load_model():
    return joblib.load('/mnt/data/best_model.pkl')

def preprocess_new_data(df):
    # Preprocess new data similarly to training data
    df = df.drop(columns=['respondent_id'])
    for col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    df = pd.get_dummies(df, drop_first=True)
    
    # Standardize the data
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    
    return df

def make_predictions(model, df):
    X = preprocess_new_data(df)
    predictions = model.predict_proba(X)
    return predictions

if __name__ == "__main__":
    df = pd.read_csv('/mnt/data/test_set_features.csv')
    model = load_model()
    predictions = make_predictions(model, df)
    output = pd.DataFrame({
        'respondent_id': df['respondent_id'],
        'xyz_vaccine': predictions[:, 0],
        'seasonal_vaccine': predictions[:, 1]
    })
    output.to_csv('/mnt/data/submission.csv', index=False)
