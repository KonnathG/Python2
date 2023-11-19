Konnáth Gergő Devizaárfolyam-átváltó programja

Ez a projekt egy egyszerű devizaárfolyam-átváltó alkalmazást valósít meg, amely lehetővé teszi a felhasználók számára a valós idejű árfolyamok ellenőrzését és devizaátváltást.

Feladat rövid leírása
Az alkalmazás egy grafikus felhasználói felülettel rendelkezik, amelyben a felhasználók kiválaszthatják az alap- és cél valutát. Az alkalmazás az exchangerate-api.com API-t használja az árfolyamok lekérdezéséhez, és rendszeresen frissíti azokat.

Modulok
sys: Az alkalmazás futtatásához és befejezéséhez szükséges modul.
requests: HTTP kérések küldésére szolgáló modul.
PyQt5.QtWidgets: Grafikus felhasználói felület elemeiért felelős PyQt5 modul.
PyQt5.QtCore azon belül is a QTimer: Ez teszi lehetővé az időzített frissítést

Függvények az Atvalto_api osztályban:
valuta_valto(kezdo_valuta, cel_valuta): A devizaárfolyam lekérdezéséért felelős függvény, amely az API-t használja.

Függvények az Atvalto_program osztályban:
__init__(self): Az alkalmazás inicializálását végző függvény, amely felépíti a grafikus felhasználói felületet és beállítja az eseménykezelőket.

atvalto_ertek_frissites(self): Az árfolyamok frissítését és az ablakban történő megjelenítést végző függvény.

Használati útmutató
Használat előtt telepítsük a PyQt5 és a requests modulokat a Pycharmban levő terminál segítségével a következő paranccsal : pip install PyQt5 requests
Indítsd el az alkalmazást a Beadando_egyben.py fájl segítségével vagy a külön bontott indítóval ami a Beadando_program.py nevet kapta
Válaszd ki az alap- és célnemű valutákat a legördülő listákból.
Figyeld az árfolyamokat és az azonnali átváltást az alkalmazás ablakában.

Kellemes használatot!

Konnáth Gergő
