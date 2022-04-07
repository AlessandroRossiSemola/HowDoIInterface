import imp
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QMainWindow, QApplication, QLineEdit, QPushButton,
                               QVBoxLayout, QHBoxLayout, QLabel, QWidget, QScrollArea)
from howdoi import howdoi

class AnswerArea(QScrollArea):
 
    def __init__(self):
        super().__init__()
        
        self.setWidgetResizable(True)

        layout = QVBoxLayout()
 
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignTop)
        self.label.setWordWrap(True)
 
        # add label to the layout
        layout.addWidget(self.label)
        
        # create widget and set layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)
 
    def setText(self, text):
        self.label.setText(text)

class HowDoIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("How Do I Interface")
        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()

        # create the output field
        self.scroll_label = AnswerArea()

        #create the input field
        self.input_line  = QLineEdit()

        #create the button search and set an event for click
        self.ask_button = QPushButton("Ask")
        self.ask_button.clicked.connect(self.click_on_ask_button)
        
        #create the button clear and set an event for click
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.click_on_clear_button)
        
        #create a lable and Font for the text befor the input field
        pre_input_label = QLabel("How do I")
        
        lable_font = pre_input_label.font()
        lable_font.setPointSize(10)
        pre_input_label.setFont(lable_font)

        # add widgets to Horizontal Layout
        horizontal_layout.addWidget(pre_input_label)
        horizontal_layout.addWidget(self.input_line)
        horizontal_layout.addWidget(self.ask_button)
        horizontal_layout.addWidget(self.clear_button)

        # add widgets and Horizontal Layout to Vertical Layout
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(self.scroll_label)

        # create widget and set layout
        widget_container = QWidget()
        widget_container.setMinimumSize(500,350)
        widget_container.setLayout(vertical_layout)
        self.setCentralWidget(widget_container)

    def click_on_ask_button(self):
        #read the input text
        input_text = self.input_line.text()
       
        #if string is empty show a error
        if len(input_text) == 0:
            self.scroll_label.setText('Insert a question')
            self.scroll_label.setStyleSheet("QLabel { color: red }")
        else:
            self.scroll_label.setText(howdoi.howdoi(input_text))
            self.scroll_label.setStyleSheet("QLabel { color: black }")
            
    def click_on_clear_button(self):
        self.input_line.clear()
        self.scroll_label.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = HowDoIWindow()
    window.show()

    app.exec_()