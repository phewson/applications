from pathlib import Path
from course.utils import load_pg_data, find_project_root
from course.supervised_classification.classify import fit_qda, fit_lda
from course.supervised_classification.predict import pred_lda, pred_qda
from course.supervised_classification.metrics import metric_report_lda, metric_report_qda
from course.supervised_classification.split_test_train import test_and_train


def task_check_cache():
    def check_cache():
        """Check cache folder exists"""
        models_path = Path("data_cache/models")
        models_path.mkdir(parents=True, exist_ok=True)
    return {
      'actions': [check_cache]
    }


def task_energy_metrics_new():
    def energy_metrics_new():
        with open('sql/energy.sql', 'r') as file:
            QUERY = file.read()
        df = load_pg_data(QUERY)
        df.to_csv('data_cache/energy.csv', index = False)
    return {
        'actions': [energy_metrics_new],
        'file_dep': ['sql/energy.sql'],
        'targets': ['data_cache/energy.csv'],
    }


def task_test_and_train():
    return {
        'actions': [test_and_train],
        'file_dep': ['data_cache/energy.csv', 'course/supervised_classification/test_train.py'],
        'targets': ['data_cache/energy_X_train.csv', 'data_cache/energy_y_train.csv',
                    'data_cache/energy_X_test.csv', 'data_cache/energy_y_test.csv'],
    }


def task_fit_lda():
    return {
      'actions': [fit_lda],
      'file_dep': ['data_cache/energy_X_train.csv', 'data_cache/energy_y_train.csv',
                   'course/supervised_classification/classify.py'],
      'targets': ['data_cache/models/lda_model.joblib']
    }


def task_fit_qda():
    return {
      'actions': [fit_qda],
      'file_dep': ['data_cache/energy_X_train.csv', 'data_cache/energy_y_train.csv', 
                   'course/supervised_classification/classify.py'],
      'targets': ['data_cache/models/qda_model.joblib']
    }


def task_predict_lda():
    return {
      'actions': [pred_lda],
      'file_dep': ['data_cache/models/lda_model.joblib', 'data_cache/energy_X_test.csv',
                   'course/supervised_classification/predict.py'],
      'targets': ['data_cache/models/lda_y_pred.csv']
    }     


def task_predict_qda():
    return {
      'actions': [pred_qda],
      'file_dep': ['data_cache/models/qda_model.joblib', 'data_cache/energy_X_test.csv',
                   'course/supervised_classification/predict.py'],
      'targets': ['data_cache/models/qda_y_pred.csv']
    }   


def task_metrics_lda():
    return {
      'actions': [metric_report_lda],
      'file_dep': ['data_cache/models/lda_y_pred.csv', 'data_cache/energy_y_test.csv',
                   'course/supervised_classification/metrics.py'],
      'targets': ['data_cache/vignettes/supervised_classification/lda.csv']
    }   
        
        
def task_metrics_qda():
    return {
      'actions': [metric_report_qda],
      'file_dep': ['data_cache/models/qda_y_pred.csv', 'data_cache/energy_y_test.csv',
      'course/supervised_classification/metrics.py'],
      'targets': ['data_cache/vignettes/supervised_classification/qda.csv']
    }   
