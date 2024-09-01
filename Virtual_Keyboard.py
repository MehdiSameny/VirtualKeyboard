# ///////////////////////////////////////////////////////////////
# Developer: Mehdi Sameni
# Designer: Mehdi Sameni
# PyQt6
# Python 3.10
# ///////////////////////////////////////////////////////////////



from PyQt6 import QtCore, QtGui, QtWidgets
from functools import partial


class VirtualKeyboard(QtWidgets.QDialog):
    #signal_lineedit_content = QtCore.pyqtSignal(str)
    signal_text = QtCore.pyqtSignal(str)

    def __init__(self,
                 w=800,
                 h=270,
                 title='Keyboard',
                 bgColor='#7E7E7E',
                 btnColor='rgba(120,120,120, 50)',
                 btnHoverColor='#fff',
                 btnPressColor='gray',
                 btnTextColor='#fff',
                 textEditColor='#E3F7FF',
                 textEditBgColor='#00567a',
                 textEditFontSize=18,
                 btnRadius=18):
        super().__init__()
        self.setObjectName("Form")
        self.resize(w, h)
        self.setWindowTitle(title)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowMaximizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowMinimizeButtonHint)

        self.verticalLayout_main = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_main.setObjectName("verticalLayout_main")

        self.lineEdit_Content = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Content.sizePolicy().hasHeightForWidth())
        self.lineEdit_Content.setSizePolicy(sizePolicy)
        self.lineEdit_Content.setMaximumSize(QtCore.QSize(16777215, 45))
        self.lineEdit_Content.setObjectName("lineEdit_FT")
        self.lineEdit_Content.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Content.setFocus()
        self.verticalLayout_main.addWidget(self.lineEdit_Content)

        self.setStyleSheet(f"""
            QLineEdit{{
                color: {textEditColor};
                background-color: {textEditBgColor};
                border: 0px solid {bgColor};
                border-radius: 5px;
                font-size: {textEditFontSize}px;
                font-style: bold;
            }}
            QPushButton{{
                color: {btnTextColor};
                border: 1px solid gray;
                border-radius: {btnRadius}px;
                background-color: {btnColor};
            }}
            QPushButton:hover{{
                background-color: {btnHoverColor};
            }}
            QPushButton:pressed{{
                background-color: {btnPressColor};
            }}
        """)

        self.frame_keyboard = QtWidgets.QFrame(self)
        self.frame_keyboard.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_keyboard.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.kb_addButton(self.frame_keyboard, True)
        self.verticalLayout_main.addWidget(self.frame_keyboard)
        QtCore.QMetaObject.connectSlotsByName(self)

    def kb_addButton(self, Forms, status):
        self.shift_active = False
        self.caps_active = False
        self.btn_line = []
        self.horizontalLayout = []
        layouts = ["layout_line_1", "layout_line_2", "layout_line_3", "layout_line_4"]
        self.linesSmall = [["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "<--"],
                      ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "LOCK"],
                      ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ENTER"],
                      ["z", "x", "c", "v", "b", "n", "SPACE", "m", ",", ":", "\\", "SHIFT"]]
        self.linesBig = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "<--"],
                    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "LOCK"],
                    ["A", "S", "D", "F", "G", "H", "J", "K", "L", "ENTER"],
                    ["Z", "X", "C", "V", "B", "N", "SPACE", "M", "<", ">", "/", "SHIFT"]]
        lines = self.linesBig if status else self.linesSmall

        self.verticalLayout_kb = QtWidgets.QVBoxLayout(Forms)
        self.verticalLayout_kb.setObjectName("verticalLayout_kb")
        count = 0

        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)

        for l, line in enumerate(lines):
            self.horizontalLayout.append(l)
            self.horizontalLayout[l] = QtWidgets.QHBoxLayout()
            self.horizontalLayout[l].setSpacing(2)
            self.horizontalLayout[l].setObjectName(layouts[l])
            self.verticalLayout_kb.addLayout(self.horizontalLayout[l])
            for i, name in enumerate(line):
                self.btn_line.append(l)
                self.btn_line[count] = QtWidgets.QPushButton(Forms)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
                sizePolicy.setHeightForWidth(self.btn_line[count].sizePolicy().hasHeightForWidth())
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHorizontalStretch(0)
                self.btn_line[count].setSizePolicy(sizePolicy)
                self.btn_line[count].setMinimumSize(QtCore.QSize(1, 1))
                self.btn_line[count].setFont(font)
                self.btn_line[count].setObjectName(name)
                self.btn_line[count].setText(name)
                self.btn_line[count].setAutoRepeat(True)
                self.btn_line[count].clicked.connect(partial(self.kb_selectBtn, btn=[name, count]))
                self.horizontalLayout[l].addWidget(self.btn_line[count])
                count += 1

        for index, obj in enumerate(self.btn_line):
            if obj.objectName() == "LOCK" or obj.objectName() == "SHIFT":
                self.btn_line[index].setCheckable(True)

            if obj.objectName() == "SPACE":
                obj.setMinimumWidth(140)

    def kb_capsLock(self, status):
        count = 0
        for index, obj in enumerate(self.btn_line):
            if index < len(self.linesBig[0]):
                count = index
                self.btn_line[index].setText(self.linesBig[0][count] if status else self.linesSmall[0][count])
            if len(self.linesBig[0]) <= index < (len(self.linesBig[0]) + len(self.linesBig[1])):
                count = index - len(self.linesBig[0])
                self.btn_line[index].setText(self.linesBig[1][count] if status else self.linesSmall[1][count])
            if len(self.linesBig[0]) + len(self.linesBig[1]) <= index < (len(self.linesBig[0]) + len(self.linesBig[1]) + len(self.linesBig[2])):
                count = index - (len(self.linesBig[0]) + len(self.linesBig[1]))
                self.btn_line[index].setText(self.linesBig[2][count] if status else self.linesSmall[2][count])
            if index >= (len(self.linesBig[0]) + len(self.linesBig[1]) + len(self.linesBig[2])):
                count = index - (len(self.linesBig[0]) + len(self.linesBig[1]) + len(self.linesBig[2]))
                self.btn_line[index].setText(self.linesBig[3][count] if status else self.linesSmall[3][count])

    def kb_selectBtn(self, **name):
        try:
            key_name = name['btn'][0]
            key_index = name['btn'][1]

            if key_name == "SPACE":
                seq = self.lineEdit_Content.text() + " "
                self.lineEdit_Content.setText(seq)
                return
            if key_name == "<--":
                seq = list(str(self.lineEdit_Content.text()))
                res = seq[:len(seq) - 1]
                s = ''.join(res)
                self.lineEdit_Content.setText(s)
                return
            elif key_name == "LOCK":
                self.caps_active = True if self.btn_line[key_index].isChecked() else False
                self.kb_capsLock(False if self.btn_line[key_index].isChecked() else True)
                return
            elif key_name == "SHIFT":
                self.shift_active = True
                self.kb_capsLock(False)
                return
            elif key_name == "ENTER":
                self.close()
            else:
                if self.shift_active:
                    self.lineEdit_Content.setText(str(self.lineEdit_Content.text()) + key_name.lower())
                    self.shift_active = False
                    for index, obj in enumerate(self.btn_line):
                        if obj.objectName() == "SHIFT":
                            obj.setChecked(False)
                            obj.setChecked(False)
                    self.kb_capsLock(True)
                else:
                    if self.caps_active:
                        self.lineEdit_Content.setText(str(self.lineEdit_Content.text()) + key_name.lower())
                    else:
                        self.lineEdit_Content.setText(str(self.lineEdit_Content.text()) + key_name)
                        self.kb_capsLock(True)

            self.lineEdit_Content.setFocus()
            self.signal_text.emit(self.lineEdit_Content.text())
        except Exception as e:
            print(e)


    def set_default_text(self, text):
        self.lineEdit_Content.setText(text)

    def set_holder_text(self, text):
        self.lineEdit_Content.setPlaceholderText(text)

    def keyPressEvent(self, event):
        # بررسی اینکه کلید فشرده شده، کلید Enter است
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.close()

    def closeEvent(self, event):
        self.lineedit_content.emit(self.lineEdit_Content.text())
        print("[KEYBOARD] :", self.lineEdit_Content.text())
        event.accept()



