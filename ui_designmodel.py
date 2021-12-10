# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from TaskModel import TaskModel

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(691, 511)
        MainWindow.setStyleSheet(u"")
        self.actionA_adir = QAction(MainWindow)
        self.actionA_adir.setObjectName(u"actionA_adir")
        icon = QIcon()
        icon.addFile(u":/iconos/icons8-a\u00f1adir-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionA_adir.setIcon(icon)
        self.actionEliminar = QAction(MainWindow)
        self.actionEliminar.setObjectName(u"actionEliminar")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/icons8-eliminar-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEliminar.setIcon(icon1)
        self.actionOcultar_barra_de_herramientas = QAction(MainWindow)
        self.actionOcultar_barra_de_herramientas.setObjectName(u"actionOcultar_barra_de_herramientas")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/icons8-ocultar-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOcultar_barra_de_herramientas.setIcon(icon2)
        self.actionMostrar_barra_de_herramientas = QAction(MainWindow)
        self.actionMostrar_barra_de_herramientas.setObjectName(u"actionMostrar_barra_de_herramientas")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/icons8-visible-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMostrar_barra_de_herramientas.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(155, 224, 39);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.model = TaskModel()

        self.listView = QListView(self.centralwidget)
        self.listView.setModel(self.model)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"background-color: rgb(193, 229, 163);")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.listView)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.PBDel = QPushButton(self.centralwidget)
        self.PBDel.setShortcut(QKeySequence("Ctrl+o"))
        self.PBDel.setObjectName(u"PBDel")
        self.PBDel.setStyleSheet(u"background-color: rgb(185, 230, 108);")

        self.gridLayout.addWidget(self.PBDel, 2, 0, 1, 1)

        self.PBAdd = QPushButton(self.centralwidget)
        self.PBAdd.setShortcut(QKeySequence("Ctrl+p"))
        self.PBAdd.setObjectName(u"PBAdd")
        self.PBAdd.setStyleSheet(u"background-color: rgb(185, 230, 108);")

        self.gridLayout.addWidget(self.PBAdd, 1, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)


        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)


        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.gridLayout)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(193, 229, 163);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 691, 22))
        self.menuBar.setStyleSheet(u"background-color: rgb(0, 199, 0);")
        self.menuTarea = QMenu(self.menuBar)
        self.menuTarea.setObjectName(u"menuTarea")
        self.menuBarra_de_herramientas = QMenu(self.menuBar)
        self.menuBarra_de_herramientas.setObjectName(u"menuBarra_de_herramientas")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setStyleSheet(u"background-color: rgb(0, 199, 0);")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"background-color: rgb(0, 199, 0);")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.lineEdit)
#endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menuTarea.menuAction())
        self.menuBar.addAction(self.menuBarra_de_herramientas.menuAction())
        self.menuTarea.addAction(self.actionA_adir)
        self.menuTarea.addAction(self.actionEliminar)
        self.menuBarra_de_herramientas.addAction(self.actionOcultar_barra_de_herramientas)
        self.menuBarra_de_herramientas.addAction(self.actionMostrar_barra_de_herramientas)
        self.toolBar.addAction(self.actionA_adir)
        self.toolBar.addAction(self.actionEliminar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionOcultar_barra_de_herramientas)

        self.retranslateUi(MainWindow)
        self.actionMostrar_barra_de_herramientas.triggered.connect(self.toolBar.show)
        self.actionOcultar_barra_de_herramientas.triggered.connect(self.toolBar.hide)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionA_adir.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
#if QT_CONFIG(statustip)
        self.actionA_adir.setStatusTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir tarea al tablon", None))
#endif // QT_CONFIG(statustip)
        self.actionEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
#if QT_CONFIG(statustip)
        self.actionEliminar.setStatusTip(QCoreApplication.translate("MainWindow", u"Elimina la tarea del tablon", None))
#endif // QT_CONFIG(statustip)
        self.actionOcultar_barra_de_herramientas.setText(QCoreApplication.translate("MainWindow", u"Ocultar barra de herramientas", None))
#if QT_CONFIG(statustip)
        self.actionOcultar_barra_de_herramientas.setStatusTip(QCoreApplication.translate("MainWindow", u"Oculta la barra de herramientas", None))
#endif // QT_CONFIG(statustip)
        self.actionMostrar_barra_de_herramientas.setText(QCoreApplication.translate("MainWindow", u"Mostrar barra de herramientas", None))
#if QT_CONFIG(statustip)
        self.actionMostrar_barra_de_herramientas.setStatusTip(QCoreApplication.translate("MainWindow", u"Mostrar barra de herranientas", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tablon de tareas", None))
        self.PBDel.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.PBAdd.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"&Tarea", None))
        self.menuTarea.setTitle(QCoreApplication.translate("MainWindow", u"Tarea", None))
        self.menuBarra_de_herramientas.setTitle(QCoreApplication.translate("MainWindow", u"Barra de herramientas", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

