from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow

import os


class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filenames = None
        self.image = None
        self.ui.folder_btn.clicked.connect(self.chosse_folder)
        self.ui.dw_btn.clicked.connect(self.do_black_white)
        self.ui.image_list.currentRowChanged.connect(self.show_image_list)

    def show_image_list(self):
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images.append(filename)
        self.ui.image_list.clear()
        self.ui.image_list.addItems(images)

    def chosse_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            message = QMessageBox()
            message.setText("Помилка відкритя папки!")
            message.exec_()

    def load_image(self, imagename):
        self.image_name = imagename
        self.image_path = os.path.join(self.workdir, self.image_name)
        self.image = Image.open(self.image_path)

    def show_image(self):
        self.ui.image_label.height.hide()
        h = self.ui.image.height()
        w = self.ui.image_label.width()

        pixmap_image = QPixmap(self.image_path)
        pixmap_image = pixmap_image.scaled(w, h, Qt.KeepAspectRatio)
        self.ui.image_label.setPixmap(pixmap_image)
        self.ui.image_label.show()

    def show_chosen_image(self):
        if self.ui.image_list.currentRow()>=0:
            self.image_name = self.ui.image_list.currentItem().text()
            self.load_images(self.image_name)
            self.show_image()
    
    def save_image(self):
        path = os.path.join(self.eorkdir, "edited")
        if not(os.path.exists(path) or os.path.isdir(path))
        self.new_path = os.path.join(path, self.image_name)
        self.new_image.save(self.new_path)

    def do_black_white():
        self.new_image = self.image.convert('L')
        self.save_image()
        self.show_image()



app = QApplication([])
ex = Widget()
ex.show()
app.exec_()



