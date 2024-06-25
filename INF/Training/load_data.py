import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


DATA_FILE = 'fake_news.csv'


def load_dataset():
    # загружаем датасет
    df = pd.read_csv(f"data/{DATA_FILE}")
    return df


def get_vectorizer():
    return TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5,
    )


def split_and_prepare_dataset(df):
    # делим на данные для тренировки и тестов
    x_train, x_test, y_train, y_test = train_test_split(
        df['text'], df['label'],
        test_size=0.1, random_state=13)

    # применяем TfidfVectorizer для перевода строк в числа
    vectorizer = get_vectorizer()
    x_train = vectorizer.fit_transform(x_train)
    x_test = vectorizer.transform(x_test)

    return x_train, x_test, y_train, y_test


def prepare_text(text):
    vectorizer = get_vectorizer()
    return vectorizer.fit_transform([text])


def load_data():
    return split_and_prepare_dataset(
        load_dataset()
    )


if __name__ == '__main__':
    print(load_dataset()[0][4])
    print(load_dataset()[2][4])
