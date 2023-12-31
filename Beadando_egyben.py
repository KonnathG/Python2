import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
from PyQt5.QtCore import QTimer


class Atvalto_api:
    @staticmethod
    def valuta_valto(kezdo_valuta, cel_valuta):
        api_url = f"https://api.exchangerate-api.com/v4/latest/{kezdo_valuta}"
        valasz = requests.get(api_url)
        adat = valasz.json()
        return adat['rates'][cel_valuta]


class Atvalto_program(QWidget):
    def __init__(self):
        super().__init__()

        self.kezdo_valuta_label = QLabel("Kezdő valuta:")
        self.cel_valuta_label = QLabel("Cél valuta:")
        self.atvalto_ertek_label = QLabel("Átváltási érték:")

        osszes_valuta = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD",
                         "NOK", "MXN", "SGD", "HKD", "TRY", "INR", "BRL", "ZAR", "RUB", "HUF"]

        self.kezdo_valuta_combobox = QComboBox()
        self.cel_valuta_combobox = QComboBox()
        osszes_valuta.sort()

        self.kezdo_valuta_combobox.addItems(osszes_valuta)
        self.cel_valuta_combobox.addItems(osszes_valuta)

        layout = QVBoxLayout()
        layout.addWidget(self.kezdo_valuta_label)
        layout.addWidget(self.kezdo_valuta_combobox)
        layout.addWidget(self.cel_valuta_label)
        layout.addWidget(self.cel_valuta_combobox)
        layout.addWidget(self.atvalto_ertek_label)

        self.setLayout(layout)

        self.kezdo_valuta_combobox.currentIndexChanged.connect(self.atvalto_ertek_frissites)
        self.cel_valuta_combobox.currentIndexChanged.connect(self.atvalto_ertek_frissites)

        self.idozito = QTimer(self)
        self.idozito.timeout.connect(self.atvalto_ertek_frissites)
        self.idozito.start(10000)
        self.atvalto_ertek_frissites()

    def atvalto_ertek_frissites(self):
        kezdo_valuta = self.kezdo_valuta_combobox.currentText()
        cel_valuta = self.cel_valuta_combobox.currentText()
        atvalto_ertek = Atvalto_api.valuta_valto(kezdo_valuta, cel_valuta)

        self.kezdo_valuta_label.setText(f"Kezdő valuta: {kezdo_valuta}")
        self.cel_valuta_label.setText(f"Cél valuta: {cel_valuta}")
        self.atvalto_ertek_label.setText(f"Átváltási érték ({kezdo_valuta} - {cel_valuta}): {atvalto_ertek}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Atvalto_program()
    window.setWindowTitle("Valutaváltó")
    window.setGeometry(800, 400, 300, 200)
    window.show()
    sys.exit(app.exec_())
