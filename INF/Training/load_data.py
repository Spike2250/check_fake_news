import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


DATA_FILE = 'fake_news.csv'


def load_dataset():
    # загружаем датасет
    df = pd.read_csv(f"data/{DATA_FILE}")
    # print(df.describe())
    return df


def split_dataset(df):
    return train_test_split(
        df['text'],
        df['label'],
        test_size=0.1, 
        random_state=13
    )


def get_vectorizer():
    return TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5,
    )


def split_and_prepare_dataset(df):
    # делим на данные для тренировки и тестов
    x_train, x_test, y_train, y_test = split_dataset(df)

    # применяем TfidfVectorizer для перевода строк в числа
    vectorizer = get_vectorizer()
    x_train = vectorizer.fit_transform(x_train)
    x_test = vectorizer.transform(x_test)

    return x_train, x_test, y_train, y_test


def prepare_text(text):
    data = split_dataset(load_dataset())
    vectorizer = get_vectorizer()
    vectorizer.fit_transform(data[0])
    return vectorizer.transform([text])


def load_data():
    return split_and_prepare_dataset(
        load_dataset()
    )
