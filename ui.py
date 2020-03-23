#!/usr/bin/python3

import sys
import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QKeyEvent, QKeySequence

class UIMainWindow(object):
    def __init__(self, window):
        self.window = window
        self.clip_board = QApplication.clipboard()
        self._init_ui()
        self._init_shortcut()

    def _init_ui(self):
        self.window.setObjectName("MainWindow")
        self.window.resize(600, 480)
        self.central_widget = QtWidgets.QWidget(self.window)
        self.central_widget.setObjectName("centralWidget")

        self.text_input = QtWidgets.QPlainTextEdit(self.central_widget)
        self.text_temp = QtWidgets.QTextBrowser(self.central_widget)
        self.text_output = QtWidgets.QTextEdit(self.central_widget)
        self.btn_append_clear = QtWidgets.QPushButton(self.central_widget)
        self.btn_append_clear.setText("Append and Clear")
        self.btn_append_clear.setMaximumWidth(180)
        self.btn_copy_clear = QtWidgets.QPushButton(self.central_widget)
        self.btn_copy_clear.setText("Copy and Clear")
        self.btn_copy_clear.setMaximumWidth(180)

        self.horizon_layout_btn1 = QtWidgets.QHBoxLayout()
        self.horizon_layout_btn1.addWidget(self.btn_append_clear)
        self.horizon_layout_btn2 = QtWidgets.QHBoxLayout()
        self.horizon_layout_btn2.addWidget(self.btn_copy_clear)

        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.addWidget(self.text_input, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.text_temp, 1, 0, 1, 1)
        self.grid_layout.addLayout(self.horizon_layout_btn1, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.text_output, 0, 1, 2, 1)
        self.grid_layout.addLayout(self.horizon_layout_btn2, 2, 1, 1, 1)
        
        self.window.setCentralWidget(self.central_widget)
        
        self._set_connect()
        

    def _init_shortcut(self):
        copy_action = QtWidgets.QAction(self.window)
        copy_action.setObjectName('action_copy')
        copy_action.triggered.connect(self._copy_text)
        copy_action.setShortcut(QKeySequence(QKeySequence.Copy))
        self.window.addAction(copy_action)

        paste_action = QtWidgets.QAction(self.window)
        paste_action.setObjectName('action_paste')
        paste_action.triggered.connect(self._paste_text)
        paste_action.setShortcut(QKeySequence(QKeySequence.Paste))
        self.window.addAction(paste_action)

        self.text_input.installEventFilter(self.window)
        self.text_temp.installEventFilter(self.window)
        self.text_output.installEventFilter(self.window)

        def mainwindow_eventFilter(watched, event):
            if event.type() == QEvent.KeyPress:
                key_event = QKeyEvent(event)
                if key_event.modifiers() == Qt.ControlModifier:
                    if key_event.key() == Qt.Key_C:
                        self._copy_text()
                        return True
                    if key_event.key() == Qt.Key_V:
                        self._paste_text()
                        return True
            return QtWidgets.QMainWindow.eventFilter(self.window, watched, event)
        self.window.eventFilter = mainwindow_eventFilter
        

    def _copy_text(self):
        text = self.text_output.toPlainText()
        self.clip_board.setText(text)


    def _paste_text(self):
        text = self.clip_board.text()
        self.text_input.appendPlainText(text)


    def _set_connect(self):
        self.text_input.textChanged.connect(self._handle_input)
        self.btn_append_clear.clicked.connect(self._append_clear)
        self.btn_copy_clear.clicked.connect(self._copy_clear)


    def _handle_input(self):
        text = self.text_input.toPlainText()
        text = re.compile(u'\s+').sub(' ', text)
        text = text.strip()
        self.text_temp.setText(text)


    def _append_clear(self):
        text = self.text_temp.toPlainText()
        self.text_output.append(text)
        self.text_output.setFocus()
        self.text_input.clear()


    def _copy_clear(self):
        self._copy_text()
        self.text_output.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UIMainWindow(main_window)
    ui.window.show()

    sys.exit(app.exec_())
