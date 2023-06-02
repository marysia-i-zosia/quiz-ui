from PyQt5 import QtWidgets

from main import Ui_MainWindow

from marysia import pytania, a, b, c, odp

global ui
global i
global poprawne
poprawne=0
i = 0


def sprawdz_a():
    if odp[i] == 'a':
        dobra_odpowiedz()
    else:
        zla_odpowiedz()


def sprawdz_b():
    if odp[i] == 'b':
        dobra_odpowiedz()
    else:
        zla_odpowiedz()


def sprawdz_c():
    if odp[i] == 'c':
        dobra_odpowiedz()
    else:
        zla_odpowiedz()


def zla_odpowiedz():
    widocznosc()
    ui.label_ocena.setText(f'Wybrałeś złą odpowiedź. Poprawna odpowiedź to {odp[i]}.')
    ui.label_zla.setVisible(True)


def dobra_odpowiedz():
    widocznosc()
    ui.label_ocena.setText('Brawo wybrałes dobrą odpowiedż.')
    global poprawne
    poprawne=poprawne+1
    ui.label_dobre.setVisible(True)

def widocznosc(widoczne=False):
    ui.button_a.setVisible(widoczne)
    ui.button_b.setVisible(widoczne)
    ui.button_c.setVisible(widoczne)
    ui.label_ocena.setVisible(not widoczne)
    ui.button_nastepne.setVisible(not widoczne)


def nastepne_pytanie():
    global i
    global poprawne
    ui.label_dobre.setVisible(False)
    ui.label_zla.setVisible(False)
    if i < 5:
        widocznosc(True)
        i = i + 1
        ui.label_pytanie.setText(pytania[i])
        ui.label_odpowiedz_a.setText(a[i])
        ui.label_odpowiedz_b.setText(b[i])
        ui.label_odpowiedz_c.setText(c[i])
    else:
        ui.label_wynik.setText(f'Twój wynik to {poprawne}/{i+1}')
        ui.button_nastepne.setVisible(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    ui.label_ocena.setVisible(False)
    ui.label.setVisible(True)
    ui.label_zla.setVisible(False)
    ui.label_dobre.setVisible(False)
    ui.button_nastepne.setVisible(False)
    ui.label_wynik.setText('')

    ui.label_pytanie.setText(pytania[i])
    ui.label_odpowiedz_a.setText(a[i])
    ui.label_odpowiedz_b.setText(b[i])
    ui.label_odpowiedz_c.setText(c[i])

    ui.button_a.clicked.connect(sprawdz_a)
    ui.button_b.clicked.connect(sprawdz_b)
    ui.button_c.clicked.connect(sprawdz_c)

    ui.button_nastepne.clicked.connect(nastepne_pytanie)

    MainWindow.show()
    sys.exit(app.exec_())
