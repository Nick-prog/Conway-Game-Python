# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Conway.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import ConwayGOL.game as game
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PIL import Image as im

count = 0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        '''
        Method to generate the interface objects.
        '''
        # Dialog box specifications.
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 482)
        Dialog.setWindowIcon(QIcon('TAMUK Logo 3.jpg'))
        Dialog.setFixedSize(650, 480)

        # Dimension and input labels (x and y) specifications.
        self.dim_label = QtWidgets.QLabel(Dialog)
        self.dim_label.setGeometry(QtCore.QRect(480, 260, 61, 16))
        self.dim_label.setObjectName("dim_label")
        self.x_label = QtWidgets.QLabel(Dialog)
        self.x_label.setGeometry(QtCore.QRect(430, 283, 21, 20))
        self.x_label.setObjectName("x_label")
        self.y_label = QtWidgets.QLabel(Dialog)
        self.y_label.setGeometry(QtCore.QRect(500, 280, 21, 20))
        self.y_label.setObjectName("y_label")
        self.x_input = QtWidgets.QLineEdit(Dialog)
        self.x_input.setGeometry(QtCore.QRect(450, 280, 41, 20))
        self.x_input.setObjectName("x_input")
        self.y_input = QtWidgets.QLineEdit(Dialog)
        self.y_input.setGeometry(QtCore.QRect(520, 280, 41, 20))
        self.y_input.setObjectName("y_input")

        # Grid label specifications. Used to display the generated grid.
        self.grid_view = QtWidgets.QLabel(Dialog)
        self.grid_view.setGeometry(QtCore.QRect(300, 60, 256, 192))
        self.grid_view.setObjectName("grid_view")
        
        # Generation label specifications. Displays current generation.
        self.generations = QtWidgets.QLabel(Dialog)
        self.generations.setGeometry(QtCore.QRect(290, 260, 100, 21))
        self.generations.setObjectName("generations")

        # Button layout. Next button starts/iterates the program. Reset button resets current inputs and outputs.
        self.nextButton = QtWidgets.QPushButton(Dialog)
        self.nextButton.setGeometry(QtCore.QRect(420, 320, 75, 23))
        self.nextButton.setObjectName("nextButton")
        self.resetButton = QtWidgets.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(510, 320, 75, 23))
        self.resetButton.setObjectName("resetButton")

        self.count = 0 # Number of button clicks.
        # Connects buttons to their designated methods.
        self.nextButton.clicked.connect(self.next_click)
        self.resetButton.clicked.connect(self.reset_click)

        # Large info box browser's specifications.
        self.infoBrowser = QtWidgets.QTextBrowser(Dialog)
        self.infoBrowser.setGeometry(QtCore.QRect(20, 30, 221, 341))
        self.infoBrowser.setObjectName("infoBrowser")
        
        # Specifications for the line used to seperate the infoBrowser from the rest.
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(260, 30, 20, 431))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Title labels specifications. Displays name of the program for user's to see.
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(360, 30, 111, 16))
        self.title_label.setObjectName("title_label")
        self.info_label = QtWidgets.QLabel(Dialog)
        self.info_label.setGeometry(QtCore.QRect(290, 320, 101, 16))
        self.info_label.setObjectName("info_label")

        # Passes the created Dialog box to another method for text inputs.
        self.retranslateUi(Dialog)
        # Connects everything to the Dialog box tab.
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def next_click(self):
        '''
        Method for the nextButton.
        Acquires the inputted values and generates a grid on first click.
        Iterates through the game of life logic for every click afterwards.
        '''
        _translate = QtCore.QCoreApplication.translate # Gives access to setText on generated Dialog box.

        if(self.count == 0): # For the first time click.
            # Acquire user inputs.
            row_x = int(self.x_input.text())
            col_y = int(self.y_input.text())
            # Generate a grid and update the approprate labels.
            self.current_gen = game.generate_grid(row_x, col_y)
            self.generations.setText(_translate("Dialog", f"Generations: {self.count}"))
            self.info_label.setText(_translate("Dialog", "Game start!"))
            self.count += 1

            # Multiple the generated grid by 255 for greyscale image. Generate image with the PIL library and save it as 'grid_img.png'.
            gen_img = self.current_gen[:,:]*255
            im.fromarray(gen_img.astype('uint8'), mode='L').save("grid_img.png")

            # Set the created image at 'grid_img.png' and scale based off the images ratio.
            pixmap = QPixmap('grid_img.png')
            self.grid_view.setPixmap(pixmap)
            self.grid_view.setScaledContents(True)

        else: # For every click after the first one.
            # Generate the next grid for a given generation. Update the appropriate labels.
            next_gen = game.GameOfLife(self.current_gen)
            self.current_gen = next_gen.copy()
            self.generations.setText(_translate("Dialog", f"Generations: {self.count}"))
            self.count += 1

            # Multiple the generated grid by 255 for greyscale image. Generate image with the PIL library and save it as 'grid_img.png'.
            gen_img = self.current_gen[:,:]*255
            im.fromarray(gen_img.astype('uint8'), mode='L').save("grid_img.png")

            # Set the created image at 'grid_img.png' and scale based off the images ratio.
            pixmap = QPixmap('grid_img.png')
            self.grid_view.setPixmap(pixmap)
            self.grid_view.setScaledContents(True)
        
    def reset_click(self):
        '''
        Method for the resetButton.
        Resets appropriate labels back to the original state.
        Informs the user of this change and removes the last generated grid_view.
        '''
        _translate = QtCore.QCoreApplication.translate # Gives access to setText on generated Dialog box.

        # Informs the user of the current changes. Resets the generations and grid_view back to the original state.
        self.info_label.setText(_translate("Dialog", "Reset...click Next!"))
        self.count = 0
        self.generations.setText(_translate("Dialog", f"Generations: {self.count}"))
        self.grid_view.clear()

    def retranslateUi(self, Dialog):
        '''
        Method to set any kind of text to generated objects.
        '''
        _translate = QtCore.QCoreApplication.translate # Gives access to setText on generated Dialog box.

        # Set the appropriate text for all relevant labels. Pass HTML text to the text browser for style integration.
        Dialog.setWindowTitle(_translate("Dialog", "Conway GOL"))
        self.dim_label.setText(_translate("Dialog", "Dimensions"))
        self.x_label.setText(_translate("Dialog", "X:"))
        self.y_label.setText(_translate("Dialog", "Y:"))
        self.x_input.setText(_translate("Dialog", "4"))
        self.y_input.setText(_translate("Dialog", "5"))
        self.generations.setText(_translate("Dialog", f"Generations: {self.count}"))
        self.nextButton.setText(_translate("Dialog", "Next"))
        self.resetButton.setText(_translate("Dialog", "Reset"))
        self.infoBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">The mathematician Conway imagined a game, called </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">game of life</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">, which considered cells that are susceptible to reproduce, disappear, or survive when they obey certain rules. These cells are represented by elements on a grid of squares, where a grid has an arbitrary size. Thus, each cell (except those on the boundaries of the grid) is surrounded by eight squares that contain other cells. The rules are stated as follows:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-weight:600;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:8pt;\">      </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-weight:600; font-style:italic;\">Survival:</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-weight:600;\"> </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">Each cell that has two or three adjacent cells </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">survives </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">until the next generation.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-weight:600;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:8pt;\">      </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-weight:600; font-style:italic;\">Death:</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> Each cell that has at least four adjacent cells </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">disappears</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> (or </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">dies</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">) by </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">overpopulation</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">. Also, each cell that has at most one adjacent cell </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">dies</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> by </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">isolation</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-weight:600;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:8pt;\">      </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-weight:600; font-style:italic;\">Birth:</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> Each </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">empty</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> square (</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">i.e.</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">, </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">dead </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\">cell) that is adjacent to exactly three cells gives </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt; font-style:italic;\">birth</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> to a new cell for the next generation.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.title_label.setText(_translate("Dialog", "Conway\'s Game of Life"))
        self.info_label.setText(_translate("Dialog", "Click Next to start..."))