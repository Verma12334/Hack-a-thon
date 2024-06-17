# scripts/preprocess.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(features_path, labels_path):
    features = pd.read_csv(features_path)
    labels = pd.read_csv(labels_path)
    df = pd.merge(features, labels, on='respondent_id')
    return df

def preprocess_data(df):
    df = df.drop(columns=['respondent_id'])  # Drop the unique identifier
    
    # Handling missing values (simple strategy: fill with mode)
    for col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    # One-hot encoding for categorical features
    df = pd.get_dummies(df, drop_first=True)
    
    return df

def split_data(df):
    X = df.drop(columns=['xyz_vaccine', 'seasonal_vaccine'])
    y = df[['xyz_vaccine', 'seasonal_vaccine']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Standardizing the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    df = load_data('/mnt/data/training_set_features.csv', '/mnt/data/training_set_labels.csv')
    df = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(df)
    # Save preprocessed data
    pd.DataFrame(X_train).to_csv('/mnt/data/X_train.csv', index=False)
    pd.DataFrame(X_test).to_csv('/mnt/data/X_test.csv', index=False)
    y_train.to_csv('/mnt/data/y_train.csv', index=False)
    y_test.to_csv('/mnt/data/y_test.csv', index=False)
