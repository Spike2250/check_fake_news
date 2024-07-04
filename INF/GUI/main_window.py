 
from PySide6 import QtWidgets, QtCore, QtGui

from INF.GUI.UI import window
from INF.Training.training import (
    is_there_saved_model,
    load_trained_model,
    save_trained_model,
    get_trained_model
)
from INF.Training.load_data import prepare_text
from INF.Training.testing import (
    show_confusion_matrix,
    show_ROCAUC,
    show_PrecisionRecallCurve,
    show_DiscriminationThreshold
)


class Ui_FakeNews_window(QtWidgets.QMainWindow,
                         window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.set_connections()
        self.check_saved_model()

    def set_connections(self):
        self.train_model.clicked.connect(self.train_new_model)
        self.save_model.clicked.connect(self.save_current_model)
        self.load_model.clicked.connect(self.load_model_from_pc)
        self.check_news.clicked.connect(self.check_news_text)
        self.show_conf_matrix.clicked.connect(self.show_model_conf_matrix)
        self.show_rocauc_info.clicked.connect(self.show_rocauc)
        self.show_prc.clicked.connect(self.show_PRC)
        self.show_dt.clicked.connect(self.show_DT)
        self.result.textChanged.connect(self.set_result_style)

    def check_saved_model(self):
        if is_there_saved_model():
            self.load_model.setEnabled(True)

    def train_new_model(self):
        self.model, self.accuracy, self.report = get_trained_model()
        self.set_success_status_model_text()
        self.set_report_info()
        self.save_model.setEnabled(True)
        self.set_enabled_buttons()

    def load_model_from_pc(self):
        self.model, self.accuracy, self.report = load_trained_model()
        self.set_success_status_model_text()
        self.set_report_info()
        self.set_enabled_buttons()

    def set_enabled_buttons(self):
        self.check_news.setEnabled(True)
        self.show_conf_matrix.setEnabled(True)
        self.show_rocauc_info.setEnabled(True)
        self.show_prc.setEnabled(True)
        self.show_dt.setEnabled(True)

    def set_success_status_model_text(self):
        text = f"Model ready to work!\n"\
               f"Accuracy on test data: {self.accuracy} %"
        self.model_status.setText(text)

    def set_report_info(self):
        self.process.setText(self.report)

    def save_current_model(self):
        save_trained_model(
            self.model,
            self.accuracy,
            self.report
        )
        self.check_saved_model()
        self.process.setText("Model saved successfully!")


    def check_news_text(self):
        self.result.setText(' ')

        text = self.news_text.toPlainText()
        if text:
            self.result.setText('Waiting...')
            self.set_result_style()

            result = self.model.predict(
                prepare_text(text)
            )[0]
            self.result.setText(result)

    def set_result_style(self):
        match self.result.text():
            case 'REAL':
                self.result.setStyleSheet('''
                    color: White;
                    background-color: rgba(50, 98, 115, 150);
                    border: 2px solid rgba(92, 158, 173, 255);
                ''')
            case 'FAKE':
                self.result.setStyleSheet('''
                    color: White;
                    background-color: rgba(112, 38, 50, 150);
                    border: 2px solid rgba(112, 38, 50, 255);
                ''')
            case _:
                self.result.setStyleSheet('''
                    color: rgba(50, 98, 115, 255);
                    background-color: transparent;
                    border: none;
                ''')

    def show_model_conf_matrix(self):
        show_confusion_matrix(self.model)

    def show_rocauc(self):
        show_ROCAUC(self.model)

    def show_PRC(self):
        show_PrecisionRecallCurve(self.model)

    def show_DT(self):
        show_DiscriminationThreshold(self.model)
