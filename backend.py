from PyQt5 import QtCore, QtWidgets
import frontend as main
import sys
import random
import string

class mainwindow:

    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        self.ui = main.Ui_Form()
        self.ui.setupUi(Form)
        self.regenerate()
        Form.show()
        sys.exit(app.exec_())

    def update(self):
        lengt = self.ui.slider.value()
        self.ui.number.setText(str(lengt))
        return lengt

    def check_checkboxes(self):
        self.checked_checkboxes = []

        if self.ui.uppercase.isChecked():
            self.checked_checkboxes.append("uppercase")
        if self.ui.lowercase.isChecked():
            self.checked_checkboxes.append("lowercase")
        if self.ui.digit.isChecked():
            self.checked_checkboxes.append("digits")
        if self.ui.specSymbol.isChecked():
            self.checked_checkboxes.append("symbols")
        return self.checked_checkboxes


    def generate(self,length,checked_checkboxes):
        character_sets = {
            "lowercase": string.ascii_lowercase,
            "uppercase": string.ascii_uppercase,
            "digits": string.digits,
            "symbols": string.punctuation
        }

        # Combine the selected character sets
        available_characters = "".join(character_sets[option] for option in checked_checkboxes)

        # Generate password components directly from available characters
        password_components = random.choices(available_characters, k=length)
        random.shuffle(password_components)
        password = "".join(password_components)
        return password


    def password(self):
        self.update()
        checked_options = self.check_checkboxes()
        password_length = self.ui.slider.value()
        password = self.generate(password_length,checked_options)
        self.ui.Output.setText(password)

    def regenerate(self):
        self.ui.uppercase.stateChanged.connect(self.password)
        self.ui.lowercase.stateChanged.connect(self.password)
        self.ui.digit.stateChanged.connect(self.password)
        self.ui.specSymbol.stateChanged.connect(self.password)
        self.ui.slider.valueChanged.connect(self.password)
        self.ui.retry.clicked.connect(self.password)


