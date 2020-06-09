import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QDate
import sqlite3


class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 550, 300) #Fenster initialisieren, Größe festlegen
        self.setWindowTitle("Fahrtenbuch") #Titel für das Fenster festlegen
        self.elements()

    def elements(self):
        #Dieses Objekt enhält alle Steuerelemente der Software.
        '''Es sind enthalten:
        - Kilometerstand*
        - Datum *
        - Preis *
        - Preis pro Liter *
        - Typ
        Die mit Stern markierten Elemente müssen bei Eintrag in die Datenbank vorhanden sein
        '''
        vertikalerAbstand = 40

        #Kilometerstand
        self.lineInKilometerstand = QtGui.QLineEdit(self)
        self.lineInKilometerstand.move(50, 10)
        self.lineInKilometerstand.resize(200, 30)
        self.lineInKilometerstand.setPlaceholderText("Kilometerstand")
        self.lineInKilometerstand.setValidator(QtGui.QIntValidator(0, 1000000, self))
        self.lineInKilometerstand.editingFinished.connect(self.textAngepasst)

        #Datum
        self.lineInDatum = QtGui.QCalendarWidget(self)
        self.lineInDatum.setFirstDayOfWeek(self, QtDayOfWeek=1)
        self.lineInDatum.setGridVisible(True)
        #self.lineInDatum = QtGui.QLineEdit(self)
        self.lineInDatum.move(300, 10)
        self.lineInDatum.resize(200, 30)
        #self.lineInDatum.setPlaceholderText("Datum")
        '''
        !!!!Das Datum kann aktuell auch falsch eingelesen werden! Es findet keine Filterung statt!!!
        '''
        #lineInDatum.setValidator(QtGui.QIntValidator(0, 100000, self))
        #QtGui.QRegExpValidator("(0[1-9]|[12][0-9]|3[01])/(0[1-9]|[1][0-2])/(19[0-9][0-9]|20[0-9][0-9])")


        #Preis
        self.lineInPreis = QtGui.QLineEdit(self)
        self.lineInPreis.move(50, 10+(1*vertikalerAbstand))
        self.lineInPreis.resize(200, 30)
        self.lineInPreis.setPlaceholderText("Betrag gezahlt")


        #Preis pro Liter
        self.lineInGrundpreis = QtGui.QLineEdit(self)
        self.lineInGrundpreis.move(50, 10+(2*vertikalerAbstand))
        self.lineInGrundpreis.resize(200, 30)
        self.lineInGrundpreis.setPlaceholderText("Grundpreis in €/l")

        self.btnSchreibeDB = QtGui.QPushButton("Schreibe in DB", self)
        self.btnSchreibeDB.clicked.connect(self.schreibeDatenbank)
        self.btnSchreibeDB.move(50, 10+(4*vertikalerAbstand))
        self.btnSchreibeDB.resize(150, 30)

        #Button zum Lesen der DB Daten
        self.btnLeseDB = QtGui.QPushButton("Lese DB", self)
        self.btnLeseDB.clicked.connect(self.schreibeDatenbank)
        self.btnLeseDB.move(50, 10+(5*vertikalerAbstand))
        self.btnLeseDB.resize(150, 30)



        self.show()


    
    def textAngepasst(self):
        feldLeer = False
        print(self.lineInKilometerstand.text())

    def leseDatenbank(self):
        self.databaseConnection()


    def schreibeDatenbank(self):

        '''

        global kilometerstandAlt
        global feldLeer
        #kilometerstandAlt = self.lineInKilometerstand.text()
        if (kilometerstandAlt == self.lineInKilometerstand.text()) or feldLeer == True:
            print("Fehler. Neue Daten eingeben")
        else:
            print(kilometerstandAlt)
            print("test")
            kilometerstandAlt = self.lineInKilometerstand.text()
        
        '''

        self.databaseConnection()
        self.databaseCreateTable()

        kilometerstand = self.lineInKilometerstand.text()
        datum = self.lineInDatum.text()
        preis = self.lineInPreis.text()
        literpreis = self.lineInGrundpreis.text()
        typ = "test"

        if kilometerstand == "" or datum == "" or typ == "":
            print("Fehler")
        else:
            self.databaseConnection()
            #sql_schreibe_daten=
            self.zeiger.execute("""
                INSERT INTO tanken
                    VALUES (?,?,?,?,?)
                    """,
                    (kilometerstand, datum, preis, literpreis, typ))

            self.verbindung.commit()
            self.verbindung.close()



    def databaseConnection(self):

        self.verbindung = sqlite3.connect("/home/benedikt/Schreibtisch/digitalesFahrtenbuch/DB/data.db")
        self.zeiger = self.verbindung.cursor()

    def databaseCreateTable(self):

        sql_tabelle_erstellen = """
        CREATE TABLE IF NOT EXISTS tanken (
            kilometerstand INTEGER,
            datum DATE,
            preis REAL,
            literpreis REAL,
            typ VARCHAR(20)
        );
        """

        self.zeiger.execute(sql_tabelle_erstellen)
        self.verbindung.commit()

        self.zeiger.execute("SELECT * FROM tanken")
        inhalt = self.zeiger.fetchall()
        print(inhalt)
        
        
        self.verbindung.close()
        


        


def run():
    
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())



feldLeer = True
kilometerstandAlt = 0
run()
