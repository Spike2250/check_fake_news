
from INF.Training.load_data import load_data
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def print_model_info(model):
    x_train, x_test, y_train, y_test = load_data()
    predictions = model.predict(x_test)
    cm = confusion_matrix(y_test, predictions, labels=model.classes_)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=model.classes_
    )
    disp.plot()
    plt.show()
