
from INF.Training.load_data import load_data
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder
from yellowbrick.classifier import ROCAUC, PrecisionRecallCurve


def show_confusion_matrix(model):
    x_train, x_test, y_train, y_test = load_data()
    predictions = model.predict(x_test)
    cm = confusion_matrix(y_test, predictions, labels=model.classes_)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=model.classes_
    )
    disp.plot()
    plt.show()


def show_ROCAUC(model):
    x_train, x_test, y_train, y_test = load_data()

    le = LabelEncoder()
    y_test = le.fit_transform(y_test)

    visualizer = ROCAUC(model, binary=True)
    visualizer.fit(x_train, y_train)
    visualizer.score(x_test, y_test)
    visualizer.show()


def show_PrecisionRecallCurve(model):
    x_train, x_test, y_train, y_test = load_data()

    le = LabelEncoder()
    y_test = le.fit_transform(y_test)

    viz = PrecisionRecallCurve(model)
    viz.fit(x_train, y_train)
    viz.score(x_test, y_test)
    viz.show()
