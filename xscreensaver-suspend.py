#!/usr/bin/env python3
#
# xscreensaver-disable
# Copyright (C) 2016 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
import subprocess
from PyQt5 import QtWidgets
from PyQt5 import QtCore


def quit_clicked():
    QtCore.QCoreApplication.quit()


def suspend_xscreensaver():
    subprocess.check_call(['xscreensaver-command', '-deactivate'])
    print("xscreensaver suspended")
    return True


def main():
    app = QtWidgets.QApplication(sys.argv)

    timer = QtCore.QTimer()
    timer.timeout.connect(suspend_xscreensaver)
    timer.start(1000 * 60)

    label = QtWidgets.QLabel("XScreensaver has been temporarily suspended.");
    label.setWordWrap(True)

    button = QtWidgets.QPushButton("Stop Suspension")
    button.clicked.connect(quit_clicked)

    vbox = QtWidgets.QVBoxLayout()

    vbox.addWidget(label)
    vbox.addWidget(button)

    main_widget = QtWidgets.QWidget()
    main_widget.setLayout(vbox)

    window = QtWidgets.QMainWindow()
    window.setCentralWidget(main_widget)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


# EOF #
