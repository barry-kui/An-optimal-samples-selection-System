import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import S1
import S2
import S3
import S4
import S5
import S6

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = S6.Ui_S6()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
