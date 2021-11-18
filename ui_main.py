# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(855, 542)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0,10);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 20);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 35))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_pg_import = QPushButton(self.frame)
        self.btn_pg_import.setObjectName(u"btn_pg_import")
        self.btn_pg_import.setMinimumSize(QSize(0, 33))
        self.btn_pg_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_import.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_pg_import)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 33))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 33))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 33))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_8 = QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"")
        self.tw_estoque.setAlternatingRowColors(False)

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(100, 27))
        self.btn_gerar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_estorno = QPushButton(self.frame_2)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setMinimumSize(QSize(100, 27))
        self.btn_estorno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estorno.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.btn_estorno)

        self.btn_ = QPushButton(self.frame_2)
        self.btn_.setObjectName(u"btn_")
        self.btn_.setMinimumSize(QSize(100, 27))
        self.btn_.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px;\n"
"	 font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #fff;\n"
"	 color:black\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_17)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_chart = QPushButton(self.tab_2)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setMinimumSize(QSize(123, 28))
        self.btn_chart.setSizeIncrement(QSize(0, 0))
        self.btn_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chart.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_chart)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(123, 28))
        self.btn_excel.setSizeIncrement(QSize(0, 0))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_excel)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.txt_search = QLineEdit(self.tab_2)
        self.txt_search.setObjectName(u"txt_search")
        font1 = QFont()
        font1.setPointSize(11)
        self.txt_search.setFont(font1)
        self.txt_search.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_search.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.txt_search)

        self.tb_geral = QTableView(self.tab_2)
        self.tb_geral.setObjectName(u"tb_geral")

        self.verticalLayout_10.addWidget(self.tb_geral)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u" background-color: rgb(0, 80, 121);\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setMinimumSize(QSize(0, 33))
        font2 = QFont()
        font2.setPointSize(10)
        self.btn_pg_cadastro.setFont(font2)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(255, 255, 255);\n"
" 	color:black\n"
" }")

        self.verticalLayout.addWidget(self.btn_pg_cadastro)

        self.Pages.addWidget(self.pg_home)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.verticalLayout_11 = QVBoxLayout(self.pg_import)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.pg_import)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_18)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_file = QLineEdit(self.pg_import)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 28))
        self.txt_file.setFont(font1)
        self.txt_file.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.pg_import)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(123, 28))
        self.btn_open.setSizeIncrement(QSize(0, 0))
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-top-right-radius:15px;\n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.pg_import)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.btn_import = QPushButton(self.pg_import)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(123, 28))
        self.btn_import.setSizeIncrement(QSize(0, 0))
        self.btn_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.btn_import)

        self.label_5 = QLabel(self.pg_import)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.progressBar = QProgressBar(self.pg_import)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{	background-color: rgba(0, 0, 0,0.1);\n"
"                    	color: rgb(255, 255, 255);\n"
"                		border-style: none;\n"
"                		text-align: center;\n"
"                		border-radius:10px;\n"
"                \n"
"                }\n"
" \n"
"               \n"
"QProgressBar::chunk{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 75, 149, 255), stop:1 rgba(72, 130, 157, 255));\n"
"                				border-radius:10px;\n"
"                                }")
        self.progressBar.setValue(0)

        self.verticalLayout_11.addWidget(self.progressBar)

        self.Pages.addWidget(self.pg_import)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, -1, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy2)
        self.txt_nome.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_8.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_7.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, -1, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, -1, -1, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, -1, -1, -1)
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy2.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(12)
        self.cb_perfil.setFont(font3)
        self.cb_perfil.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 35))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_15 = QLabel(self.pg_contato)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_15)

        self.label_19 = QLabel(self.pg_contato)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_19)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_27 = QLabel(self.pg_contato)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_15.addWidget(self.label_27)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_24 = QLabel(self.pg_contato)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.label_24)

        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_20)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)

        self.label_28 = QLabel(self.pg_contato)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_15.addWidget(self.label_28)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_29 = QLabel(self.pg_contato)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_16.addWidget(self.label_29)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_25 = QLabel(self.pg_contato)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.label_25)

        self.label_21 = QLabel(self.pg_contato)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_21)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)

        self.label_30 = QLabel(self.pg_contato)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_16.addWidget(self.label_30)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_31 = QLabel(self.pg_contato)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_17.addWidget(self.label_31)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_26 = QLabel(self.pg_contato)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.label_26)

        self.label_22 = QLabel(self.pg_contato)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_22)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_14)

        self.label_32 = QLabel(self.pg_contato)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_17.addWidget(self.label_32)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)

        self.Pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_13 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_16 = QLabel(self.pg_sobre)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_16)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.label_23 = QLabel(self.pg_sobre)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_23)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_pg_import.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Estoque</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(14, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Valor Produto", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Unidade medida", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Total Nfe", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Emitente", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Cnpj_emitente", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Data_emissao", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Sa\u00edda</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"DATA SA\u00cdDA", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"DATA IMPORTA\u00c7\u00c3O", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"SERIE", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar sa\u00edda", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.btn_.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"GERAL", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"GERAL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">PYTAX</span></p><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Sistema de gerenciamento</span></p><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\"><img src=\"_imgs/logo.png\"/></span></p></body></html>", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR XML", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleciona a pasta com os arquivos XML --->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_4.setText("")
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_5.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tela de cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"_imgs/user.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nome:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Usu\u00e1rio</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Perfil:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CONTATOS", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Desenvolvedor: Nicolas almeida</span></p></body></html>", None))
        self.label_27.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"_imgs/phone.png\"/></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">(11)98013-0552</span></p></body></html>", None))
        self.label_28.setText("")
        self.label_29.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"_imgs/email.png\"/></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\"> contato@pytax.net</span></p></body></html>", None))
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"_imgs/instagram.png\"/></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">pytax</span></p></body></html>", None))
        self.label_32.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Este sistema faz a imoprta\u00e7\u00e3o de arquivos XML e faz o controle do estoque de acordo com a entrada de notas e sa\u00eddas apontadas pelo usu\u00e1rio.</span></p></body></html>", None))
    # retranslateUi

