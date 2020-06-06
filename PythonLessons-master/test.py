from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QLabel
from PyQt5.QtGui import QPixmap, QTransform
import sys



class Rotate(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Вращение изображения')

#       Кнопка загрузки изображения
        self.btn = QPushButton('Показать картинку', self)
        self.btn.move(120, 340)
        self.btn.clicked.connect(self.run)

#       Кнопка переворота изображения на 90° налево
        self.btn1 = QPushButton("Перевернуть изображение на 90° влево", self)
        self.btn1.move(120, 360)
        self.btn1.clicked.connect(self.left_rotate)

    #       Поле для ввода имени файла
        self.file_name = QLineEdit(self)
        self.file_name.move(140, 20)

    #       Изображение
        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)

    def run(self):
        self.pixmap.load(self.file_name.text())
        self.image.setPixmap(self.pixmap)

    def left_rotate(self):
        p = QPixmap().load(self.file_name.text())
        t = QTransform().rotate(+90)
        self.image.setPixmap(p.transformed(t))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rotate()
    ex.show()
    sys.exit(app.exec())