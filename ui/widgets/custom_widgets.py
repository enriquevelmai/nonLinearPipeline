import PySide2.QtWidgets
import typing


class kComboBox(PySide2.QtWidgets.QComboBox):
    def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...):
        super().__init__(parent)


class kCheckBox(PySide2.QtWidgets.QCheckBox):
    def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...):
        super().__init__(parent)


class kLineEdit(PySide2.QtWidgets.QLineEdit):
    def __init__(self, arg__1: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...):
        super().__init__(arg__1, parent)


class kTableWidget(PySide2.QtWidgets.QTableWidget):
    def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...):
        super().__init__(parent)


class kPushButton(PySide2.QtWidgets.QPushButton):
    def __init__(self, icon: PySide2.QtGui.QIcon, text: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...):
        super().__init__(icon, text, parent)
