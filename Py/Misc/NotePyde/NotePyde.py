'''
NotePyde
by Aaron Aikman
first created 2018 05 24
A simple notepad application

TODO add drag and drop
TODO add runner options (including option for base path)
TODO add syntax highlighting
TODO add tabs
TODO add comparison
TODO add an About
'''

import sys
from PyQt4 import QtGui, uic

# TODO fix extra imports
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(r'F:\Database\Satchel\Works\Scripting\MiscScripts\Py\Misc\NotePyde\NotePyde.ui', self)

        self.currentFile = None

        self.actionOpen.triggered.connect(self.getFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveAs)
        self.actionNew.triggered.connect(self.newFile)
        self.show()


    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
            'c:\\',"Text files (*.txt)")
        self.le.setPixmap(QPixmap(fname))


    def getFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        filenames = QStringList()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.currentFile = filenames[0]
            f = open(self.currentFile, 'r')

            with f:
                data = f.read()
                # print data
                self.textEdit.setText(data)


    def saveFile(self, doDialog = 0):
        if doDialog:
            filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        else:
            if self.currentFile:
                filename = self.currentFile
            else:
                filename = None

        if filename:
            newText = self.textEdit.toPlainText()
            with open(filename, 'w') as f:
                # f.write(newText) # Writes the whole file at once
                for line in str(newText).splitlines():
                    line += '\n'
                    f.write(line)
                # TODO Fix this adding and extra newline at the end
        else:
            self.saveAs()

    def saveAs(self):
        self.saveFile(1)

    def savePrompt(self):
        reply = QMessageBox.question(self, 'Save?',
                        'Do you want to save before proceeding?', QMessageBox.Yes, QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.saveFile()


    def newFile(self):
        self.savePrompt()
        self.textEdit.clear()
        self.currentFile = None



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())