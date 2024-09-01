# ///////////////////////////////////////////////////////////////
# Developer: Mehdi Sameni
# Designer: Mehdi Sameni
# PyQt6
# Python 3.10
# other module : perlin_noise
# ///////////////////////////////////////////////////////////////


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QColor
from Virtual_Keyboard import VirtualKeyboard


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 300)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        layout = QVBoxLayout(self)
        frame = QFrame(self)
        layoutF = QVBoxLayout(frame)
        layout.addWidget(frame)
        keyboard = VirtualKeyboard(
                                 w=800,
                                 h=270,
                                 title='Keyboard',
                                 bgColor='#7E7E7E',
                                 btnColor='rgba(120,120,120, 50)',
                                 btnHoverColor='rgba(120,120,120, 150)',
                                 btnPressColor='gray',
                                 btnTextColor='#222324',
                                 textEditColor='#E3F7FF',
                                 textEditBgColor='#00567a',
                                 textEditFontSize=18,
                                 btnRadius=18)
        layoutF.addWidget(keyboard)
        keyboard.signal_text.connect(self.func_lineEdit)

    def func_lineEdit(self, event):
        print(event)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
