# Virtual Keyboard With PyQt6

![](https://img.shields.io/badge/Developer-MehdiSameni-blue)
![](https://img.shields.io/badge/PyQt-Version6-green)
![](https://img.shields.io/badge/Python-3.8|3.9|3.10|3.11|3.12-gold)
([https://devguide.python.org/versions/])

## How to use:

- import
```python
  from VirtualKeyboard import VirtualKeyboard
```

- call
```python
  keyboard = VirtualKeyboard()
  keyboard.signal_lineedit_content.connect(self.function)
  keyboard.exec()
```


- excute
```python
  import sys
  frpm PyQt6 import QtWidgets, QtGui, QtCore
  from VirtualKeyboard import VirtualKeyboard
  
  class MainWidget(QtWidgets.QWidget)
    def __init__(self)
      super().__init__(self)
  
      keyboard = VirtualKeyboard()
      keyboard.signal_lineedit_content.connect(self.my_function)
      keyboard.exec()

    def my_function(self, text):
      print(f"{text=}")
```


##
![img_1](image/img_1.png)
##
![img_2](image/img_2.png)
