import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer

class CurrencyConverter:
    @staticmethod
    def get_exchange_rate(base_currency, target_currency):
        api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(api_url)
        data = response.json()
        return data['rates'][target_currency]

class CurrencyConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.base_currency_label = QLabel("Base Currency:")
        self.target_currency_label = QLabel("Target Currency:")
        self.exchange_rate_label = QLabel("Exchange Rate:")

        # Lista az összes lehetséges valutáról
        all_currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "NOK", "MXN", "SGD", "HKD", "KRW", "TRY", "INR", "BRL", "ZAR", "RUB", "HUF"]

        self.base_currency_combobox = QComboBox()
        self.target_currency_combobox = QComboBox()

        # ABC sorrendbe rendezzük a valutákat
        all_currencies.sort()

        self.base_currency_combobox.addItems(all_currencies)
        self.target_currency_combobox.addItems(all_currencies)

        layout = QVBoxLayout()
        layout.addWidget(self.base_currency_label)
        layout.addWidget(self.base_currency_combobox)
        layout.addWidget(self.target_currency_label)
        layout.addWidget(self.target_currency_combobox)
        layout.addWidget(self.exchange_rate_label)

        self.setLayout(layout)

        self.base_currency_combobox.currentIndexChanged.connect(self.update_exchange_rate)
        self.target_currency_combobox.currentIndexChanged.connect(self.update_exchange_rate)

        # Frissíti az árfolyamot minden 10 másodpercben
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_exchange_rate)
        self.timer.start(10000)

        # Azonnali frissítés az indításkor
        self.update_exchange_rate()

        # Ablak ikonjának beállítása
        self.setWindowIcon(QIcon(QPixmap("icon.png")))  # Cseréld ki az elérési utat a tényleges kép elérési útjára

    def update_exchange_rate(self):
        base_currency = self.base_currency_combobox.currentText()
        target_currency = self.target_currency_combobox.currentText()
        exchange_rate = CurrencyConverter.get_exchange_rate(base_currency, target_currency)

        self.base_currency_label.setText(f"Base Currency: {base_currency}")
        self.target_currency_label.setText(f"Target Currency: {target_currency}")
        self.exchange_rate_label.setText(f"Exchange Rate ({base_currency} to {target_currency}): {exchange_rate}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverterApp()
    window.setWindowTitle("Currency Exchange Rate Converter")
    window.setGeometry(100, 100, 300, 200)
    window.show()
    sys.exit(app.exec_())
