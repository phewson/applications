import joblib
import pandas as pd
from course.utils import find_project_root


def predict(model_path, X_test_path, y_pred_path):
    model = joblib.load(model_path)
    X_test = pd.read_csv(X_test_path)
    """Form an object y_pred containing a list of your classifer predictions"""
    y_pred_series = pd.Series(y_pred, name='predicted_tenure')
    y_pred_series.to_csv(y_pred_path, index=False)


def pred_lda():
    base_dir = find_project_root()
    model_path = base_dir / 'data_cache' / 'models' / 'lda_model.joblib'
    X_test_path = base_dir / 'data_cache' / 'energy_X_test.csv'
    y_pred_path = base_dir / 'data_cache' / 'models' / 'lda_y_pred.csv'
    predict(model_path, X_test_path, y_pred_path)


def pred_qda():
    base_dir = find_project_root()
    model_path = base_dir / 'data_cache' / 'models' / 'qda_model.joblib'
    X_test_path = base_dir / 'data_cache' / 'energy_X_test.csv'
    y_pred_path = base_dir / 'data_cache' / 'models' / 'qda_y_pred.csv'
    predict(model_path, X_test_path, y_pred_path)
