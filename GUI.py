import os
import random
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QMessageBox, QListWidget, QSpinBox, QStackedWidget, QRadioButton, QScrollArea, QScrollBar, QGridLayout,QButtonGroup
from function import *
from PyQt5.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Optimal Sample Selection System')
        self.setWindowIcon(QIcon('./resources/可莉.ico'))
        self.resize(1280, 960)
        self.stacked_widget = QStackedWidget(self)
        self.select_screen = SelectionPage(self)
        self.file_screen = FilePage(self)
        '''
        self.function_screen = FCPage(self)
        self.position_number_screen = PNPage(self)
        self.position_range_number_screen = PNRPage(self)
        self.select_position_screen = SPPage(self)
        '''
        self.stacked_widget.addWidget(self.select_screen)
        self.stacked_widget.addWidget(self.file_screen)

        '''
        self.stacked_widget.addWidget(self.function_screen)
        self.stacked_widget.addWidget(self.position_number_screen)
        self.stacked_widget.addWidget(self.position_range_number_screen)
        self.stacked_widget.addWidget(self.select_position_screen)
        '''
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)


    def go_to_Select_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_File_page(self):
        self.stacked_widget.setCurrentIndex(1)
        #print(os.listdir("./Data"))

    def go_to_function_choice(self):
        self.stacked_widget.setCurrentIndex(2)

    def go_to_position_number_page(self):
        self.stacked_widget.setCurrentWidget(3)

    def go_to_position_range_number_page(self):
        self.stacked_widget.setCurrentIndex(4)

    def go_to_selection_position_page(self):
        self.stacked_widget.setCurrentIndex(5)

class SelectionPage(QWidget):

    def __init__(self,main_widow):
        super().__init__()
        self.main_widow = main_widow
        self.P1gui()

    def P1gui(self):
        self.setWindowTitle("Optimal Sample Selection System")
        self.resize(1280,960)
        self.choice = 0
        self.Print_init = 0
        #layout
        main_layout = QVBoxLayout()
        m_n_layout = QHBoxLayout()
        k_j_s_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        dialog_layout = QHBoxLayout()
        result_layout = QHBoxLayout()
        UserInput_layout = QHBoxLayout()


        main_layout.addWidget(QLabel("Optimal Sample Selection System"),0,Qt.AlignHCenter)
        #get m,n
        m_n_layout.addWidget(QLabel("m:"),0,Qt.AlignRight)
        self.input_m = QSpinBox(self)
        m_n_layout.addWidget(self.input_m)
        self.input_m.setRange(45,54)
        m_n_layout.addWidget(QLabel("45 ≤ m ≤ 54"))
        m_n_layout.addWidget(QLabel("n:"),0,Qt.AlignRight)
        self.input_n = QSpinBox(self)
        self.input_n.setRange(7,25)
        m_n_layout.addWidget(self.input_n)
        m_n_layout.addWidget(QLabel("7 ≤ n ≤ 25"))
        m_n_layout.addWidget(QLabel(" "))
        m_n_layout.addWidget(QLabel(" "))
        m_n_layout.addWidget(QLabel(" "))

        #get k
        k_j_s_layout.addWidget(QLabel("k:"),0,Qt.AlignRight)
        self.input_k = QSpinBox(self)
        k_j_s_layout.addWidget(self.input_k)
        self.input_k.setRange(4, 7)
        k_j_s_layout.addWidget(QLabel("4 ≤ k ≤ 7"))
        #get j
        k_j_s_layout.addWidget(QLabel("j:"),0,Qt.AlignRight)
        self.input_j = QSpinBox(self)
        k_j_s_layout.addWidget(self.input_j)

        k_j_s_layout.addWidget(QLabel("s ≤ j ≤ k"))
        #get s
        k_j_s_layout.addWidget(QLabel("s:"),0,Qt.AlignRight)
        self.input_s = QSpinBox(self)
        k_j_s_layout.addWidget(self.input_s)
        self.input_s.setRange(3, 7)
        k_j_s_layout.addWidget(QLabel("3 ≤ s ≤ 7"))

        self.input_j.setRange(self.input_s.value(), self.input_k.value())
        self.input_s.valueChanged.connect(self.Update_j_range)
        self.input_k.valueChanged.connect(self.Update_j_range)

        #Random n & input n
        self.Random_n = QRadioButton(self)
        self.Random_n.setText("Random n")
        button_layout.addWidget(self.Random_n)

        #Input n
        self.User_Input_n = QRadioButton(self)
        self.User_Input_n.setText("Input n")
        button_layout.addWidget(self.User_Input_n)
        self.User_Input_n.toggled.connect(self.Random_n_value)
        self.Random_n.toggled.connect(self.Random_n_value)

        #Store DB
        Store_DB = QPushButton(self)
        Store_DB.setText("Store DB")
        Store_DB.clicked.connect(self.sort_DB)
        button_layout.addWidget(Store_DB)


        #Execute
        Execute = QPushButton(self)
        Execute.setText("Execute")
        Execute.clicked.connect(self.execute_click)
        button_layout.addWidget(Execute)


        #Dellte
        self.Delete = QPushButton(self)
        self.Delete.setText("Delete")
        self.Delete.clicked.connect(self.Clean_up)
        button_layout.addWidget(self.Delete)

        main_layout.addLayout(m_n_layout)
        main_layout.addLayout(k_j_s_layout)
        main_layout.addLayout(button_layout)

        #Userinput
        main_layout.addWidget(QLabel("User input n"))
        self.userlist = QLineEdit(self)
        self.input_str = self.userlist.text()
        self.input_list = self.input_str.split(',')

        UserInput_layout.addWidget(self.userlist)
        main_layout.addLayout(UserInput_layout)

        #time
        main_layout.addWidget(QLabel("Time Cost"))
        self.time_cost = QLabel("Time Cost result")
        main_layout.addWidget(self.time_cost)

        #Dialog
        dialog_layout.addWidget(QLabel("Value Input"))
        dialog_layout.addWidget(QLabel("Result"))
        main_layout.addLayout(dialog_layout)

        #result
        IVarea = QScrollArea()
        self.input_value = QListWidget()
        IVarea.setWidget(self.input_value)
        IVarea.setWidgetResizable(True)
        result_layout.addWidget(IVarea)

        Rarea = QScrollArea()
        self.result = QListWidget()
        Rarea.setWidget(self.result)
        Rarea.setWidgetResizable(True)
        result_layout.addWidget(Rarea)

        #button
        Print = QPushButton(self)
        Print.setText("Print")
        Print.clicked.connect(self.generate_n_group)
        Next = QPushButton(self)
        Next.setText("Next")
        Next.clicked.connect(self.main_widow.go_to_File_page)
        result_layout.addWidget(Print)
        result_layout.addWidget(Next,0,Qt.AlignBottom)
        main_layout.addLayout(result_layout)
        self.setLayout(main_layout)

    def Update_j_range(self):
        self.input_j.setRange(self.input_s.value(), self.input_k.value())

    '''
    def test(self):
        a= list(random_samples(45,7))
        for i in range(len(a)):
            self.input_value.addItem(str(a[i]))
    '''
    def Clean_up(self):
        self.input_value.clear()
        self.result.clear()
        self.execute_times=0
    def generate_n_group(self):
        self.input_value.clear()
        m = self.input_m.value()
        n = self.input_n.value()
        self.execute_times = 0
        self.Print_init = 1
        try:
            if self.choice == 0:
                raise ValueError
            if self.choice == 1:
                self.input_str = self.userlist.text()
                self.input_list = self.input_str.split(',')
                self.n_group = self.input_list
                for j in range(len(self.n_group)):
                    if self.n_group[j] > 54 or not isinstance(self.n_group[j],int) or self.n_group[j] == 0:
                        raise TypeError
                print(self.input_str)
            elif self.choice == 2:
                self.n_group = random_samples(m,n)
            for i in range(len(self.n_group)):
                input_value = f"{i+1}#: {self.n_group[i]}\n"
                self.input_value.addItem(str(input_value))
        except ValueError:
            QMessageBox.warning(self, "error", "Please choice a method first")
        except TypeError:
            QMessageBox.warning(self, "error", "Please input the number in range 1-54 or in int")


    def execute_click(self):
        self.result.clear()
        k = self.input_k.value()
        j = self.input_j.value()
        s = self.input_s.value()
        try:
            if self.Print_init == 0:
                raise ValueError
            n_group = self.n_group

            start_time = time.time()
            self.optimal_group = select_k(n_group,k,j,s)
            end_time = time.time()
            self.execute_times += 1

            for group in range(len(self.optimal_group)):
                optimal_value = f"{group+1}: {self.optimal_group[group]}"
                self.result.addItem(str(optimal_value))
            self.final_result = str(f"{self.input_m.value()}-{self.input_n.value()}-{k}-{j}-{s}-{self.execute_times}-{group+1}")
            self.result.addItem(self.final_result)
            result = f"{end_time-start_time}s"
            self.time_cost.setText(result)
        except ValueError:
            QMessageBox.warning(self, "error", "Please Press Print to generate n_group first")

    def Random_n_value(self,checked):
        if checked:
            if self.Random_n.isChecked():
                self.choice = 2
                pass
            elif self.User_Input_n.isChecked():
                self.choice = 1


    def save_data(self,output,filename):
        filename = f"{filename}.txt"
        if not os.path.exists("Data") and os.getcwd() != "Data":
            os.makedirs("Data")
        os.chdir("Data")
        if os.path.exists(filename):
            os.remove(filename)
            with open(filename, 'a') as file:
                for group in output:
                    file.write(str(group)+'\n')
                self.update()

                os.chdir(os.path.dirname(os.getcwd()))
            QMessageBox.information(self,"Information",f"The data {filename} be replaces")
            return 0

        else:
            with open(filename, 'a') as file:
                for group in output:
                    file.write(str(group)+'\n')
                file.flush()
                os.chdir(os.path.dirname(os.getcwd()))
                QMessageBox.information(self, "Information", f"Data {filename} will be save")




    def sort_DB(self):
        self.save_data(self.optimal_group,self.final_result)




class FilePage(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.P2gui()

    def P2gui(self):
        main_layout = QVBoxLayout()
        dialog_layout = QHBoxLayout()
        firstlayer_layout = QHBoxLayout()
        secondlayer_layout = QHBoxLayout()
        thirdlayer_layout = QHBoxLayout()
        fourthlayer_layout = QHBoxLayout()
        output_layout = QHBoxLayout()
        button_layout = QVBoxLayout()

        #Title
        main_layout.addWidget(QLabel("Optimal Sample Selection System"), 0, Qt.AlignHCenter)

        #dialog
        dialog_layout.addWidget(QLabel("Data Base Resources"))
        self.Display = QPushButton()
        self.Display.setText("Display")
        dialog_layout.addWidget(self.Display)
        self.Display.clicked.connect(self.file_display)
        self.Delete = QPushButton()
        self.Delete.setText("Delete")
        self.Delete.clicked.connect(self.Delet_clicked)
        dialog_layout.addWidget(self.Delete)
        main_layout.addLayout(dialog_layout)


        #firstlayer
        self.file1 = QRadioButton()
        self.file2 = QRadioButton()
        self.file3 = QRadioButton()
        self.file1.clicked.connect(self.file_clicked)
        self.file2.clicked.connect(self.file_clicked)
        self.file3.clicked.connect(self.file_clicked)
        firstlayer_layout.addWidget(self.file1)
        firstlayer_layout.addWidget(self.file2)
        firstlayer_layout.addWidget(self.file3)
        main_layout.addLayout(firstlayer_layout)

        #second
        self.file4 = QRadioButton()
        self.file5 = QRadioButton()
        self.file6 = QRadioButton()
        self.file4.clicked.connect(self.file_clicked)
        self.file5.clicked.connect(self.file_clicked)
        self.file6.clicked.connect(self.file_clicked)
        secondlayer_layout.addWidget(self.file4)
        secondlayer_layout.addWidget(self.file5)
        secondlayer_layout.addWidget(self.file6)
        main_layout.addLayout(secondlayer_layout)


        #third
        self.file7 = QRadioButton()
        self.file8 = QRadioButton()
        self.file9 = QRadioButton()
        self.file7.clicked.connect(self.file_clicked)
        self.file8.clicked.connect(self.file_clicked)
        self.file9.clicked.connect(self.file_clicked)
        thirdlayer_layout.addWidget(self.file7)
        thirdlayer_layout.addWidget(self.file8)
        thirdlayer_layout.addWidget(self.file9)
        main_layout.addLayout(thirdlayer_layout)

        #fourth
        self.file10 = QRadioButton()
        self.file11 = QRadioButton()
        self.file12 = QRadioButton()
        self.file10.clicked.connect(self.file_clicked)
        self.file11.clicked.connect(self.file_clicked)
        self.file12.clicked.connect(self.file_clicked)
        fourthlayer_layout.addWidget(self.file10)
        fourthlayer_layout.addWidget(self.file11)
        fourthlayer_layout.addWidget(self.file12)
        main_layout.addLayout(fourthlayer_layout)


        self.group = QButtonGroup()
        self.group.addButton(self.file1, 1)
        self.group.addButton(self.file2, 2)
        self.group.addButton(self.file3, 3)
        self.group.addButton(self.file4, 4)
        self.group.addButton(self.file5, 5)
        self.group.addButton(self.file6, 6)
        self.group.addButton(self.file7, 7)
        self.group.addButton(self.file8, 8)
        self.group.addButton(self.file9, 9)
        self.group.addButton(self.file10, 10)
        self.group.addButton(self.file11, 11)
        self.group.addButton(self.file12, 12)


        #output
        Rarea = QScrollArea()
        self.result = QListWidget()
        Rarea.setWidget(self.result)
        Rarea.setWidgetResizable(True)
        output_layout.addWidget(Rarea)


        #button
        Previous = QPushButton()
        Previous.setText("Previous")
        Previous.clicked.connect(self.main_window.go_to_Select_page)
        ReFliter = QPushButton()
        ReFliter.setText("ReFlash")
        ReFliter.clicked.connect(self.reflash)
        button_layout.addWidget(Previous)
        button_layout.addWidget(ReFliter)
        output_layout.addLayout(button_layout)
        main_layout.addLayout(output_layout)


        self.setLayout(main_layout)

    def show_file(self):
        os.chdir("Data")
        file_list = os.listdir('.')
        for i in range(len(file_list)):
            self.group.button(i+1).setText(str(file_list[i]))
        os.chdir(os.path.dirname(os.getcwd()))

    def file_clicked(self):
        self.button_name = self.sender().text()

    def file_display(self):
        self.result.clear()
        os.chdir("Data")
        file_path = f"{self.button_name}"
        try:
            with open(file_path, "r") as file:
                file_lines = file.readlines()
                file_lines = [line.strip() for line in file_lines]
                for line in range(len(file_lines)):
                    optimal_value = f"{line + 1}: {file_lines[line]}"
                    self.result.addItem(optimal_value)
            os.chdir(os.path.dirname(os.getcwd()))

        except FileNotFoundError:
            print("File")
        except Exception as e:
            print(f"File Error: {e}")
    def reflash(self):
        for i in range(0,12):
            self.group.button(i+1).setText(str(" "))
        self.show_file()
    def Delet_clicked(self):
        os.chdir("Data")
        file_path = f"{self.button_name}"
        if os.path.exists(file_path):
            os.remove(file_path)
        QMessageBox.information(self, "Information",f"{self.button_name}is delete")
        os.chdir(os.path.dirname(os.getcwd()))
        self.reflash()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())