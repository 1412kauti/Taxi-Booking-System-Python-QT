# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_Driver_First_Name.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 120, 341, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.change_Driver_FirstName_Label = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.change_Driver_FirstName_Label.setObjectName("change_Driver_FirstName_Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.change_Driver_FirstName_Label)
        self.ChangeFirstNameBtn = QtWidgets.QPushButton(Form)
        self.ChangeFirstNameBtn.setGeometry(QtCore.QRect(130, 190, 141, 23))
        self.ChangeFirstNameBtn.setObjectName("ChangeFirstNameBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "New First Name :"))
        self.ChangeFirstNameBtn.setText(_translate("Form", "Change First Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())