
""" TODO: write doc
"""

import sys
import os
import fnmatch
import re
from PyQt4 import QtGui, QtCore, QtSql, uic
from src.gui import Ui_SearchReadMeDialog


class SearchReadMeDialog(QtGui.QDialog):
    def __init__(self, parent=None, rootFolder='.'):
        super(self.__class__, self).__init__()
        QtGui.QDialog.__init__(self, parent)

        self.ui = Ui_SearchReadMeDialog.Ui_Ui_SearchReadMeDialog()
        self.ui.setupUi(self)

        self.setModal(True)
        self.dat = []
        self.searchReadMe(rootFolder)


    def writeLine(self, line):
        self.ui.plainTextEdit.appendPlainText(line)

    def getValues(self):
        return self.dat

    def searchReadMe(self, rootFolder):
        filenames = []
        dir_path = str(rootFolder).rstrip('/')

        self.writeLine("Starting recursive walk")
        self.writeLine("Searching for ReadMe...")

        # walk recursively
        for root, dirnames, fnames in os.walk(dir_path):
            for fname in fnmatch.filter(fnames, '[Rr]ead[Mm]e.txt'):
                filenames.append(os.path.join(root, fname))
                self.writeLine('ReadMe found: ' + filenames[-1])

        self.writeLine("Walked through the whole tree")
        self.writeLine("Parsing files...")
        for fileCurr in filenames:
            try:
                f = open(fileCurr, 'r')
            except IOError:
                self.writeLine('Could not open ' + fileCurr)

            with f:
                self.writeLine('Processing ' + fileCurr)
                currentDat = self.parseFile(f)
                # clean up the text
                print('----OLD----')
                print(currentDat)
                currentDatCorr = {}

                currentDatCorr.update({key.rstrip('\r'): val.rstrip('\n').rstrip('\r') for key, val in currentDat.items()})     # TODO: can do better than just rstrip(r)...
                print('----NEW----')
                print(currentDatCorr)
                currentDatCorr['path'] = os.path.abspath(os.path.dirname(fileCurr))
                self.dat.append(currentDatCorr)
                self.writeLine('Done.')


    def parseFile(self, f):
        dat = {}
        header_re = re.compile(r'^ *#+ *([^\n]+?) *#* *(?:\n+|$)', flags=re.UNICODE)
        header_name = ''
        for line in f:
            match = header_re.match(line.decode('utf-8'))
            if match: # we are at a header of a section
                header_name = match.group(1).decode('utf-8')
                dat[header_name] = ''
            else:
                if header_name != '': # we are in a section
                    dat[header_name] += line.decode('utf-8')
        return dat
