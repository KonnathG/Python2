from Beadando_build import Atvalto_program
from PyQt5.QtWidgets import QApplication


def run_currency_converter_app():
    app = QApplication([])
    window = Atvalto_program()
    window.setWindowTitle("Valutaváltó")
    window.setGeometry(800, 400, 300, 200)
    window.show()
    app.exec_()


if __name__ == "__main__":
    run_currency_converter_app()
