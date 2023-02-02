from datetime import datetime, timedelta
import sys
import PyQt6
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.uic import loadUi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        loadUi("window.ui", self)

        self.setWindowTitle("Anwesendheit")

        #Ui elements
        # inputs
        self.lineEdit1 = self.findChild(QtWidgets.QLineEdit, "sDate")
        self.lineEdit2 = self.findChild(QtWidgets.QLineEdit, "eDate")
        self.lineEdit3 = self.findChild(QtWidgets.QLineEdit, "fDays")
        self.lineEdit4 = self.findChild(QtWidgets.QLineEdit, "ffDays")

        # buttons append, delete and calculate
        self.btn_1 = self.findChild(QtWidgets.QPushButton, "cal")
        self.btn_1.clicked.connect(self.calculate)
        # label

        self.labelinfo = self.findChild(QtWidgets.QLabel, "labelInfo")

        #widgets fürs plotten
        self.plot1 = self.findChild(QtWidgets.QWidget, "plot1")
        self.plot1.setLayout(QtWidgets.QVBoxLayout())
        self.plot2 = self.findChild(QtWidgets.QWidget, "plot2")
        self.plot3 = self.findChild(QtWidgets.QWidget, "plot3")


        # calculations for remaining days------------------------------------------------------------------------

        # Abfrage des Datums, an dem Sie die Schule begonnen haben
        start_date_str = "2022-09-10"
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

        # Abfrage des Enddatums der Schule
        end_date_str = "2024-05-10"
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Berechnung der Anzahl der Tage bis heute und der verbleibenden Tage
        today = datetime.now()
        days_passed = (today - start_date).days
        remaining_days = (end_date - today).days

        # Tage gesamt
        total_days = (end_date - start_date).days

        print("Sie haben die Schule am", start_date.strftime('%d.%m.%Y'), "begonnen.")
        print(days_passed)
        print(remaining_days)
        print(total_days)

        # Daten für den Plot vorbereiten
        days1 = [days_passed, remaining_days]
        labels2 = ['Vergangene Tage', 'verbleibende Tage']

        self.figure1 = Figure()
        # Erstellen Sie eine neue Axes-Instanz und fügen Sie sie der Figure hinzu
        # Erstellen Sie eine neue Axes-Instanz und fügen Sie sie der Figure hinzuu
        self.ax = self.figure1.add_subplot()

        # Erstellen Sie eine neue FigureCanvasQTAgg-Instanz und fügen Sie sie dem frame hinzu
        self.canvas = FigureCanvasQTAgg(self.figure1)
        self.plot1.layout().addWidget(self.canvas)
        self.ax.pie(days1, labels=labels2, autopct='%1.1f%%')
        self.figure1.canvas.draw()



        # calculations for complete days----------------------------------------------------------------------------

        weekend_days = 174
        ferien = 93
        werktage = total_days - weekend_days - ferien
        Feiertage = 9

        # Daten für den Plot vorbereiten
        days2 = [weekend_days, ferien, werktage, Feiertage]
        labels2 = ['Wochend Tage', 'Ferientage', 'Schultage', 'Feiertage']


        self.figure2 = Figure()
        # Erstellen Sie eine neue Axes-Instanz und fügen Sie sie der Figure hinzu
        # Erstellen Sie eine neue Axes-Instanz und fügen Sie sie der Figure hinzuu
        self.ax = self.figure2.add_subplot()

        # Erstellen Sie eine neue FigureCanvasQTAgg-Instanz und fügen Sie sie dem frame hinzu
        self.canvas = FigureCanvasQTAgg(self.figure2)
        self.plot1.layout().addWidget(self.canvas)
        self.ax.pie(days2, labels=labels2, autopct='%1.1f%%')
        self.figure2.canvas.draw()


    def calculate(self):
        print("hallo")

        #calculations for all charts

        # Input of start date of school
        start_date_str = self.lineEdit1.text()
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

        # Input of end date of school
        end_date_str = self.lineEdit2.text()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Input of number of absent days
        absent_days_str = self.lineEdit3.text()
        absent_days = int(absent_days_str)

        # Input of number of holiday days
        holiday_days_str = self.lineEdit4.text()
        holiday_days = int(holiday_days_str)

        # total days
        total_days = (end_date - start_date).days

        # Calculation of number of weekend days
        weekend_days = 0
        for day in range(total_days):
            if (start_date + timedelta(day)).weekday() >= 5:
                weekend_days += 1

        # Calculation of attendance percentage
        attendance_days = total_days - absent_days - holiday_days - weekend_days
        attendance = attendance_days / total_days * 100

        # Data preparation for pie chart
        days3 = [attendance_days, absent_days]
        labels3 = ['anwesend', 'abwesend']


        print("Total days between", start_date.strftime('%Y-%m-%d'), "and", end_date.strftime('%Y-%m-%d'), ":",
              total_days)
        print("Number of absent days:", absent_days)
        print("Number of holiday days:", holiday_days)
        print("Number of weekend days:", weekend_days)
        print("Attendance percentage:", attendance, "%")

        self.figure2 = Figure()
        # Erstellen Sie eine neue Axes-Instanz und fügen Sie sie der Figure hinzu
        # Erstellen Sie eine neue Axes-Instanz und fügen Sie sie der Figure hinzuu
        self.ax = self.figure2.add_subplot()

        # Erstellen Sie eine neue FigureCanvasQTAgg-Instanz und fügen Sie sie dem frame hinzu
        self.canvas = FigureCanvasQTAgg(self.figure2)
        self.plot1.layout().addWidget(self.canvas)
        self.ax.pie(days3, labels=labels3, autopct='%1.1f%%')
        self.figure2.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




