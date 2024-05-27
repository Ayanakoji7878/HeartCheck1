# напиши здесь код третьего экрана приложения 3
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont 
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit
      
class FinalWin(QWidget):
    def __init__(self):
        self.initUI()
        self.set_appear()
        self.show()
    def initUI(self):
    self.workh_name = QLabel(txt_workheart)
    self.index_text = QLabel(txt_index)
    self.layout_line = QVBoxLayout()
    self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
    self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)