import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

def read_dataset(fpath):
    'Reads a CSV file into a pandas dataframe'
    return pd.read_csv(fpath).fillna(0)

def prepare_dataset(dataset):
    'Prepares a pandas dataframe for ML'
    # Convert categorical variables to boolean ones
    return pd.get_dummies(dataset)

def split_dataset(dataset, y_feature):
    'Split the dataset and return a tuple of (test, train)'
    # Create X and Y datasets
    return train_test_split(dataset.drop(y_feature, axis=1), dataset[y_feature])

def scale_features(X_train, X_test):
    'Normalise training inputs to prevent erratic model convergence behaviour'
    scaler = StandardScaler() # Initialise scaler object
    scaler.fit(X_train)       # Compute mean and standard deviation of dataset
    return scaler.transform(X_train), scaler.transform(X_test)

def run_model(X_train, y_train):
    'Runs an MLP Classifier model on the training datasets and returns a fit'
    model = MLPClassifier(hidden_layer_sizes=(3), max_iter=100)
    model.fit(X_train, y_train)
    return model

def run(fpath, y_feature):
    'Run an MLP Classifier model over the fpath file to predict y_feature'
    dataset = prepare_dataset(read_dataset(fpath), y_feature)
    X_train, X_test, y_train, y_test = split_dataset(dataset, y_feature)

    X_train, X_test = scale_features(X_train, X_test)
    predictions = run_model(X_train, y_train).predict(X_test)
    return classification_report(y_test, predictions)

if __name__ == '__main__':
    print(run('data/LoanStats3a.csv', 'loan_status_Charged Off'))
