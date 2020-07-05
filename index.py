from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType

library = loadUiType('library.ui')
app = QApplication([])
library = uic.loadUi('library.ui')
library.show()
sys.exit(app.exec_())