from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import json
import os

from INF.Training.load_data import load_data


MODEL_NAME = 'fake_news_model'

MODEL_PATH = 'models'
JSON_PATH = 'related_data'

model_name = f"{MODEL_PATH}/{MODEL_NAME}.pkl"
file_name = f"{MODEL_PATH}/{JSON_PATH}/{MODEL_NAME}.json"


def create_model():
    return PassiveAggressiveClassifier(
        C=0.1,
        random_state=5
    )


def get_trained_model():
    model = create_model()
    x_train, x_test, y_train, y_test = load_data()

    # обучаем модель
    model.fit(x_train, y_train)

    # проверяем на тестовых данных
    test_pred = model.predict(x_test)
    # определяем точность
    accuracy = round((accuracy_score(y_test, test_pred) * 100), 2)
    # формируем отчет
    report = classification_report(y_test, test_pred)

    return model, accuracy, report


def save_trained_model(model, accuracy='', report=''):
    # сохраняем модель
    joblib.dump(model, model_name)
    # сохраняем доп.данные
    related_data = {
        'accuracy': accuracy,
        'report': report
    }
    with open(file_name, 'w') as file:
        json.dump(related_data, file, indent=2)


def load_trained_model():
    # проверяем наличие модели и доп.данных
    if is_there_saved_model():
        # загружаем модель
        model = joblib.load(model_name)
        # загружаем доп.данные
        with open(file_name, 'r') as file:
            related_data = json.load(file)
        accuracy = related_data['accuracy']
        report = related_data['report']

        return model, accuracy, report
    return None

def is_there_saved_model():
    return os.path.exists(model_name) and os.path.exists(file_name)


if __name__ == '__main__':
    get_trained_model()
