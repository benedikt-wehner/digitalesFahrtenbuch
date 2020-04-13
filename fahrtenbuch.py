import sys
from PyQt4 import QtGui, QtCore
import sqlite3


class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 300, 300) #Fenster initialisieren, Größe festlegen
        self.setWindowTitle("Fahrtenbuch") #Titel für das Fenster festlegen
        self.elements()

    def elements(self):
        #Dieses Objekt enhält alle Steuerelemente der Software.
        '''Es sind enthalten:
        - Kilometerstand
        - Datum *
        - Preis *
        - Preis pro Liter *
        - Typ
        Die mit Stern markierten Elemente müssen bei Eintrag in die Datenbank vorhanden sein
        '''
        vertikalerAbstand = 40

        #Kilometerstand
        lineInKilometerstand = QtGui.QLineEdit(self)
        lineInKilometerstand.move(50, 10)
        lineInKilometerstand.resize(200, 30)
        lineInKilometerstand.setPlaceholderText("Kilometerstand")
        lineInKilometerstand.setValidator(QtGui.QIntValidator(0, 100000, self))

        #Datum
        lineInDatum = QtGui.QLineEdit(self)
        lineInDatum.move(50, 10+vertikalerAbstand)
        lineInDatum.resize(200, 30)
        lineInDatum.setPlaceholderText("Datum")
        '''
        !!!!Das Datum kann aktuell auch falsch eingelesen werden! Es findet keine Filterung statt!!!
        '''
        #lineInDatum.setValidator(QtGui.QIntValidator(0, 100000, self))
        #QtGui.QRegExpValidator("(0[1-9]|[12][0-9]|3[01])/(0[1-9]|[1][0-2])/(19[0-9][0-9]|20[0-9][0-9])")


        #Preis
        lineInPreis = QtGui.QLineEdit(self)
        lineInPreis.move(50, 10+(2*vertikalerAbstand))
        lineInPreis.resize(200, 30)
        lineInPreis.setPlaceholderText("Betrag gezahlt")


        #Preis pro Liter
        lineInGrundpreis = QtGui.QLineEdit(self)
        lineInGrundpreis.move(50, 10+(3*vertikalerAbstand))
        lineInGrundpreis.resize(200, 30)
        lineInGrundpreis.setPlaceholderText("Grundpreis in €/l")




        self.show()

def run():
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

run()
