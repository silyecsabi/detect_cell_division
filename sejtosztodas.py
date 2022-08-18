# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sejtosztodasRbqQsm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(578, 575)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.true_button = QPushButton(self.centralwidget)
        self.true_button.setObjectName(u"true_button")
        self.true_button.setGeometry(QRect(40, 490, 161, 41))
        self.false_button = QPushButton(self.centralwidget)
        self.false_button.setObjectName(u"false_button")
        self.false_button.setGeometry(QRect(370, 390, 161, 180))     #ereeti: (370, 490, 161, 41)
        self.original_image_label = QLabel(self.centralwidget)
        self.original_image_label.setObjectName(u"original_image_label")
        self.original_image_label.setGeometry(QRect(80, 80, 391, 300))
        self.original_image_label.setFrameShape(QFrame.StyledPanel)
        self.original_image_label.setScaledContents(True)
        self.original_image_label.setAlignment(Qt.AlignCenter)
        self.choose_image_button = QPushButton(self.centralwidget)
        self.choose_image_button.setObjectName(u"choose_image_button")
        self.choose_image_button.setGeometry(QRect(20, 10, 91, 23))
        self.sliced_image_label = QLabel(self.centralwidget)
        self.sliced_image_label.setObjectName(u"sliced_image_label")
        self.sliced_image_label.setGeometry(QRect(250, 480, 60, 60))
        self.sliced_image_label.setFocusPolicy(Qt.NoFocus)
        self.sliced_image_label.setFrameShape(QFrame.StyledPanel)
        self.sliced_image_label.setFrameShadow(QFrame.Plain)
        self.sliced_image_label.setAlignment(Qt.AlignCenter)
        self.choose_sliced_image_folder_button = QPushButton(self.centralwidget)
        self.choose_sliced_image_folder_button.setObjectName(u"choose_sliced_image_folder")
        self.choose_sliced_image_folder_button.setGeometry(QRect(120, 10, 161, 23))
        self.frame_label = QLabel(self.centralwidget)
        self.frame_label.setObjectName(u"frame_label")
        self.frame_label.setGeometry(QRect(80, 80, 15, 15))
        self.frame_label.setFrameShape(QFrame.NoFrame)
        self.frame_label.setLineWidth(1)
        self.frame_label.setPixmap(QPixmap(u"frame.png"))
        self.file_name_label = QLabel(self.centralwidget)
        self.file_name_label.setObjectName(u"file_name_label")
        self.file_name_label.setGeometry(QRect(208, 50, 161, 21))
        self.file_name_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.filename_list = []

        self.choose_image_button.clicked.connect(self.choose_image)

        self.choose_sliced_image_folder_button.clicked.connect(self.choose_sliced_image_folder)

        self.true_button.clicked.connect(self.click_true)
        self.false_button.clicked.connect(self.click_false)
        self.counter_button_clicked = 0

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"sejtosztodas", None))
        self.true_button.setText(QCoreApplication.translate("MainWindow", u"IGEN", None))
        self.false_button.setText(QCoreApplication.translate("MainWindow", u"NEM", None))
        self.original_image_label.setText("")
        self.choose_image_button.setText(QCoreApplication.translate("MainWindow", u"K\u00e9p v\u00e1laszt\u00e1s", None))
        self.sliced_image_label.setText("")
        self.choose_sliced_image_folder_button.setText(QCoreApplication.translate("MainWindow", u"Szeletelt k\u00e9p mappa v\u00e1laszt\u00e1sa", None))
    # retranslateUi



    def make_slice_dir(self, im_name):
        try:
            os.mkdir("sliced_images_folder")
        except FileExistsError:
            print("A mappa már létezik.")
        try:
            temp_path = rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\sliced_images_folder\{im_name}"
            os.mkdir(temp_path)
            print("Mappa létrehozva")
        except:
            print("A mappa már létezik")

    def original_image_url(self, image_name):
        if image_name[4] == "f":
            original_image_url = rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\szekvencia elso fele\{image_name}.tif"
        if image_name[4] == "s":
            original_image_url = rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\szekvencia masodik fele\{image_name}.tif"

        return original_image_url

    def sliced_image_url(self, image_name, counter):
        sliced_image_url = rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\sliced_images_folder\{image_name}\{counter}_{image_name}.tif"
        return sliced_image_url

    def choose_image(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Choose image", os.getcwd(), "All Files (*)")
        fname = filename.split("/")
        im_name = fname[-1].split(".")[0]           # kép neve
        im_ext = fname[-1].split(".")[1]

        #képszelet
        try:
            image = Image.open(rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\szekvencia elso fele\{fname[-1]}")
        except:
            image = Image.open(rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\szekvencia masodik fele\{fname[-1]}")

        image = np.array(image)
        image = image[0 : 1200, 0 : 1560]


        self.make_slice_dir(im_name)

        # SZELETELÉS
        global number_of_slice
        number_of_slice = 0
        for i in range(int(image.shape[0] / 60)):
            for j in range(int(image.shape[1] / 60)):
                k = i + 1
                l = j + 1
                cropped_image = image[i * 60: k * 60, j * 60: l * 60]
                index = str(i) + str(j)
                new_im_name = f"{number_of_slice}_{im_name}.{im_ext}"

                #kép lementése a saját nevű mappájába

                cropped_img = Image.fromarray(cropped_image)
                cropped_img.save(rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\sliced_images_folder\{im_name}\{new_im_name}")
                number_of_slice += 1

        print("Szeletelés, mentés sikeres.")

        # image_test = self.convert_nparray_to_QPixmap(image)

        return number_of_slice


    def choose_sliced_image_folder(self):
        foldername = QFileDialog.getExistingDirectory(None, "Kép mappa választás", "All Files (*)")
        #print(foldername)
        foldername_temp = foldername.split("/")
        filename = foldername_temp[-1]
        #print(filename)
        count_of_img = 0
        NUMBER_OF_SLICE = 520
        FILE_EXT = "tif"

        #eredeti kép megjelenítése
        self.pixmap = QPixmap(self.original_image_url(filename))
        self.original_image_label.setPixmap(self.pixmap)

        self.filename_list.clear()
        self.filename_list.append(filename)

        #szeletelt kép megjelenítése
        self.pixmap = QPixmap(self.sliced_image_url(self.filename_list[0], self.counter_button_clicked))
        self.sliced_image_label.setPixmap(self.pixmap)

        self.file_name_label.setText(self.filename_list[0])

        self.frame_label.move(80, 80)

        self.counter_button_clicked = 0

    def click_true(self):
        self.counter_button_clicked += 1
        print(f"{self.counter_button_clicked}_{self.filename_list[0]}")
        #print(self.sliced_image_url(self.filename_list[0], self.counter_true_button_clicked))
        self.pixmap = QPixmap(self.sliced_image_url(self.filename_list[0], self.counter_button_clicked))
        self.sliced_image_label.setPixmap(self.pixmap)
        with open(rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\sliced_images_csv\{self.filename_list[0]}.csv", "a") as out_file:
            print(f"{self.counter_button_clicked - 1}_{self.filename_list[0]}", 1, file = out_file)
            #azért counter_button_clicked -1, mert az első kép az az amit megjelenít alapból, ekkor 0 kattintás volt még

        #move frame

        x_pos = self.counter_button_clicked % 26
        y_pos = self.counter_button_clicked // 26

        self.frame_label.move(x_pos * 15 + 80, y_pos * 15 + 80)


    def click_false(self):
        self.counter_button_clicked += 1
        print(f"{self.counter_button_clicked}_{self.filename_list[0]}")
        self.pixmap = QPixmap(self.sliced_image_url(self.filename_list[0], self.counter_button_clicked))
        self.sliced_image_label.setPixmap(self.pixmap)
        with open(rf"C:\Users\Silye Csabi\Desktop\Mappák\Iskola\Egyetem\Programozás\sliced_images_csv\{self.filename_list[0]}.csv", "a") as out_file:
            print(f"{self.counter_button_clicked - 1}_{self.filename_list[0]}", 0, file = out_file)

        self.frame_label.move(80 + self.counter_button_clicked * 15, 80)

        # move frame

        x_pos = self.counter_button_clicked % 26
        y_pos = self.counter_button_clicked // 26

        self.frame_label.move(x_pos * 15 + 80, y_pos * 15 + 80)

    try:
        os.mkdir("sliced_images_csv")
    except FileExistsError:
        print("A mappa már létezik.")

import sys
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())