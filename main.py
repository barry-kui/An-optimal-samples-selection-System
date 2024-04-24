import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


import P2
import S3
import S4
import S5
import P11

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = P2.Ui_P2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
