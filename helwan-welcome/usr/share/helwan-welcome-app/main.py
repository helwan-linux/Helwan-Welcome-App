#!/usr/bin/env python3
# CREATED BY Saeed Badrelden <saeedbadrelden2021@gmail.com>

import sys
from PyQt5.QtWidgets import QApplication
from welcome_app import WelcomeApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeApp()
    window.show()
    sys.exit(app.exec_())
