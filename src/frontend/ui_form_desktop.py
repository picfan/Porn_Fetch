# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_desktop.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTextBrowser, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_PornFetch_Desktop(object):
    def setupUi(self, PornFetch_Desktop):
        if not PornFetch_Desktop.objectName():
            PornFetch_Desktop.setObjectName(u"PornFetch_Desktop")
        PornFetch_Desktop.resize(1409, 918)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PornFetch_Desktop.sizePolicy().hasHeightForWidth())
        PornFetch_Desktop.setSizePolicy(sizePolicy)
        PornFetch_Desktop.setMinimumSize(QSize(670, 580))
        PornFetch_Desktop.setStyleSheet(u"QLbel {\n"
"    color: black;}")
        self.gridLayout_16 = QGridLayout(PornFetch_Desktop)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticallayout_main = QVBoxLayout()
        self.verticallayout_main.setSpacing(0)
        self.verticallayout_main.setObjectName(u"verticallayout_main")
        self.main_horizontallayout_menu_buttons = QHBoxLayout()
        self.main_horizontallayout_menu_buttons.setSpacing(0)
        self.main_horizontallayout_menu_buttons.setObjectName(u"main_horizontallayout_menu_buttons")
        self.main_button_switch_home = QPushButton(PornFetch_Desktop)
        self.main_button_switch_home.setObjectName(u"main_button_switch_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_button_switch_home.sizePolicy().hasHeightForWidth())
        self.main_button_switch_home.setSizePolicy(sizePolicy1)
        self.main_button_switch_home.setMinimumSize(QSize(50, 35))
        self.main_button_switch_home.setMaximumSize(QSize(16777215, 35))
        self.main_button_switch_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_button_switch_home.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #a9a9a9;\n"
"    border-radius: 8px;\n"
"    padding: 8px 10px;\n"
"}")
        self.main_button_switch_home.setIconSize(QSize(32, 32))

        self.main_horizontallayout_menu_buttons.addWidget(self.main_button_switch_home)

        self.main_button_switch_account = QPushButton(PornFetch_Desktop)
        self.main_button_switch_account.setObjectName(u"main_button_switch_account")
        sizePolicy1.setHeightForWidth(self.main_button_switch_account.sizePolicy().hasHeightForWidth())
        self.main_button_switch_account.setSizePolicy(sizePolicy1)
        self.main_button_switch_account.setMinimumSize(QSize(50, 35))
        self.main_button_switch_account.setMaximumSize(QSize(16777215, 35))
        self.main_button_switch_account.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_button_switch_account.setStyleSheet(u"QPushButton {\n"
"    border-radius: 8px;\n"
"    padding: 8px 10px;\n"
"    border: 2px solid #a9a9a9;\n"
"}\n"
"")
        self.main_button_switch_account.setIconSize(QSize(32, 32))

        self.main_horizontallayout_menu_buttons.addWidget(self.main_button_switch_account)

        self.main_button_switch_tools = QPushButton(PornFetch_Desktop)
        self.main_button_switch_tools.setObjectName(u"main_button_switch_tools")
        sizePolicy1.setHeightForWidth(self.main_button_switch_tools.sizePolicy().hasHeightForWidth())
        self.main_button_switch_tools.setSizePolicy(sizePolicy1)
        self.main_button_switch_tools.setMinimumSize(QSize(50, 35))
        self.main_button_switch_tools.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        self.main_button_switch_tools.setFont(font)
        self.main_button_switch_tools.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_button_switch_tools.setStyleSheet(u"QPushButton {\n"
"    border-radius: 8px;\n"
"    border: 2px solid #a9a9a9;\n"
"    padding: 8px 10px;\n"
"}\n"
"")
        self.main_button_switch_tools.setIconSize(QSize(32, 32))

        self.main_horizontallayout_menu_buttons.addWidget(self.main_button_switch_tools)

        self.main_button_switch_settings = QPushButton(PornFetch_Desktop)
        self.main_button_switch_settings.setObjectName(u"main_button_switch_settings")
        sizePolicy1.setHeightForWidth(self.main_button_switch_settings.sizePolicy().hasHeightForWidth())
        self.main_button_switch_settings.setSizePolicy(sizePolicy1)
        self.main_button_switch_settings.setMinimumSize(QSize(50, 35))
        self.main_button_switch_settings.setMaximumSize(QSize(16777215, 35))
        self.main_button_switch_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_button_switch_settings.setStyleSheet(u"QPushButton {\n"
"    border-radius: 8px;\n"
"    border: 2px solid #a9a9a9;\n"
"    padding: 8px 10px;\n"
"}\n"
"")
        self.main_button_switch_settings.setIconSize(QSize(32, 32))

        self.main_horizontallayout_menu_buttons.addWidget(self.main_button_switch_settings)

        self.main_button_switch_credits = QPushButton(PornFetch_Desktop)
        self.main_button_switch_credits.setObjectName(u"main_button_switch_credits")
        sizePolicy1.setHeightForWidth(self.main_button_switch_credits.sizePolicy().hasHeightForWidth())
        self.main_button_switch_credits.setSizePolicy(sizePolicy1)
        self.main_button_switch_credits.setMinimumSize(QSize(50, 35))
        self.main_button_switch_credits.setMaximumSize(QSize(16777215, 35))
        self.main_button_switch_credits.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_button_switch_credits.setStyleSheet(u"QPushButton {\n"
"    border-radius: 8px;\n"
"    border: 2px solid #a9a9a9;\n"
"    padding: 8px 10px;\n"
"}\n"
"")
        self.main_button_switch_credits.setIconSize(QSize(32, 32))

        self.main_horizontallayout_menu_buttons.addWidget(self.main_button_switch_credits)

        self.main_button_view_progress_bars = QPushButton(PornFetch_Desktop)
        self.main_button_view_progress_bars.setObjectName(u"main_button_view_progress_bars")
        sizePolicy1.setHeightForWidth(self.main_button_view_progress_bars.sizePolicy().hasHeightForWidth())
        self.main_button_view_progress_bars.setSizePolicy(sizePolicy1)
        self.main_button_view_progress_bars.setMinimumSize(QSize(50, 35))
        self.main_button_view_progress_bars.setMaximumSize(QSize(16777215, 35))
        self.main_button_view_progress_bars.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_button_view_progress_bars.setStyleSheet(u"QPushButton {\n"
"    border-radius: 8px;\n"
"    border: 2px solid #a9a9a9;\n"
"    padding: 8px 10px;\n"
"}")
        self.main_button_view_progress_bars.setIconSize(QSize(32, 32))

        self.main_horizontallayout_menu_buttons.addWidget(self.main_button_view_progress_bars)

        self.main_button_switch_supported_websites = QPushButton(PornFetch_Desktop)
        self.main_button_switch_supported_websites.setObjectName(u"main_button_switch_supported_websites")
        sizePolicy1.setHeightForWidth(self.main_button_switch_supported_websites.sizePolicy().hasHeightForWidth())
        self.main_button_switch_supported_websites.setSizePolicy(sizePolicy1)
        self.main_button_switch_supported_websites.setMinimumSize(QSize(50, 35))
        self.main_button_switch_supported_websites.setMaximumSize(QSize(16777215, 35))
        self.main_button_switch_supported_websites.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.main_button_switch_supported_websites.setStyleSheet(u"QPushButton {\n"
"    border-radius: 8px;\n"
"    border: 2px solid #a9a9a9;\n"
"    padding: 8px 10px;\n"
"}")
        self.main_button_switch_supported_websites.setIconSize(QSize(32, 32))

        self.main_horizontallayout_menu_buttons.addWidget(self.main_button_switch_supported_websites)


        self.verticallayout_main.addLayout(self.main_horizontallayout_menu_buttons)

        self.stacked_widget_main = QStackedWidget(PornFetch_Desktop)
        self.stacked_widget_main.setObjectName(u"stacked_widget_main")
        self.stacked_widget_main.setLineWidth(1)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stacked_widget_top = QStackedWidget(self.widget)
        self.stacked_widget_top.setObjectName(u"stacked_widget_top")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stacked_widget_top.sizePolicy().hasHeightForWidth())
        self.stacked_widget_top.setSizePolicy(sizePolicy2)
        self.stacked_widget_top.setMinimumSize(QSize(650, 20))
        self.stacked_widget_top.setStyleSheet(u"b")
        self.stacked_widget_top.setLineWidth(1)
        self.page_download = QWidget()
        self.page_download.setObjectName(u"page_download")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.page_download.sizePolicy().hasHeightForWidth())
        self.page_download.setSizePolicy(sizePolicy3)
        self.page_download.setMinimumSize(QSize(0, 0))
        self.gridLayout_5 = QGridLayout(self.page_download)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridlayout_downloading = QGridLayout()
        self.gridlayout_downloading.setSpacing(6)
        self.gridlayout_downloading.setObjectName(u"gridlayout_downloading")
        self.gridlayout_downloading.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridlayout_downloading.setContentsMargins(-1, 14, -1, -1)
        self.radio_search_website_xvideos = QRadioButton(self.page_download)
        self.radio_search_website_xvideos.setObjectName(u"radio_search_website_xvideos")
        sizePolicy2.setHeightForWidth(self.radio_search_website_xvideos.sizePolicy().hasHeightForWidth())
        self.radio_search_website_xvideos.setSizePolicy(sizePolicy2)
        self.radio_search_website_xvideos.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.radio_search_website_xvideos, 8, 3, 1, 1)

        self.button_help_file = QPushButton(self.page_download)
        self.button_help_file.setObjectName(u"button_help_file")
        sizePolicy2.setHeightForWidth(self.button_help_file.sizePolicy().hasHeightForWidth())
        self.button_help_file.setSizePolicy(sizePolicy2)
        self.button_help_file.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.button_help_file, 6, 4, 1, 1)

        self.radio_search_website_pornhub = QRadioButton(self.page_download)
        self.radio_search_website_pornhub.setObjectName(u"radio_search_website_pornhub")
        sizePolicy2.setHeightForWidth(self.radio_search_website_pornhub.sizePolicy().hasHeightForWidth())
        self.radio_search_website_pornhub.setSizePolicy(sizePolicy2)
        self.radio_search_website_pornhub.setMinimumSize(QSize(0, 30))
        self.radio_search_website_pornhub.setChecked(True)

        self.gridlayout_downloading.addWidget(self.radio_search_website_pornhub, 8, 1, 1, 1)

        self.button_playlist_get_videos = QPushButton(self.page_download)
        self.button_playlist_get_videos.setObjectName(u"button_playlist_get_videos")
        sizePolicy2.setHeightForWidth(self.button_playlist_get_videos.sizePolicy().hasHeightForWidth())
        self.button_playlist_get_videos.setSizePolicy(sizePolicy2)
        self.button_playlist_get_videos.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.button_playlist_get_videos, 4, 5, 1, 1)

        self.label_model_url = QLabel(self.page_download)
        self.label_model_url.setObjectName(u"label_model_url")
        sizePolicy2.setHeightForWidth(self.label_model_url.sizePolicy().hasHeightForWidth())
        self.label_model_url.setSizePolicy(sizePolicy2)
        self.label_model_url.setMinimumSize(QSize(100, 30))

        self.gridlayout_downloading.addWidget(self.label_model_url, 5, 0, 1, 1)

        self.lineedit_url = QLineEdit(self.page_download)
        self.lineedit_url.setObjectName(u"lineedit_url")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineedit_url.sizePolicy().hasHeightForWidth())
        self.lineedit_url.setSizePolicy(sizePolicy4)
        self.lineedit_url.setMinimumSize(QSize(300, 30))

        self.gridlayout_downloading.addWidget(self.lineedit_url, 2, 1, 1, 4)

        self.label_playlist_url = QLabel(self.page_download)
        self.label_playlist_url.setObjectName(u"label_playlist_url")
        sizePolicy3.setHeightForWidth(self.label_playlist_url.sizePolicy().hasHeightForWidth())
        self.label_playlist_url.setSizePolicy(sizePolicy3)
        self.label_playlist_url.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.label_playlist_url, 4, 0, 1, 1)

        self.button_search = QPushButton(self.page_download)
        self.button_search.setObjectName(u"button_search")
        sizePolicy2.setHeightForWidth(self.button_search.sizePolicy().hasHeightForWidth())
        self.button_search.setSizePolicy(sizePolicy2)
        self.button_search.setMinimumSize(QSize(0, 30))
        self.button_search.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_downloading.addWidget(self.button_search, 7, 5, 1, 1)

        self.radio_search_website_eporner = QRadioButton(self.page_download)
        self.radio_search_website_eporner.setObjectName(u"radio_search_website_eporner")
        sizePolicy2.setHeightForWidth(self.radio_search_website_eporner.sizePolicy().hasHeightForWidth())
        self.radio_search_website_eporner.setSizePolicy(sizePolicy2)
        self.radio_search_website_eporner.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.radio_search_website_eporner, 8, 4, 1, 1)

        self.label_file = QLabel(self.page_download)
        self.label_file.setObjectName(u"label_file")
        sizePolicy2.setHeightForWidth(self.label_file.sizePolicy().hasHeightForWidth())
        self.label_file.setSizePolicy(sizePolicy2)
        self.label_file.setMinimumSize(QSize(100, 30))

        self.gridlayout_downloading.addWidget(self.label_file, 6, 0, 1, 1)

        self.radio_search_website_xnxx = QRadioButton(self.page_download)
        self.radio_search_website_xnxx.setObjectName(u"radio_search_website_xnxx")
        sizePolicy2.setHeightForWidth(self.radio_search_website_xnxx.sizePolicy().hasHeightForWidth())
        self.radio_search_website_xnxx.setSizePolicy(sizePolicy2)
        self.radio_search_website_xnxx.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.radio_search_website_xnxx, 8, 5, 1, 1)

        self.lineedit_model_url = QLineEdit(self.page_download)
        self.lineedit_model_url.setObjectName(u"lineedit_model_url")
        sizePolicy4.setHeightForWidth(self.lineedit_model_url.sizePolicy().hasHeightForWidth())
        self.lineedit_model_url.setSizePolicy(sizePolicy4)
        self.lineedit_model_url.setMinimumSize(QSize(300, 30))

        self.gridlayout_downloading.addWidget(self.lineedit_model_url, 5, 1, 1, 4)

        self.button_open_file = QPushButton(self.page_download)
        self.button_open_file.setObjectName(u"button_open_file")
        sizePolicy2.setHeightForWidth(self.button_open_file.sizePolicy().hasHeightForWidth())
        self.button_open_file.setSizePolicy(sizePolicy2)
        self.button_open_file.setMinimumSize(QSize(60, 30))
        self.button_open_file.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_open_file.setStyleSheet(u"")

        self.gridlayout_downloading.addWidget(self.button_open_file, 6, 5, 1, 1)

        self.button_model = QPushButton(self.page_download)
        self.button_model.setObjectName(u"button_model")
        sizePolicy2.setHeightForWidth(self.button_model.sizePolicy().hasHeightForWidth())
        self.button_model.setSizePolicy(sizePolicy2)
        self.button_model.setMinimumSize(QSize(60, 30))
        self.button_model.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_model.setStyleSheet(u"")

        self.gridlayout_downloading.addWidget(self.button_model, 5, 5, 1, 1)

        self.lineedit_file = QLineEdit(self.page_download)
        self.lineedit_file.setObjectName(u"lineedit_file")
        sizePolicy4.setHeightForWidth(self.lineedit_file.sizePolicy().hasHeightForWidth())
        self.lineedit_file.setSizePolicy(sizePolicy4)
        self.lineedit_file.setMinimumSize(QSize(300, 30))
        self.lineedit_file.setReadOnly(True)

        self.gridlayout_downloading.addWidget(self.lineedit_file, 6, 1, 1, 3)

        self.button_download = QPushButton(self.page_download)
        self.button_download.setObjectName(u"button_download")
        sizePolicy2.setHeightForWidth(self.button_download.sizePolicy().hasHeightForWidth())
        self.button_download.setSizePolicy(sizePolicy2)
        self.button_download.setMinimumSize(QSize(60, 30))
        self.button_download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_download.setStyleSheet(u"")

        self.gridlayout_downloading.addWidget(self.button_download, 2, 5, 1, 1)

        self.labell_search = QLabel(self.page_download)
        self.labell_search.setObjectName(u"labell_search")
        sizePolicy3.setHeightForWidth(self.labell_search.sizePolicy().hasHeightForWidth())
        self.labell_search.setSizePolicy(sizePolicy3)
        self.labell_search.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.labell_search, 7, 0, 1, 1)

        self.label_search_website = QLabel(self.page_download)
        self.label_search_website.setObjectName(u"label_search_website")
        sizePolicy.setHeightForWidth(self.label_search_website.sizePolicy().hasHeightForWidth())
        self.label_search_website.setSizePolicy(sizePolicy)
        self.label_search_website.setMinimumSize(QSize(0, 0))

        self.gridlayout_downloading.addWidget(self.label_search_website, 8, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridlayout_downloading.addItem(self.verticalSpacer_4, 9, 2, 1, 1)

        self.radio_search_website_hqporner = QRadioButton(self.page_download)
        self.radio_search_website_hqporner.setObjectName(u"radio_search_website_hqporner")
        sizePolicy2.setHeightForWidth(self.radio_search_website_hqporner.sizePolicy().hasHeightForWidth())
        self.radio_search_website_hqporner.setSizePolicy(sizePolicy2)
        self.radio_search_website_hqporner.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.radio_search_website_hqporner, 8, 2, 1, 1)

        self.lineedit_playlist_url = QLineEdit(self.page_download)
        self.lineedit_playlist_url.setObjectName(u"lineedit_playlist_url")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineedit_playlist_url.sizePolicy().hasHeightForWidth())
        self.lineedit_playlist_url.setSizePolicy(sizePolicy5)
        self.lineedit_playlist_url.setMinimumSize(QSize(0, 30))

        self.gridlayout_downloading.addWidget(self.lineedit_playlist_url, 4, 1, 1, 4)

        self.lineedit_search_query = QLineEdit(self.page_download)
        self.lineedit_search_query.setObjectName(u"lineedit_search_query")
        sizePolicy4.setHeightForWidth(self.lineedit_search_query.sizePolicy().hasHeightForWidth())
        self.lineedit_search_query.setSizePolicy(sizePolicy4)
        self.lineedit_search_query.setMinimumSize(QSize(300, 30))

        self.gridlayout_downloading.addWidget(self.lineedit_search_query, 7, 1, 1, 4)

        self.label_url = QLabel(self.page_download)
        self.label_url.setObjectName(u"label_url")
        sizePolicy2.setHeightForWidth(self.label_url.sizePolicy().hasHeightForWidth())
        self.label_url.setSizePolicy(sizePolicy2)
        self.label_url.setMinimumSize(QSize(100, 30))

        self.gridlayout_downloading.addWidget(self.label_url, 2, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridlayout_downloading, 0, 0, 1, 1)

        self.stacked_widget_top.addWidget(self.page_download)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.page_login.setMinimumSize(QSize(0, 30))
        self.gridLayout_2 = QGridLayout(self.page_login)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridlayout_login_box = QGridLayout()
        self.gridlayout_login_box.setSpacing(6)
        self.gridlayout_login_box.setObjectName(u"gridlayout_login_box")
        self.gridlayout_login_box.setContentsMargins(-1, 14, -1, -1)
        self.button_get_liked_videos = QPushButton(self.page_login)
        self.button_get_liked_videos.setObjectName(u"button_get_liked_videos")
        self.button_get_liked_videos.setMinimumSize(QSize(0, 30))
        self.button_get_liked_videos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_get_liked_videos.setStyleSheet(u"")

        self.gridlayout_login_box.addWidget(self.button_get_liked_videos, 3, 0, 1, 1)

        self.button_get_watched_videos = QPushButton(self.page_login)
        self.button_get_watched_videos.setObjectName(u"button_get_watched_videos")
        self.button_get_watched_videos.setMinimumSize(QSize(0, 30))
        self.button_get_watched_videos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_get_watched_videos.setStyleSheet(u"")

        self.gridlayout_login_box.addWidget(self.button_get_watched_videos, 3, 1, 1, 1)

        self.label_username = QLabel(self.page_login)
        self.label_username.setObjectName(u"label_username")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy6)
        self.label_username.setMinimumSize(QSize(0, 30))

        self.gridlayout_login_box.addWidget(self.label_username, 0, 0, 1, 1)

        self.button_login = QPushButton(self.page_login)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setMinimumSize(QSize(0, 30))
        self.button_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_login.setStyleSheet(u"")

        self.gridlayout_login_box.addWidget(self.button_login, 2, 0, 1, 4)

        self.lineedit_username = QLineEdit(self.page_login)
        self.lineedit_username.setObjectName(u"lineedit_username")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lineedit_username.sizePolicy().hasHeightForWidth())
        self.lineedit_username.setSizePolicy(sizePolicy7)
        self.lineedit_username.setMinimumSize(QSize(150, 30))

        self.gridlayout_login_box.addWidget(self.lineedit_username, 0, 1, 1, 3)

        self.button_get_recommended_videos = QPushButton(self.page_login)
        self.button_get_recommended_videos.setObjectName(u"button_get_recommended_videos")
        self.button_get_recommended_videos.setMinimumSize(QSize(0, 30))
        self.button_get_recommended_videos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_get_recommended_videos.setStyleSheet(u"")

        self.gridlayout_login_box.addWidget(self.button_get_recommended_videos, 3, 2, 1, 1)

        self.label_password = QLabel(self.page_login)
        self.label_password.setObjectName(u"label_password")
        sizePolicy6.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy6)
        self.label_password.setMinimumSize(QSize(0, 30))

        self.gridlayout_login_box.addWidget(self.label_password, 1, 0, 1, 1)

        self.lineedit_password = QLineEdit(self.page_login)
        self.lineedit_password.setObjectName(u"lineedit_password")
        sizePolicy7.setHeightForWidth(self.lineedit_password.sizePolicy().hasHeightForWidth())
        self.lineedit_password.setSizePolicy(sizePolicy7)
        self.lineedit_password.setMinimumSize(QSize(150, 30))
        self.lineedit_password.setEchoMode(QLineEdit.EchoMode.Normal)

        self.gridlayout_login_box.addWidget(self.lineedit_password, 1, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridlayout_login_box.addItem(self.verticalSpacer, 4, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridlayout_login_box, 0, 0, 1, 1)

        self.stacked_widget_top.addWidget(self.page_login)
        self.page_progressbars = QWidget()
        self.page_progressbars.setObjectName(u"page_progressbars")
        self.gridLayout_6 = QGridLayout(self.page_progressbars)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_progressbars)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 634, 272))
        self.gridLayout_18 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridlayout_progressbar = QGridLayout()
        self.gridlayout_progressbar.setObjectName(u"gridlayout_progressbar")
        self.gridlayout_progressbar.setHorizontalSpacing(6)
        self.progressbar_eporner = QProgressBar(self.scrollAreaWidgetContents)
        self.progressbar_eporner.setObjectName(u"progressbar_eporner")
        self.progressbar_eporner.setMinimumSize(QSize(0, 30))
        self.progressbar_eporner.setStyleSheet(u"text-align: center; /* Centered text */")
        self.progressbar_eporner.setValue(0)

        self.gridlayout_progressbar.addWidget(self.progressbar_eporner, 2, 1, 1, 1)

        self.label_progress_eporner = QLabel(self.scrollAreaWidgetContents)
        self.label_progress_eporner.setObjectName(u"label_progress_eporner")
        self.label_progress_eporner.setMinimumSize(QSize(0, 30))

        self.gridlayout_progressbar.addWidget(self.label_progress_eporner, 2, 0, 1, 1)

        self.progressbar_xnxx = QProgressBar(self.scrollAreaWidgetContents)
        self.progressbar_xnxx.setObjectName(u"progressbar_xnxx")
        self.progressbar_xnxx.setMinimumSize(QSize(0, 30))
        self.progressbar_xnxx.setStyleSheet(u"text-align: center; /* Centered text */")
        self.progressbar_xnxx.setValue(0)

        self.gridlayout_progressbar.addWidget(self.progressbar_xnxx, 3, 1, 1, 1)

        self.progressbar_pornhub = QProgressBar(self.scrollAreaWidgetContents)
        self.progressbar_pornhub.setObjectName(u"progressbar_pornhub")
        sizePolicy7.setHeightForWidth(self.progressbar_pornhub.sizePolicy().hasHeightForWidth())
        self.progressbar_pornhub.setSizePolicy(sizePolicy7)
        self.progressbar_pornhub.setMinimumSize(QSize(300, 30))
        self.progressbar_pornhub.setStyleSheet(u"text-align: center; /* Centered text */")
        self.progressbar_pornhub.setValue(0)

        self.gridlayout_progressbar.addWidget(self.progressbar_pornhub, 0, 1, 1, 1)

        self.progressbar_hqporner = QProgressBar(self.scrollAreaWidgetContents)
        self.progressbar_hqporner.setObjectName(u"progressbar_hqporner")
        sizePolicy7.setHeightForWidth(self.progressbar_hqporner.sizePolicy().hasHeightForWidth())
        self.progressbar_hqporner.setSizePolicy(sizePolicy7)
        self.progressbar_hqporner.setMinimumSize(QSize(300, 30))
        self.progressbar_hqporner.setStyleSheet(u"text-align: center; /* Centered text */")
        self.progressbar_hqporner.setValue(0)

        self.gridlayout_progressbar.addWidget(self.progressbar_hqporner, 1, 1, 1, 1)

        self.progressbar_spankbang = QProgressBar(self.scrollAreaWidgetContents)
        self.progressbar_spankbang.setObjectName(u"progressbar_spankbang")
        self.progressbar_spankbang.setMinimumSize(QSize(0, 30))
        self.progressbar_spankbang.setStyleSheet(u"text-align: center; /* Centered text */")
        self.progressbar_spankbang.setValue(0)

        self.gridlayout_progressbar.addWidget(self.progressbar_spankbang, 5, 1, 1, 1)

        self.progressbar_xvideos = QProgressBar(self.scrollAreaWidgetContents)
        self.progressbar_xvideos.setObjectName(u"progressbar_xvideos")
        self.progressbar_xvideos.setMinimumSize(QSize(0, 30))
        self.progressbar_xvideos.setStyleSheet(u"text-align: center; /* Centered text */")
        self.progressbar_xvideos.setValue(0)

        self.gridlayout_progressbar.addWidget(self.progressbar_xvideos, 4, 1, 1, 1)

        self.label_info = QLabel(self.scrollAreaWidgetContents)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setMinimumSize(QSize(0, 30))

        self.gridlayout_progressbar.addWidget(self.label_info, 6, 0, 1, 1)

        self.label_progress_xvideos = QLabel(self.scrollAreaWidgetContents)
        self.label_progress_xvideos.setObjectName(u"label_progress_xvideos")
        self.label_progress_xvideos.setMinimumSize(QSize(0, 30))

        self.gridlayout_progressbar.addWidget(self.label_progress_xvideos, 4, 0, 1, 1)

        self.label_progress_pornhub = QLabel(self.scrollAreaWidgetContents)
        self.label_progress_pornhub.setObjectName(u"label_progress_pornhub")
        sizePolicy6.setHeightForWidth(self.label_progress_pornhub.sizePolicy().hasHeightForWidth())
        self.label_progress_pornhub.setSizePolicy(sizePolicy6)
        self.label_progress_pornhub.setMinimumSize(QSize(0, 30))

        self.gridlayout_progressbar.addWidget(self.label_progress_pornhub, 0, 0, 1, 1)

        self.lineedit_download_info = QLineEdit(self.scrollAreaWidgetContents)
        self.lineedit_download_info.setObjectName(u"lineedit_download_info")
        self.lineedit_download_info.setReadOnly(True)

        self.gridlayout_progressbar.addWidget(self.lineedit_download_info, 6, 1, 1, 1)

        self.label_progress_xnxx = QLabel(self.scrollAreaWidgetContents)
        self.label_progress_xnxx.setObjectName(u"label_progress_xnxx")
        self.label_progress_xnxx.setMinimumSize(QSize(0, 30))

        self.gridlayout_progressbar.addWidget(self.label_progress_xnxx, 3, 0, 1, 1)

        self.label_progress_hqporner = QLabel(self.scrollAreaWidgetContents)
        self.label_progress_hqporner.setObjectName(u"label_progress_hqporner")
        sizePolicy6.setHeightForWidth(self.label_progress_hqporner.sizePolicy().hasHeightForWidth())
        self.label_progress_hqporner.setSizePolicy(sizePolicy6)
        self.label_progress_hqporner.setMinimumSize(QSize(0, 30))

        self.gridlayout_progressbar.addWidget(self.label_progress_hqporner, 1, 0, 1, 1)

        self.label_progress_spankbang = QLabel(self.scrollAreaWidgetContents)
        self.label_progress_spankbang.setObjectName(u"label_progress_spankbang")
        self.label_progress_spankbang.setMinimumSize(QSize(0, 30))

        self.gridlayout_progressbar.addWidget(self.label_progress_spankbang, 5, 0, 1, 1)

        self.verticalspacer_progress_bars = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridlayout_progressbar.addItem(self.verticalspacer_progress_bars, 7, 1, 1, 1)


        self.gridLayout_18.addLayout(self.gridlayout_progressbar, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stacked_widget_top.addWidget(self.page_progressbars)
        self.page_tools = QWidget()
        self.page_tools.setObjectName(u"page_tools")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.page_tools.sizePolicy().hasHeightForWidth())
        self.page_tools.setSizePolicy(sizePolicy8)
        self.page_tools.setMinimumSize(QSize(100, 30))
        self.gridLayout_29 = QGridLayout(self.page_tools)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridlayout_tools = QGridLayout()
        self.gridlayout_tools.setSpacing(6)
        self.gridlayout_tools.setObjectName(u"gridlayout_tools")
        self.gridlayout_tools.setContentsMargins(-1, 14, -1, -1)
        self.button_get_brazzers_videos = QPushButton(self.page_tools)
        self.button_get_brazzers_videos.setObjectName(u"button_get_brazzers_videos")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.button_get_brazzers_videos.sizePolicy().hasHeightForWidth())
        self.button_get_brazzers_videos.setSizePolicy(sizePolicy9)
        self.button_get_brazzers_videos.setMinimumSize(QSize(0, 0))
        self.button_get_brazzers_videos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.button_get_brazzers_videos, 3, 1, 1, 2)

        self.radio_top_porn_month = QRadioButton(self.page_tools)
        self.radio_top_porn_month.setObjectName(u"radio_top_porn_month")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.radio_top_porn_month.sizePolicy().hasHeightForWidth())
        self.radio_top_porn_month.setSizePolicy(sizePolicy10)
        self.radio_top_porn_month.setMinimumSize(QSize(0, 0))
        self.radio_top_porn_month.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.radio_top_porn_month, 0, 2, 1, 1)

        self.button_list_categories = QPushButton(self.page_tools)
        self.button_list_categories.setObjectName(u"button_list_categories")
        sizePolicy10.setHeightForWidth(self.button_list_categories.sizePolicy().hasHeightForWidth())
        self.button_list_categories.setSizePolicy(sizePolicy10)
        self.button_list_categories.setMinimumSize(QSize(0, 0))
        self.button_list_categories.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.button_list_categories, 1, 4, 1, 1)

        self.button_eporner_category_get_videos = QPushButton(self.page_tools)
        self.button_eporner_category_get_videos.setObjectName(u"button_eporner_category_get_videos")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(2)
        sizePolicy11.setHeightForWidth(self.button_eporner_category_get_videos.sizePolicy().hasHeightForWidth())
        self.button_eporner_category_get_videos.setSizePolicy(sizePolicy11)
        self.button_eporner_category_get_videos.setMinimumSize(QSize(0, 0))
        self.button_eporner_category_get_videos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.button_eporner_category_get_videos, 4, 4, 1, 1)

        self.radio_top_porn_all_time = QRadioButton(self.page_tools)
        self.radio_top_porn_all_time.setObjectName(u"radio_top_porn_all_time")
        sizePolicy10.setHeightForWidth(self.radio_top_porn_all_time.sizePolicy().hasHeightForWidth())
        self.radio_top_porn_all_time.setSizePolicy(sizePolicy10)
        self.radio_top_porn_all_time.setMinimumSize(QSize(0, 0))
        self.radio_top_porn_all_time.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.radio_top_porn_all_time, 0, 3, 1, 1)

        self.label_videos_by_category_eporner = QLabel(self.page_tools)
        self.label_videos_by_category_eporner.setObjectName(u"label_videos_by_category_eporner")
        sizePolicy9.setHeightForWidth(self.label_videos_by_category_eporner.sizePolicy().hasHeightForWidth())
        self.label_videos_by_category_eporner.setSizePolicy(sizePolicy9)
        self.label_videos_by_category_eporner.setMinimumSize(QSize(100, 0))

        self.gridlayout_tools.addWidget(self.label_videos_by_category_eporner, 4, 0, 1, 1)

        self.button_list_categories_eporner = QPushButton(self.page_tools)
        self.button_list_categories_eporner.setObjectName(u"button_list_categories_eporner")
        sizePolicy10.setHeightForWidth(self.button_list_categories_eporner.sizePolicy().hasHeightForWidth())
        self.button_list_categories_eporner.setSizePolicy(sizePolicy10)
        self.button_list_categories_eporner.setMinimumSize(QSize(0, 0))
        self.button_list_categories_eporner.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.button_list_categories_eporner, 4, 3, 1, 1)

        self.label_videos_by_category = QLabel(self.page_tools)
        self.label_videos_by_category.setObjectName(u"label_videos_by_category")
        sizePolicy9.setHeightForWidth(self.label_videos_by_category.sizePolicy().hasHeightForWidth())
        self.label_videos_by_category.setSizePolicy(sizePolicy9)
        self.label_videos_by_category.setMinimumSize(QSize(0, 0))

        self.gridlayout_tools.addWidget(self.label_videos_by_category, 1, 0, 1, 1)

        self.lineedit_hqporner_category = QLineEdit(self.page_tools)
        self.lineedit_hqporner_category.setObjectName(u"lineedit_hqporner_category")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(4)
        sizePolicy12.setHeightForWidth(self.lineedit_hqporner_category.sizePolicy().hasHeightForWidth())
        self.lineedit_hqporner_category.setSizePolicy(sizePolicy12)
        self.lineedit_hqporner_category.setMinimumSize(QSize(100, 0))

        self.gridlayout_tools.addWidget(self.lineedit_hqporner_category, 1, 1, 1, 2)

        self.radio_top_porn_week = QRadioButton(self.page_tools)
        self.radio_top_porn_week.setObjectName(u"radio_top_porn_week")
        sizePolicy10.setHeightForWidth(self.radio_top_porn_week.sizePolicy().hasHeightForWidth())
        self.radio_top_porn_week.setSizePolicy(sizePolicy10)
        self.radio_top_porn_week.setMinimumSize(QSize(0, 0))
        self.radio_top_porn_week.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_top_porn_week.setChecked(True)

        self.gridlayout_tools.addWidget(self.radio_top_porn_week, 0, 1, 1, 1)

        self.lineedit_videos_by_category_eporner = QLineEdit(self.page_tools)
        self.lineedit_videos_by_category_eporner.setObjectName(u"lineedit_videos_by_category_eporner")
        sizePolicy12.setHeightForWidth(self.lineedit_videos_by_category_eporner.sizePolicy().hasHeightForWidth())
        self.lineedit_videos_by_category_eporner.setSizePolicy(sizePolicy12)
        self.lineedit_videos_by_category_eporner.setMinimumSize(QSize(100, 0))

        self.gridlayout_tools.addWidget(self.lineedit_videos_by_category_eporner, 4, 1, 1, 2)

        self.button_hqporner_category_get_videos = QPushButton(self.page_tools)
        self.button_hqporner_category_get_videos.setObjectName(u"button_hqporner_category_get_videos")
        sizePolicy11.setHeightForWidth(self.button_hqporner_category_get_videos.sizePolicy().hasHeightForWidth())
        self.button_hqporner_category_get_videos.setSizePolicy(sizePolicy11)
        self.button_hqporner_category_get_videos.setMinimumSize(QSize(0, 0))
        self.button_hqporner_category_get_videos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.button_hqporner_category_get_videos, 1, 3, 1, 1)

        self.labe_get_random_video = QLabel(self.page_tools)
        self.labe_get_random_video.setObjectName(u"labe_get_random_video")
        sizePolicy9.setHeightForWidth(self.labe_get_random_video.sizePolicy().hasHeightForWidth())
        self.labe_get_random_video.setSizePolicy(sizePolicy9)
        self.labe_get_random_video.setMinimumSize(QSize(0, 0))

        self.gridlayout_tools.addWidget(self.labe_get_random_video, 2, 0, 1, 1)

        self.button_top_porn_get_videos = QPushButton(self.page_tools)
        self.button_top_porn_get_videos.setObjectName(u"button_top_porn_get_videos")
        sizePolicy10.setHeightForWidth(self.button_top_porn_get_videos.sizePolicy().hasHeightForWidth())
        self.button_top_porn_get_videos.setSizePolicy(sizePolicy10)
        self.button_top_porn_get_videos.setMinimumSize(QSize(0, 0))
        self.button_top_porn_get_videos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.button_top_porn_get_videos, 0, 4, 1, 1)

        self.label_get_brazzers_videos = QLabel(self.page_tools)
        self.label_get_brazzers_videos.setObjectName(u"label_get_brazzers_videos")
        sizePolicy9.setHeightForWidth(self.label_get_brazzers_videos.sizePolicy().hasHeightForWidth())
        self.label_get_brazzers_videos.setSizePolicy(sizePolicy9)
        self.label_get_brazzers_videos.setMinimumSize(QSize(0, 0))

        self.gridlayout_tools.addWidget(self.label_get_brazzers_videos, 3, 0, 1, 1)

        self.label_get_top_porn = QLabel(self.page_tools)
        self.label_get_top_porn.setObjectName(u"label_get_top_porn")
        sizePolicy9.setHeightForWidth(self.label_get_top_porn.sizePolicy().hasHeightForWidth())
        self.label_get_top_porn.setSizePolicy(sizePolicy9)
        self.label_get_top_porn.setMinimumSize(QSize(0, 0))

        self.gridlayout_tools.addWidget(self.label_get_top_porn, 0, 0, 1, 1)

        self.button_get_random_videos = QPushButton(self.page_tools)
        self.button_get_random_videos.setObjectName(u"button_get_random_videos")
        sizePolicy9.setHeightForWidth(self.button_get_random_videos.sizePolicy().hasHeightForWidth())
        self.button_get_random_videos.setSizePolicy(sizePolicy9)
        self.button_get_random_videos.setMinimumSize(QSize(0, 0))
        self.button_get_random_videos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tools.addWidget(self.button_get_random_videos, 2, 1, 1, 2)


        self.gridLayout_29.addLayout(self.gridlayout_tools, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.stacked_widget_top.addWidget(self.page_tools)

        self.verticalLayout_3.addWidget(self.stacked_widget_top)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollarea_treewidget = QScrollArea(self.widget)
        self.scrollarea_treewidget.setObjectName(u"scrollarea_treewidget")
        self.scrollarea_treewidget.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 120, 220))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticallayout_treewidget_settings = QVBoxLayout()
        self.verticallayout_treewidget_settings.setSpacing(0)
        self.verticallayout_treewidget_settings.setObjectName(u"verticallayout_treewidget_settings")
        self.treeWidget = QTreeWidget(self.scrollAreaWidgetContents_3)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Title");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy13)
        self.treeWidget.setMinimumSize(QSize(100, 200))

        self.verticallayout_treewidget_settings.addWidget(self.treeWidget)


        self.gridLayout_4.addLayout(self.verticallayout_treewidget_settings, 1, 0, 1, 1)

        self.scrollarea_treewidget.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollarea_treewidget)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.gridlayout_tree_settings = QGridLayout()
        self.gridlayout_tree_settings.setObjectName(u"gridlayout_tree_settings")
        self.button_tree_download = QPushButton(self.widget)
        self.button_tree_download.setObjectName(u"button_tree_download")
        sizePolicy1.setHeightForWidth(self.button_tree_download.sizePolicy().hasHeightForWidth())
        self.button_tree_download.setSizePolicy(sizePolicy1)
        self.button_tree_download.setMinimumSize(QSize(0, 30))
        self.button_tree_download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_tree_download.setStyleSheet(u"")

        self.gridlayout_tree_settings.addWidget(self.button_tree_download, 3, 0, 1, 3)

        self.button_tree_select_range = QPushButton(self.widget)
        self.button_tree_select_range.setObjectName(u"button_tree_select_range")
        sizePolicy1.setHeightForWidth(self.button_tree_select_range.sizePolicy().hasHeightForWidth())
        self.button_tree_select_range.setSizePolicy(sizePolicy1)
        self.button_tree_select_range.setMinimumSize(QSize(0, 30))
        self.button_tree_select_range.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_tree_select_range.setStyleSheet(u"")

        self.gridlayout_tree_settings.addWidget(self.button_tree_select_range, 2, 0, 1, 1)

        self.checkbox_tree_show_videos_reversed = QCheckBox(self.widget)
        self.checkbox_tree_show_videos_reversed.setObjectName(u"checkbox_tree_show_videos_reversed")
        self.checkbox_tree_show_videos_reversed.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridlayout_tree_settings.addWidget(self.checkbox_tree_show_videos_reversed, 1, 1, 1, 1)

        self.button_range_apply_everything = QPushButton(self.widget)
        self.button_range_apply_everything.setObjectName(u"button_range_apply_everything")

        self.gridlayout_tree_settings.addWidget(self.button_range_apply_everything, 2, 1, 1, 1)

        self.button_tree_export_video_urls = QPushButton(self.widget)
        self.button_tree_export_video_urls.setObjectName(u"button_tree_export_video_urls")

        self.gridlayout_tree_settings.addWidget(self.button_tree_export_video_urls, 1, 2, 1, 1)

        self.radio_tree_show_title = QRadioButton(self.widget)
        self.radio_tree_show_title.setObjectName(u"radio_tree_show_title")
        sizePolicy6.setHeightForWidth(self.radio_tree_show_title.sizePolicy().hasHeightForWidth())
        self.radio_tree_show_title.setSizePolicy(sizePolicy6)
        self.radio_tree_show_title.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_tree_show_title.setChecked(True)

        self.gridlayout_tree_settings.addWidget(self.radio_tree_show_title, 0, 0, 1, 1)

        self.button_tree_unselect_all = QPushButton(self.widget)
        self.button_tree_unselect_all.setObjectName(u"button_tree_unselect_all")
        sizePolicy1.setHeightForWidth(self.button_tree_unselect_all.sizePolicy().hasHeightForWidth())
        self.button_tree_unselect_all.setSizePolicy(sizePolicy1)
        self.button_tree_unselect_all.setMinimumSize(QSize(0, 30))
        self.button_tree_unselect_all.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_tree_unselect_all.setStyleSheet(u"")

        self.gridlayout_tree_settings.addWidget(self.button_tree_unselect_all, 2, 2, 1, 1)

        self.radio_tree_show_all = QRadioButton(self.widget)
        self.radio_tree_show_all.setObjectName(u"radio_tree_show_all")
        sizePolicy6.setHeightForWidth(self.radio_tree_show_all.sizePolicy().hasHeightForWidth())
        self.radio_tree_show_all.setSizePolicy(sizePolicy6)
        self.radio_tree_show_all.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radio_tree_show_all.setStyleSheet(u"")
        self.radio_tree_show_all.setCheckable(True)
        self.radio_tree_show_all.setChecked(False)

        self.gridlayout_tree_settings.addWidget(self.radio_tree_show_all, 0, 1, 1, 1)

        self.button_tree_stop = QPushButton(self.widget)
        self.button_tree_stop.setObjectName(u"button_tree_stop")
        sizePolicy1.setHeightForWidth(self.button_tree_stop.sizePolicy().hasHeightForWidth())
        self.button_tree_stop.setSizePolicy(sizePolicy1)
        self.button_tree_stop.setMinimumSize(QSize(0, 30))

        self.gridlayout_tree_settings.addWidget(self.button_tree_stop, 0, 2, 1, 1)

        self.checkbox_tree_do_not_clear_videos = QCheckBox(self.widget)
        self.checkbox_tree_do_not_clear_videos.setObjectName(u"checkbox_tree_do_not_clear_videos")

        self.gridlayout_tree_settings.addWidget(self.checkbox_tree_do_not_clear_videos, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridlayout_tree_settings)


        self.gridLayout_8.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stacked_widget_main.addWidget(self.widget)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.gridLayout_25 = QGridLayout(self.page_settings)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.settings_verticallayout = QVBoxLayout()
        self.settings_verticallayout.setSpacing(0)
        self.settings_verticallayout.setObjectName(u"settings_verticallayout")
        self.settings_scrollarea = QScrollArea(self.page_settings)
        self.settings_scrollarea.setObjectName(u"settings_scrollarea")
        self.settings_scrollarea.setWidgetResizable(True)
        self.settings_scrollarea_widget_contents = QWidget()
        self.settings_scrollarea_widget_contents.setObjectName(u"settings_scrollarea_widget_contents")
        self.settings_scrollarea_widget_contents.setGeometry(QRect(0, 0, 1385, 803))
        self.gridLayout_19 = QGridLayout(self.settings_scrollarea_widget_contents)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.settings_scrollarea_gridlayout = QGridLayout()
        self.settings_scrollarea_gridlayout.setObjectName(u"settings_scrollarea_gridlayout")
        self.settings_groupbox_performance = QGroupBox(self.settings_scrollarea_widget_contents)
        self.settings_groupbox_performance.setObjectName(u"settings_groupbox_performance")
        self.gridLayout_9 = QGridLayout(self.settings_groupbox_performance)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_simultaneous_downloads = QHBoxLayout()
        self.horizontallayout_simultaneous_downloads.setObjectName(u"horizontallayout_simultaneous_downloads")
        self.label_semaphore = QLabel(self.settings_groupbox_performance)
        self.label_semaphore.setObjectName(u"label_semaphore")

        self.horizontallayout_simultaneous_downloads.addWidget(self.label_semaphore)

        self.spinbox_semaphore = QSpinBox(self.settings_groupbox_performance)
        self.spinbox_semaphore.setObjectName(u"spinbox_semaphore")
        self.spinbox_semaphore.setMinimum(1)
        self.spinbox_semaphore.setMaximum(5000)

        self.horizontallayout_simultaneous_downloads.addWidget(self.spinbox_semaphore)

        self.button_semaphore_help = QPushButton(self.settings_groupbox_performance)
        self.button_semaphore_help.setObjectName(u"button_semaphore_help")
        self.button_semaphore_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_simultaneous_downloads.addWidget(self.button_semaphore_help)


        self.gridLayout_9.addLayout(self.horizontallayout_simultaneous_downloads, 2, 0, 1, 1)

        self.horizontallayout_maximal_workers = QHBoxLayout()
        self.horizontallayout_maximal_workers.setObjectName(u"horizontallayout_maximal_workers")
        self.label_maximal_workers = QLabel(self.settings_groupbox_performance)
        self.label_maximal_workers.setObjectName(u"label_maximal_workers")

        self.horizontallayout_maximal_workers.addWidget(self.label_maximal_workers)

        self.spinbox_maximal_workers = QSpinBox(self.settings_groupbox_performance)
        self.spinbox_maximal_workers.setObjectName(u"spinbox_maximal_workers")
        self.spinbox_maximal_workers.setMinimum(1)
        self.spinbox_maximal_workers.setMaximum(5000)

        self.horizontallayout_maximal_workers.addWidget(self.spinbox_maximal_workers)

        self.button_workers_help = QPushButton(self.settings_groupbox_performance)
        self.button_workers_help.setObjectName(u"button_workers_help")
        self.button_workers_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_maximal_workers.addWidget(self.button_workers_help)


        self.gridLayout_9.addLayout(self.horizontallayout_maximal_workers, 4, 0, 1, 1)

        self.horizontallayout_maximal_timeout = QHBoxLayout()
        self.horizontallayout_maximal_timeout.setObjectName(u"horizontallayout_maximal_timeout")
        self.label_maximal_timeout = QLabel(self.settings_groupbox_performance)
        self.label_maximal_timeout.setObjectName(u"label_maximal_timeout")

        self.horizontallayout_maximal_timeout.addWidget(self.label_maximal_timeout)

        self.spinbox_maximal_timeout = QSpinBox(self.settings_groupbox_performance)
        self.spinbox_maximal_timeout.setObjectName(u"spinbox_maximal_timeout")
        self.spinbox_maximal_timeout.setMinimum(5)
        self.spinbox_maximal_timeout.setMaximum(5000)

        self.horizontallayout_maximal_timeout.addWidget(self.spinbox_maximal_timeout)

        self.button_timeout_help = QPushButton(self.settings_groupbox_performance)
        self.button_timeout_help.setObjectName(u"button_timeout_help")
        self.button_timeout_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_maximal_timeout.addWidget(self.button_timeout_help)


        self.gridLayout_9.addLayout(self.horizontallayout_maximal_timeout, 5, 0, 1, 1)

        self.horizontallayout_maximal_retries = QHBoxLayout()
        self.horizontallayout_maximal_retries.setObjectName(u"horizontallayout_maximal_retries")
        self.label_maximal_retries = QLabel(self.settings_groupbox_performance)
        self.label_maximal_retries.setObjectName(u"label_maximal_retries")

        self.horizontallayout_maximal_retries.addWidget(self.label_maximal_retries)

        self.spinbox_maximal_retries = QSpinBox(self.settings_groupbox_performance)
        self.spinbox_maximal_retries.setObjectName(u"spinbox_maximal_retries")
        self.spinbox_maximal_retries.setMinimum(5)
        self.spinbox_maximal_retries.setMaximum(5000)

        self.horizontallayout_maximal_retries.addWidget(self.spinbox_maximal_retries)

        self.button_timeout_maximal_retries_help = QPushButton(self.settings_groupbox_performance)
        self.button_timeout_maximal_retries_help.setObjectName(u"button_timeout_maximal_retries_help")
        self.button_timeout_maximal_retries_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_maximal_retries.addWidget(self.button_timeout_maximal_retries_help)


        self.gridLayout_9.addLayout(self.horizontallayout_maximal_retries, 6, 0, 1, 1)

        self.horizontallayout_pornhub_delay = QHBoxLayout()
        self.horizontallayout_pornhub_delay.setObjectName(u"horizontallayout_pornhub_delay")
        self.label_pornhub_delay = QLabel(self.settings_groupbox_performance)
        self.label_pornhub_delay.setObjectName(u"label_pornhub_delay")

        self.horizontallayout_pornhub_delay.addWidget(self.label_pornhub_delay)

        self.spinbox_pornhub_delay = QSpinBox(self.settings_groupbox_performance)
        self.spinbox_pornhub_delay.setObjectName(u"spinbox_pornhub_delay")
        self.spinbox_pornhub_delay.setMinimum(0)
        self.spinbox_pornhub_delay.setMaximum(5000)

        self.horizontallayout_pornhub_delay.addWidget(self.spinbox_pornhub_delay)

        self.button_pornhub_delay_help = QPushButton(self.settings_groupbox_performance)
        self.button_pornhub_delay_help.setObjectName(u"button_pornhub_delay_help")
        self.button_pornhub_delay_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_pornhub_delay.addWidget(self.button_pornhub_delay_help)


        self.gridLayout_9.addLayout(self.horizontallayout_pornhub_delay, 3, 0, 1, 1)

        self.horizontallayout_threading_mode = QHBoxLayout()
        self.horizontallayout_threading_mode.setObjectName(u"horizontallayout_threading_mode")
        self.label_threading_mode = QLabel(self.settings_groupbox_performance)
        self.label_threading_mode.setObjectName(u"label_threading_mode")
        sizePolicy6.setHeightForWidth(self.label_threading_mode.sizePolicy().hasHeightForWidth())
        self.label_threading_mode.setSizePolicy(sizePolicy6)

        self.horizontallayout_threading_mode.addWidget(self.label_threading_mode)

        self.radio_threading_mode_high_performance = QRadioButton(self.settings_groupbox_performance)
        self.radio_threading_mode_high_performance.setObjectName(u"radio_threading_mode_high_performance")
        self.radio_threading_mode_high_performance.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_threading_mode.addWidget(self.radio_threading_mode_high_performance)

        self.radio_threading_mode_ffmpeg = QRadioButton(self.settings_groupbox_performance)
        self.radio_threading_mode_ffmpeg.setObjectName(u"radio_threading_mode_ffmpeg")
        self.radio_threading_mode_ffmpeg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_threading_mode.addWidget(self.radio_threading_mode_ffmpeg)

        self.radio_threading_mode_default = QRadioButton(self.settings_groupbox_performance)
        self.radio_threading_mode_default.setObjectName(u"radio_threading_mode_default")
        self.radio_threading_mode_default.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_threading_mode.addWidget(self.radio_threading_mode_default)

        self.button_threading_mode_help = QPushButton(self.settings_groupbox_performance)
        self.button_threading_mode_help.setObjectName(u"button_threading_mode_help")
        self.button_threading_mode_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontallayout_threading_mode.addWidget(self.button_threading_mode_help)


        self.gridLayout_9.addLayout(self.horizontallayout_threading_mode, 1, 0, 1, 1)


        self.settings_scrollarea_gridlayout.addWidget(self.settings_groupbox_performance, 0, 0, 1, 1)

        self.settings_groupbox_ui = QGroupBox(self.settings_scrollarea_widget_contents)
        self.settings_groupbox_ui.setObjectName(u"settings_groupbox_ui")
        self.gridLayout_12 = QGridLayout(self.settings_groupbox_ui)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_ui_language = QLabel(self.settings_groupbox_ui)
        self.label_ui_language.setObjectName(u"label_ui_language")
        sizePolicy6.setHeightForWidth(self.label_ui_language.sizePolicy().hasHeightForWidth())
        self.label_ui_language.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.label_ui_language, 0, 0, 1, 1)

        self.radio_ui_language_system_default = QRadioButton(self.settings_groupbox_ui)
        self.radio_ui_language_system_default.setObjectName(u"radio_ui_language_system_default")
        self.radio_ui_language_system_default.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.radio_ui_language_system_default, 0, 1, 1, 1)

        self.radio_ui_language_english = QRadioButton(self.settings_groupbox_ui)
        self.radio_ui_language_english.setObjectName(u"radio_ui_language_english")
        self.radio_ui_language_english.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.radio_ui_language_english, 0, 2, 1, 1)

        self.radio_ui_language_french = QRadioButton(self.settings_groupbox_ui)
        self.radio_ui_language_french.setObjectName(u"radio_ui_language_french")
        self.radio_ui_language_french.setEnabled(True)

        self.gridLayout_3.addWidget(self.radio_ui_language_french, 0, 5, 1, 1)

        self.radio_ui_language_chinese_simplified = QRadioButton(self.settings_groupbox_ui)
        self.radio_ui_language_chinese_simplified.setObjectName(u"radio_ui_language_chinese_simplified")
        self.radio_ui_language_chinese_simplified.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.radio_ui_language_chinese_simplified, 0, 4, 1, 1)

        self.radio_ui_language_german = QRadioButton(self.settings_groupbox_ui)
        self.radio_ui_language_german.setObjectName(u"radio_ui_language_german")
        self.radio_ui_language_german.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.radio_ui_language_german, 0, 3, 1, 1)

        self.label_settings_design = QLabel(self.settings_groupbox_ui)
        self.label_settings_design.setObjectName(u"label_settings_design")

        self.gridLayout_3.addWidget(self.label_settings_design, 1, 0, 1, 1)

        self.radio_ui_design_native = QRadioButton(self.settings_groupbox_ui)
        self.radio_ui_design_native.setObjectName(u"radio_ui_design_native")

        self.gridLayout_3.addWidget(self.radio_ui_design_native, 1, 1, 1, 1)

        self.radio_ui_design_dark_mode = QRadioButton(self.settings_groupbox_ui)
        self.radio_ui_design_dark_mode.setObjectName(u"radio_ui_design_dark_mode")

        self.gridLayout_3.addWidget(self.radio_ui_design_dark_mode, 1, 2, 1, 1)

        self.radio_ui_design_light_mode = QRadioButton(self.settings_groupbox_ui)
        self.radio_ui_design_light_mode.setObjectName(u"radio_ui_design_light_mode")

        self.gridLayout_3.addWidget(self.radio_ui_design_light_mode, 1, 3, 1, 3)


        self.gridLayout_12.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.settings_scrollarea_gridlayout.addWidget(self.settings_groupbox_ui, 3, 0, 1, 1)

        self.settings_groupbox_system_pornfetch = QGroupBox(self.settings_scrollarea_widget_contents)
        self.settings_groupbox_system_pornfetch.setObjectName(u"settings_groupbox_system_pornfetch")
        self.gridLayout_7 = QGridLayout(self.settings_groupbox_system_pornfetch)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.settings_checkbox_system_update_checks = QCheckBox(self.settings_groupbox_system_pornfetch)
        self.settings_checkbox_system_update_checks.setObjectName(u"settings_checkbox_system_update_checks")

        self.gridLayout_13.addWidget(self.settings_checkbox_system_update_checks, 2, 1, 1, 1)

        self.settings_checkbox_internet_checks = QCheckBox(self.settings_groupbox_system_pornfetch)
        self.settings_checkbox_internet_checks.setObjectName(u"settings_checkbox_internet_checks")

        self.gridLayout_13.addWidget(self.settings_checkbox_internet_checks, 2, 2, 1, 1)

        self.checkbox_settings_system_anonymous_mode = QCheckBox(self.settings_groupbox_system_pornfetch)
        self.checkbox_settings_system_anonymous_mode.setObjectName(u"checkbox_settings_system_anonymous_mode")

        self.gridLayout_13.addWidget(self.checkbox_settings_system_anonymous_mode, 3, 2, 1, 1)

        self.label_settings_system_privacy = QLabel(self.settings_groupbox_system_pornfetch)
        self.label_settings_system_privacy.setObjectName(u"label_settings_system_privacy")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.label_settings_system_privacy.sizePolicy().hasHeightForWidth())
        self.label_settings_system_privacy.setSizePolicy(sizePolicy14)

        self.gridLayout_13.addWidget(self.label_settings_system_privacy, 3, 0, 1, 1)

        self.checkbox_settings_system_enable_tor = QCheckBox(self.settings_groupbox_system_pornfetch)
        self.checkbox_settings_system_enable_tor.setObjectName(u"checkbox_settings_system_enable_tor")

        self.gridLayout_13.addWidget(self.checkbox_settings_system_enable_tor, 3, 1, 1, 1)

        self.settings_label_startup = QLabel(self.settings_groupbox_system_pornfetch)
        self.settings_label_startup.setObjectName(u"settings_label_startup")
        sizePolicy14.setHeightForWidth(self.settings_label_startup.sizePolicy().hasHeightForWidth())
        self.settings_label_startup.setSizePolicy(sizePolicy14)

        self.gridLayout_13.addWidget(self.settings_label_startup, 2, 0, 1, 1)

        self.button_settings_help_tor = QPushButton(self.settings_groupbox_system_pornfetch)
        self.button_settings_help_tor.setObjectName(u"button_settings_help_tor")

        self.gridLayout_13.addWidget(self.button_settings_help_tor, 4, 1, 1, 1)

        self.settings_button_help_anonymous_mode = QPushButton(self.settings_groupbox_system_pornfetch)
        self.settings_button_help_anonymous_mode.setObjectName(u"settings_button_help_anonymous_mode")

        self.gridLayout_13.addWidget(self.settings_button_help_anonymous_mode, 4, 2, 1, 1)

        self.button_download_ffmpeg = QPushButton(self.settings_groupbox_system_pornfetch)
        self.button_download_ffmpeg.setObjectName(u"button_download_ffmpeg")

        self.gridLayout_13.addWidget(self.button_download_ffmpeg, 0, 0, 1, 3)

        self.button_install_pornfetch = QPushButton(self.settings_groupbox_system_pornfetch)
        self.button_install_pornfetch.setObjectName(u"button_install_pornfetch")

        self.gridLayout_13.addWidget(self.button_install_pornfetch, 1, 0, 1, 3)


        self.gridLayout_7.addLayout(self.gridLayout_13, 2, 0, 1, 1)


        self.settings_scrollarea_gridlayout.addWidget(self.settings_groupbox_system_pornfetch, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupbox_videos = QGroupBox(self.settings_scrollarea_widget_contents)
        self.groupbox_videos.setObjectName(u"groupbox_videos")
        self.gridLayout_10 = QGridLayout(self.groupbox_videos)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.radio_directory_system_no = QRadioButton(self.groupbox_videos)
        self.radio_directory_system_no.setObjectName(u"radio_directory_system_no")
        self.radio_directory_system_no.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.radio_directory_system_no, 2, 2, 1, 1)

        self.button_directory_system_help = QPushButton(self.groupbox_videos)
        self.button_directory_system_help.setObjectName(u"button_directory_system_help")
        self.button_directory_system_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.button_directory_system_help, 2, 3, 1, 2)

        self.radio_directory_system_yes = QRadioButton(self.groupbox_videos)
        self.radio_directory_system_yes.setObjectName(u"radio_directory_system_yes")
        self.radio_directory_system_yes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.radio_directory_system_yes, 2, 1, 1, 1)

        self.button_help_model_videos = QPushButton(self.groupbox_videos)
        self.button_help_model_videos.setObjectName(u"button_help_model_videos")

        self.gridLayout.addWidget(self.button_help_model_videos, 5, 4, 1, 1)

        self.radio_skip_existing_files_yes = QRadioButton(self.groupbox_videos)
        self.radio_skip_existing_files_yes.setObjectName(u"radio_skip_existing_files_yes")

        self.gridLayout.addWidget(self.radio_skip_existing_files_yes, 3, 1, 1, 1)

        self.labe_settings_videos_model = QLabel(self.groupbox_videos)
        self.labe_settings_videos_model.setObjectName(u"labe_settings_videos_model")

        self.gridLayout.addWidget(self.labe_settings_videos_model, 5, 0, 1, 1)

        self.radio_quality_half = QRadioButton(self.groupbox_videos)
        self.radio_quality_half.setObjectName(u"radio_quality_half")
        self.radio_quality_half.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.radio_quality_half, 0, 2, 1, 1)

        self.radio_model_both = QRadioButton(self.groupbox_videos)
        self.radio_model_both.setObjectName(u"radio_model_both")

        self.gridLayout.addWidget(self.radio_model_both, 5, 3, 1, 1)

        self.label_output_path = QLabel(self.groupbox_videos)
        self.label_output_path.setObjectName(u"label_output_path")

        self.gridLayout.addWidget(self.label_output_path, 7, 0, 1, 1)

        self.button_output_path_select = QPushButton(self.groupbox_videos)
        self.button_output_path_select.setObjectName(u"button_output_path_select")
        self.button_output_path_select.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.button_output_path_select, 7, 3, 1, 2)

        self.radio_quality_worst = QRadioButton(self.groupbox_videos)
        self.radio_quality_worst.setObjectName(u"radio_quality_worst")
        self.radio_quality_worst.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.radio_quality_worst, 0, 3, 1, 2)

        self.radio_skip_existing_files_no = QRadioButton(self.groupbox_videos)
        self.radio_skip_existing_files_no.setObjectName(u"radio_skip_existing_files_no")

        self.gridLayout.addWidget(self.radio_skip_existing_files_no, 3, 2, 1, 1)

        self.label_directory_system = QLabel(self.groupbox_videos)
        self.label_directory_system.setObjectName(u"label_directory_system")

        self.gridLayout.addWidget(self.label_directory_system, 2, 0, 1, 1)

        self.button_result_limit_help = QPushButton(self.groupbox_videos)
        self.button_result_limit_help.setObjectName(u"button_result_limit_help")
        self.button_result_limit_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.button_result_limit_help, 6, 3, 1, 2)

        self.radio_model_featured = QRadioButton(self.groupbox_videos)
        self.radio_model_featured.setObjectName(u"radio_model_featured")

        self.gridLayout.addWidget(self.radio_model_featured, 5, 2, 1, 1)

        self.lineedit_output_path = QLineEdit(self.groupbox_videos)
        self.lineedit_output_path.setObjectName(u"lineedit_output_path")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.lineedit_output_path.sizePolicy().hasHeightForWidth())
        self.lineedit_output_path.setSizePolicy(sizePolicy15)

        self.gridLayout.addWidget(self.lineedit_output_path, 7, 1, 1, 2)

        self.radio_quality_best = QRadioButton(self.groupbox_videos)
        self.radio_quality_best.setObjectName(u"radio_quality_best")
        self.radio_quality_best.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.radio_quality_best, 0, 1, 1, 1)

        self.label_skip_existing_files = QLabel(self.groupbox_videos)
        self.label_skip_existing_files.setObjectName(u"label_skip_existing_files")

        self.gridLayout.addWidget(self.label_skip_existing_files, 3, 0, 1, 1)

        self.radio_model_uploads = QRadioButton(self.groupbox_videos)
        self.radio_model_uploads.setObjectName(u"radio_model_uploads")

        self.gridLayout.addWidget(self.radio_model_uploads, 5, 1, 1, 1)

        self.button_help_skip_existing_files = QPushButton(self.groupbox_videos)
        self.button_help_skip_existing_files.setObjectName(u"button_help_skip_existing_files")

        self.gridLayout.addWidget(self.button_help_skip_existing_files, 3, 3, 1, 2)

        self.spinbox_treewidget_limit = QSpinBox(self.groupbox_videos)
        self.spinbox_treewidget_limit.setObjectName(u"spinbox_treewidget_limit")
        self.spinbox_treewidget_limit.setMinimum(1)
        self.spinbox_treewidget_limit.setMaximum(5000)

        self.gridLayout.addWidget(self.spinbox_treewidget_limit, 6, 1, 1, 2)

        self.label_quality = QLabel(self.groupbox_videos)
        self.label_quality.setObjectName(u"label_quality")
        sizePolicy6.setHeightForWidth(self.label_quality.sizePolicy().hasHeightForWidth())
        self.label_quality.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.label_quality, 0, 0, 1, 1)

        self.label_searching_limit = QLabel(self.groupbox_videos)
        self.label_searching_limit.setObjectName(u"label_searching_limit")

        self.gridLayout.addWidget(self.label_searching_limit, 6, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout, 6, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupbox_videos)

        self.groupbox_post_processing = QGroupBox(self.settings_scrollarea_widget_contents)
        self.groupbox_post_processing.setObjectName(u"groupbox_post_processing")
        self.gridLayout_14 = QGridLayout(self.groupbox_post_processing)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.radio_settings_post_processing_use_custom_format = QRadioButton(self.groupbox_post_processing)
        self.radio_settings_post_processing_use_custom_format.setObjectName(u"radio_settings_post_processing_use_custom_format")

        self.gridLayout_15.addWidget(self.radio_settings_post_processing_use_custom_format, 0, 1, 1, 1)

        self.radio_settings_post_rocessing_do_not_convert = QRadioButton(self.groupbox_post_processing)
        self.radio_settings_post_rocessing_do_not_convert.setObjectName(u"radio_settings_post_rocessing_do_not_convert")

        self.gridLayout_15.addWidget(self.radio_settings_post_rocessing_do_not_convert, 0, 0, 1, 1)

        self.lineedit_settings_post_processing_use_custom_format = QLineEdit(self.groupbox_post_processing)
        self.lineedit_settings_post_processing_use_custom_format.setObjectName(u"lineedit_settings_post_processing_use_custom_format")

        self.gridLayout_15.addWidget(self.lineedit_settings_post_processing_use_custom_format, 0, 2, 1, 1)

        self.checkbox_settings_post_processing_write_metadata_tags = QCheckBox(self.groupbox_post_processing)
        self.checkbox_settings_post_processing_write_metadata_tags.setObjectName(u"checkbox_settings_post_processing_write_metadata_tags")

        self.gridLayout_15.addWidget(self.checkbox_settings_post_processing_write_metadata_tags, 1, 0, 1, 1)

        self.checkbox_settings_post_processing_unfinished_videos = QCheckBox(self.groupbox_post_processing)
        self.checkbox_settings_post_processing_unfinished_videos.setObjectName(u"checkbox_settings_post_processing_unfinished_videos")

        self.gridLayout_15.addWidget(self.checkbox_settings_post_processing_unfinished_videos, 2, 0, 1, 1)

        self.lineedit_settings_post_processing_unfinished_path_ = QLineEdit(self.groupbox_post_processing)
        self.lineedit_settings_post_processing_unfinished_path_.setObjectName(u"lineedit_settings_post_processing_unfinished_path_")

        self.gridLayout_15.addWidget(self.lineedit_settings_post_processing_unfinished_path_, 2, 1, 1, 1)

        self.button_settings_post_processing_output_path = QPushButton(self.groupbox_post_processing)
        self.button_settings_post_processing_output_path.setObjectName(u"button_settings_post_processing_output_path")

        self.gridLayout_15.addWidget(self.button_settings_post_processing_output_path, 2, 2, 1, 1)

        self.button_help_write_metadata_tags = QPushButton(self.groupbox_post_processing)
        self.button_help_write_metadata_tags.setObjectName(u"button_help_write_metadata_tags")

        self.gridLayout_15.addWidget(self.button_help_write_metadata_tags, 1, 1, 1, 2)


        self.gridLayout_14.addLayout(self.gridLayout_15, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupbox_post_processing)


        self.settings_scrollarea_gridlayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_19.addLayout(self.settings_scrollarea_gridlayout, 0, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_3, 4, 0, 1, 2)

        self.settings_horizontallayout_apply = QHBoxLayout()
        self.settings_horizontallayout_apply.setObjectName(u"settings_horizontallayout_apply")
        self.settings_button_apply = QPushButton(self.settings_scrollarea_widget_contents)
        self.settings_button_apply.setObjectName(u"settings_button_apply")
        self.settings_button_apply.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.settings_horizontallayout_apply.addWidget(self.settings_button_apply)

        self.settings_button_reset = QPushButton(self.settings_scrollarea_widget_contents)
        self.settings_button_reset.setObjectName(u"settings_button_reset")
        self.settings_button_reset.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_button_reset.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(85, 0, 0)/* Green */\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 3px;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(222, 0, 41)/* Lighter green */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(108, 0, 52) /* Dark green */\n"
"}\n"
"")

        self.settings_horizontallayout_apply.addWidget(self.settings_button_reset)


        self.gridLayout_19.addLayout(self.settings_horizontallayout_apply, 2, 0, 2, 2)

        self.settings_scrollarea.setWidget(self.settings_scrollarea_widget_contents)

        self.settings_verticallayout.addWidget(self.settings_scrollarea)


        self.gridLayout_25.addLayout(self.settings_verticallayout, 0, 0, 1, 1)

        self.stacked_widget_main.addWidget(self.page_settings)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.gridLayout_26 = QGridLayout(self.page_credits)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.main_gridlayout_textbrowser = QGridLayout()
        self.main_gridlayout_textbrowser.setObjectName(u"main_gridlayout_textbrowser")
        self.main_textbrowser_credits = QTextBrowser(self.page_credits)
        self.main_textbrowser_credits.setObjectName(u"main_textbrowser_credits")

        self.main_gridlayout_textbrowser.addWidget(self.main_textbrowser_credits, 0, 0, 1, 1)


        self.gridLayout_26.addLayout(self.main_gridlayout_textbrowser, 0, 0, 1, 1)

        self.stacked_widget_main.addWidget(self.page_credits)
        self.page_supported_websites = QWidget()
        self.page_supported_websites.setObjectName(u"page_supported_websites")
        self.gridLayout_11 = QGridLayout(self.page_supported_websites)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.textbrowser_websites = QTextBrowser(self.page_supported_websites)
        self.textbrowser_websites.setObjectName(u"textbrowser_websites")

        self.gridLayout_11.addWidget(self.textbrowser_websites, 0, 0, 1, 1)

        self.stacked_widget_main.addWidget(self.page_supported_websites)

        self.verticallayout_main.addWidget(self.stacked_widget_main)

        self.formlayout_progressbar = QFormLayout()
        self.formlayout_progressbar.setObjectName(u"formlayout_progressbar")
        self.formlayout_progressbar.setHorizontalSpacing(0)
        self.formlayout_progressbar.setVerticalSpacing(0)
        self.main_label_progressbar_total = QLabel(PornFetch_Desktop)
        self.main_label_progressbar_total.setObjectName(u"main_label_progressbar_total")

        self.formlayout_progressbar.setWidget(0, QFormLayout.LabelRole, self.main_label_progressbar_total)

        self.main_progressbar_total = QProgressBar(PornFetch_Desktop)
        self.main_progressbar_total.setObjectName(u"main_progressbar_total")
        sizePolicy7.setHeightForWidth(self.main_progressbar_total.sizePolicy().hasHeightForWidth())
        self.main_progressbar_total.setSizePolicy(sizePolicy7)
        self.main_progressbar_total.setMinimumSize(QSize(300, 0))
        self.main_progressbar_total.setStyleSheet(u"text-align: center; /* Centered text */")
        self.main_progressbar_total.setValue(0)

        self.formlayout_progressbar.setWidget(0, QFormLayout.FieldRole, self.main_progressbar_total)

        self.main_label_progressbar_converting = QLabel(PornFetch_Desktop)
        self.main_label_progressbar_converting.setObjectName(u"main_label_progressbar_converting")

        self.formlayout_progressbar.setWidget(1, QFormLayout.LabelRole, self.main_label_progressbar_converting)

        self.main_progressbar_converting = QProgressBar(PornFetch_Desktop)
        self.main_progressbar_converting.setObjectName(u"main_progressbar_converting")
        self.main_progressbar_converting.setStyleSheet(u"text-align: center; /* Centered text */")
        self.main_progressbar_converting.setValue(0)

        self.formlayout_progressbar.setWidget(1, QFormLayout.FieldRole, self.main_progressbar_converting)


        self.verticallayout_main.addLayout(self.formlayout_progressbar)


        self.gridLayout_16.addLayout(self.verticallayout_main, 0, 0, 1, 1)

        QWidget.setTabOrder(self.lineedit_url, self.lineedit_playlist_url)
        QWidget.setTabOrder(self.lineedit_playlist_url, self.lineedit_model_url)
        QWidget.setTabOrder(self.lineedit_model_url, self.lineedit_file)
        QWidget.setTabOrder(self.lineedit_file, self.lineedit_search_query)
        QWidget.setTabOrder(self.lineedit_search_query, self.lineedit_username)
        QWidget.setTabOrder(self.lineedit_username, self.lineedit_password)
        QWidget.setTabOrder(self.lineedit_password, self.button_login)
        QWidget.setTabOrder(self.button_login, self.button_get_liked_videos)
        QWidget.setTabOrder(self.button_get_liked_videos, self.button_get_watched_videos)
        QWidget.setTabOrder(self.button_get_watched_videos, self.button_get_recommended_videos)
        QWidget.setTabOrder(self.button_get_recommended_videos, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.radio_top_porn_week)
        QWidget.setTabOrder(self.radio_top_porn_week, self.radio_top_porn_month)
        QWidget.setTabOrder(self.radio_top_porn_month, self.radio_top_porn_all_time)
        QWidget.setTabOrder(self.radio_top_porn_all_time, self.button_top_porn_get_videos)
        QWidget.setTabOrder(self.button_top_porn_get_videos, self.lineedit_hqporner_category)
        QWidget.setTabOrder(self.lineedit_hqporner_category, self.button_hqporner_category_get_videos)
        QWidget.setTabOrder(self.button_hqporner_category_get_videos, self.button_list_categories)
        QWidget.setTabOrder(self.button_list_categories, self.radio_threading_mode_high_performance)
        QWidget.setTabOrder(self.radio_threading_mode_high_performance, self.radio_threading_mode_ffmpeg)
        QWidget.setTabOrder(self.radio_threading_mode_ffmpeg, self.radio_threading_mode_default)
        QWidget.setTabOrder(self.radio_threading_mode_default, self.button_threading_mode_help)
        QWidget.setTabOrder(self.button_threading_mode_help, self.spinbox_semaphore)
        QWidget.setTabOrder(self.spinbox_semaphore, self.button_semaphore_help)
        QWidget.setTabOrder(self.button_semaphore_help, self.spinbox_pornhub_delay)
        QWidget.setTabOrder(self.spinbox_pornhub_delay, self.button_pornhub_delay_help)
        QWidget.setTabOrder(self.button_pornhub_delay_help, self.spinbox_maximal_workers)
        QWidget.setTabOrder(self.spinbox_maximal_workers, self.button_workers_help)
        QWidget.setTabOrder(self.button_workers_help, self.spinbox_maximal_timeout)
        QWidget.setTabOrder(self.spinbox_maximal_timeout, self.button_timeout_help)
        QWidget.setTabOrder(self.button_timeout_help, self.spinbox_maximal_retries)
        QWidget.setTabOrder(self.spinbox_maximal_retries, self.button_timeout_maximal_retries_help)
        QWidget.setTabOrder(self.button_timeout_maximal_retries_help, self.settings_button_apply)
        QWidget.setTabOrder(self.settings_button_apply, self.settings_button_reset)
        QWidget.setTabOrder(self.settings_button_reset, self.main_textbrowser_credits)
        QWidget.setTabOrder(self.main_textbrowser_credits, self.textbrowser_websites)

        self.retranslateUi(PornFetch_Desktop)

        self.stacked_widget_main.setCurrentIndex(1)
        self.stacked_widget_top.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(PornFetch_Desktop)
    # setupUi

    def retranslateUi(self, PornFetch_Desktop):
        PornFetch_Desktop.setWindowTitle(QCoreApplication.translate("PornFetch_Desktop", u"Porn Fetch V3.5 (C) Johannes Habel GPL 3", None))
        self.main_button_switch_home.setText("")
        self.main_button_switch_account.setText("")
        self.main_button_switch_tools.setText("")
        self.main_button_switch_settings.setText("")
        self.main_button_switch_credits.setText("")
        self.main_button_view_progress_bars.setText("")
        self.main_button_switch_supported_websites.setText(QCoreApplication.translate("PornFetch_Desktop", u"Supported websites", None))
        self.stacked_widget_main.setStyleSheet("")
        self.radio_search_website_xvideos.setText(QCoreApplication.translate("PornFetch_Desktop", u"XVideos", None))
        self.button_help_file.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.radio_search_website_pornhub.setText(QCoreApplication.translate("PornFetch_Desktop", u"PornHub", None))
        self.button_playlist_get_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Videos", None))
        self.label_model_url.setText(QCoreApplication.translate("PornFetch_Desktop", u"Model URL:", None))
        self.lineedit_url.setPlaceholderText(QCoreApplication.translate("PornFetch_Desktop", u"Enter video URL", None))
        self.label_playlist_url.setText(QCoreApplication.translate("PornFetch_Desktop", u"Playlist URL:", None))
        self.button_search.setText(QCoreApplication.translate("PornFetch_Desktop", u"Start", None))
        self.radio_search_website_eporner.setText(QCoreApplication.translate("PornFetch_Desktop", u"EPorner", None))
        self.label_file.setText(QCoreApplication.translate("PornFetch_Desktop", u"File:", None))
        self.radio_search_website_xnxx.setText(QCoreApplication.translate("PornFetch_Desktop", u"XNXX", None))
        self.lineedit_model_url.setPlaceholderText(QCoreApplication.translate("PornFetch_Desktop", u"Enter Model / Channel / Actress URL", None))
        self.button_open_file.setText(QCoreApplication.translate("PornFetch_Desktop", u"Open File", None))
        self.button_model.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Videos", None))
        self.lineedit_file.setText("")
        self.lineedit_file.setPlaceholderText(QCoreApplication.translate("PornFetch_Desktop", u"URLs in the file must be separated with new lines!", None))
        self.button_download.setText(QCoreApplication.translate("PornFetch_Desktop", u"Download", None))
        self.labell_search.setText(QCoreApplication.translate("PornFetch_Desktop", u"Search Query:", None))
        self.label_search_website.setText(QCoreApplication.translate("PornFetch_Desktop", u"Search Website", None))
        self.radio_search_website_hqporner.setText(QCoreApplication.translate("PornFetch_Desktop", u"HQPorner", None))
        self.lineedit_playlist_url.setPlaceholderText(QCoreApplication.translate("PornFetch_Desktop", u"Enter a PornHub Playlist URL", None))
        self.lineedit_search_query.setText("")
        self.lineedit_search_query.setPlaceholderText(QCoreApplication.translate("PornFetch_Desktop", u"Search for Videos. Select Website below", None))
        self.label_url.setText(QCoreApplication.translate("PornFetch_Desktop", u"URL:", None))
        self.button_get_liked_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Liked videos", None))
        self.button_get_watched_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get watched videos", None))
        self.label_username.setText(QCoreApplication.translate("PornFetch_Desktop", u"E-Mail:", None))
        self.button_login.setText(QCoreApplication.translate("PornFetch_Desktop", u"Login", None))
        self.lineedit_username.setPlaceholderText(QCoreApplication.translate("PornFetch_Desktop", u"Enter your PornHub E-Mail address (not your username, pornhub changed it) ", None))
        self.button_get_recommended_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get recommended videos", None))
        self.label_password.setText(QCoreApplication.translate("PornFetch_Desktop", u"Password:", None))
        self.lineedit_password.setPlaceholderText(QCoreApplication.translate("PornFetch_Desktop", u"Enter your PornHub Password", None))
        self.label_progress_eporner.setText(QCoreApplication.translate("PornFetch_Desktop", u"Eporner:", None))
        self.label_info.setText(QCoreApplication.translate("PornFetch_Desktop", u"Info:", None))
        self.label_progress_xvideos.setText(QCoreApplication.translate("PornFetch_Desktop", u"XVideos:", None))
        self.label_progress_pornhub.setText(QCoreApplication.translate("PornFetch_Desktop", u"PornHub:", None))
        self.lineedit_download_info.setText("")
        self.label_progress_xnxx.setText(QCoreApplication.translate("PornFetch_Desktop", u"XNXX:", None))
        self.label_progress_hqporner.setText(QCoreApplication.translate("PornFetch_Desktop", u"HQPorner:", None))
        self.label_progress_spankbang.setText(QCoreApplication.translate("PornFetch_Desktop", u"Spankbang:", None))
        self.button_get_brazzers_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Videos", None))
        self.radio_top_porn_month.setText(QCoreApplication.translate("PornFetch_Desktop", u"Month", None))
        self.button_list_categories.setText(QCoreApplication.translate("PornFetch_Desktop", u"List of all categories", None))
        self.button_eporner_category_get_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Videos", None))
        self.radio_top_porn_all_time.setText(QCoreApplication.translate("PornFetch_Desktop", u"All Time", None))
        self.label_videos_by_category_eporner.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get videos by category", None))
        self.button_list_categories_eporner.setText(QCoreApplication.translate("PornFetch_Desktop", u"List of all categories", None))
        self.label_videos_by_category.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get videos by category", None))
        self.radio_top_porn_week.setText(QCoreApplication.translate("PornFetch_Desktop", u"Week", None))
        self.button_hqporner_category_get_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Videos", None))
        self.labe_get_random_video.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get random video", None))
        self.button_top_porn_get_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Videos", None))
        self.label_get_brazzers_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Brazzers videos", None))
        self.label_get_top_porn.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Top Porn:", None))
        self.button_get_random_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Video", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("PornFetch_Desktop", u"Duration (minutes)", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("PornFetch_Desktop", u"Author", None));
        self.button_tree_download.setText(QCoreApplication.translate("PornFetch_Desktop", u"Download Selected Videos", None))
#if QT_CONFIG(tooltip)
        self.button_tree_select_range.setToolTip(QCoreApplication.translate("PornFetch_Desktop", u"Automatically checks a range of videos", None))
#endif // QT_CONFIG(tooltip)
        self.button_tree_select_range.setText(QCoreApplication.translate("PornFetch_Desktop", u"Select a range of videos", None))
        self.checkbox_tree_show_videos_reversed.setText(QCoreApplication.translate("PornFetch_Desktop", u"Show videos in reverse", None))
        self.button_range_apply_everything.setText(QCoreApplication.translate("PornFetch_Desktop", u"Select everything", None))
        self.button_tree_export_video_urls.setText(QCoreApplication.translate("PornFetch_Desktop", u"Export video URLs", None))
        self.radio_tree_show_title.setText(QCoreApplication.translate("PornFetch_Desktop", u"Only Title (a lot faster)", None))
#if QT_CONFIG(tooltip)
        self.button_tree_unselect_all.setToolTip(QCoreApplication.translate("PornFetch_Desktop", u"Unselects all videos in the tree widget", None))
#endif // QT_CONFIG(tooltip)
        self.button_tree_unselect_all.setText(QCoreApplication.translate("PornFetch_Desktop", u"Unselect all", None))
#if QT_CONFIG(tooltip)
        self.radio_tree_show_all.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.radio_tree_show_all.setText(QCoreApplication.translate("PornFetch_Desktop", u"Get Title, Author, Duration", None))
#if QT_CONFIG(tooltip)
        self.button_tree_stop.setToolTip(QCoreApplication.translate("PornFetch_Desktop", u"Does not stop downloading videos", None))
#endif // QT_CONFIG(tooltip)
        self.button_tree_stop.setText(QCoreApplication.translate("PornFetch_Desktop", u"Stop loading videos", None))
        self.checkbox_tree_do_not_clear_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Do not clear videos", None))
        self.settings_groupbox_performance.setTitle(QCoreApplication.translate("PornFetch_Desktop", u"Performance", None))
        self.label_semaphore.setText(QCoreApplication.translate("PornFetch_Desktop", u"Simultaneous downloads:", None))
        self.button_semaphore_help.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.label_maximal_workers.setText(QCoreApplication.translate("PornFetch_Desktop", u"Maximal workers:", None))
        self.button_workers_help.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.label_maximal_timeout.setText(QCoreApplication.translate("PornFetch_Desktop", u"Maximal timeout:", None))
        self.button_timeout_help.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.label_maximal_retries.setText(QCoreApplication.translate("PornFetch_Desktop", u"Maximal retries:", None))
        self.button_timeout_maximal_retries_help.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.label_pornhub_delay.setText(QCoreApplication.translate("PornFetch_Desktop", u"PornHub Delay (0 = Disabled) in seconds:", None))
        self.button_pornhub_delay_help.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.label_threading_mode.setText(QCoreApplication.translate("PornFetch_Desktop", u"Threading Mode:", None))
        self.radio_threading_mode_high_performance.setText(QCoreApplication.translate("PornFetch_Desktop", u"High Performance", None))
        self.radio_threading_mode_ffmpeg.setText(QCoreApplication.translate("PornFetch_Desktop", u"FFMPEG", None))
        self.radio_threading_mode_default.setText(QCoreApplication.translate("PornFetch_Desktop", u"Default", None))
        self.button_threading_mode_help.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.settings_groupbox_ui.setTitle(QCoreApplication.translate("PornFetch_Desktop", u"Graphical User Interface", None))
        self.label_ui_language.setText(QCoreApplication.translate("PornFetch_Desktop", u"Graphical User Interface Language:", None))
        self.radio_ui_language_system_default.setText(QCoreApplication.translate("PornFetch_Desktop", u"System default", None))
        self.radio_ui_language_english.setText(QCoreApplication.translate("PornFetch_Desktop", u"English", None))
        self.radio_ui_language_french.setText(QCoreApplication.translate("PornFetch_Desktop", u"French", None))
        self.radio_ui_language_chinese_simplified.setText(QCoreApplication.translate("PornFetch_Desktop", u"Chinese (simplified)", None))
        self.radio_ui_language_german.setText(QCoreApplication.translate("PornFetch_Desktop", u"German", None))
        self.label_settings_design.setText(QCoreApplication.translate("PornFetch_Desktop", u"Porn Fetch Design:", None))
        self.radio_ui_design_native.setText(QCoreApplication.translate("PornFetch_Desktop", u"LSD", None))
        self.radio_ui_design_dark_mode.setText(QCoreApplication.translate("PornFetch_Desktop", u"System's dark mode", None))
        self.radio_ui_design_light_mode.setText(QCoreApplication.translate("PornFetch_Desktop", u"System's light mode", None))
        self.settings_groupbox_system_pornfetch.setTitle(QCoreApplication.translate("PornFetch_Desktop", u"System / Porn Fetch", None))
        self.settings_checkbox_system_update_checks.setText(QCoreApplication.translate("PornFetch_Desktop", u"Update checks", None))
        self.settings_checkbox_internet_checks.setText(QCoreApplication.translate("PornFetch_Desktop", u"Internet checks", None))
        self.checkbox_settings_system_anonymous_mode.setText(QCoreApplication.translate("PornFetch_Desktop", u"Enable Anonymous mode", None))
        self.label_settings_system_privacy.setText(QCoreApplication.translate("PornFetch_Desktop", u"Privacy:", None))
        self.checkbox_settings_system_enable_tor.setText(QCoreApplication.translate("PornFetch_Desktop", u"Enable Tor", None))
        self.settings_label_startup.setText(QCoreApplication.translate("PornFetch_Desktop", u"Startup:", None))
        self.button_settings_help_tor.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.settings_button_help_anonymous_mode.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.button_download_ffmpeg.setText(QCoreApplication.translate("PornFetch_Desktop", u"Download and Setup FFmpeg", None))
        self.button_install_pornfetch.setText(QCoreApplication.translate("PornFetch_Desktop", u"Install Porn Fetch", None))
        self.groupbox_videos.setTitle(QCoreApplication.translate("PornFetch_Desktop", u"Videos", None))
        self.radio_directory_system_no.setText(QCoreApplication.translate("PornFetch_Desktop", u"No", None))
        self.button_directory_system_help.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.radio_directory_system_yes.setText(QCoreApplication.translate("PornFetch_Desktop", u"Yes", None))
        self.button_help_model_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.radio_skip_existing_files_yes.setText(QCoreApplication.translate("PornFetch_Desktop", u"Yes", None))
        self.labe_settings_videos_model.setText(QCoreApplication.translate("PornFetch_Desktop", u"Model videos (PornHub)", None))
        self.radio_quality_half.setText(QCoreApplication.translate("PornFetch_Desktop", u"Half", None))
        self.radio_model_both.setText(QCoreApplication.translate("PornFetch_Desktop", u"Both", None))
        self.label_output_path.setText(QCoreApplication.translate("PornFetch_Desktop", u"Output path:", None))
        self.button_output_path_select.setText(QCoreApplication.translate("PornFetch_Desktop", u"Open", None))
        self.radio_quality_worst.setText(QCoreApplication.translate("PornFetch_Desktop", u"Worst", None))
        self.radio_skip_existing_files_no.setText(QCoreApplication.translate("PornFetch_Desktop", u"No", None))
        self.label_directory_system.setText(QCoreApplication.translate("PornFetch_Desktop", u"Use Directory system? ", None))
        self.button_result_limit_help.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.radio_model_featured.setText(QCoreApplication.translate("PornFetch_Desktop", u"Featured videos", None))
        self.lineedit_output_path.setPlaceholderText(QCoreApplication.translate("PornFetch_Desktop", u"Enter \"./\" for current directory", None))
        self.radio_quality_best.setText(QCoreApplication.translate("PornFetch_Desktop", u"Best", None))
        self.label_skip_existing_files.setText(QCoreApplication.translate("PornFetch_Desktop", u"Skip existing files:", None))
        self.radio_model_uploads.setText(QCoreApplication.translate("PornFetch_Desktop", u"User uploads", None))
        self.button_help_skip_existing_files.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.label_quality.setText(QCoreApplication.translate("PornFetch_Desktop", u"Quality:", None))
        self.label_searching_limit.setText(QCoreApplication.translate("PornFetch_Desktop", u"Result Limit:", None))
        self.groupbox_post_processing.setTitle(QCoreApplication.translate("PornFetch_Desktop", u"Post Processing", None))
        self.radio_settings_post_processing_use_custom_format.setText(QCoreApplication.translate("PornFetch_Desktop", u"Use custom format:", None))
        self.radio_settings_post_rocessing_do_not_convert.setText(QCoreApplication.translate("PornFetch_Desktop", u"Do not convert", None))
        self.lineedit_settings_post_processing_use_custom_format.setText(QCoreApplication.translate("PornFetch_Desktop", u"mp4", None))
        self.checkbox_settings_post_processing_write_metadata_tags.setText(QCoreApplication.translate("PornFetch_Desktop", u"Write metadata tags", None))
        self.checkbox_settings_post_processing_unfinished_videos.setText(QCoreApplication.translate("PornFetch_Desktop", u"Use a different output path for unfinished videos:", None))
        self.button_settings_post_processing_output_path.setText(QCoreApplication.translate("PornFetch_Desktop", u"Open", None))
        self.button_help_write_metadata_tags.setText(QCoreApplication.translate("PornFetch_Desktop", u"Help", None))
        self.settings_button_apply.setText(QCoreApplication.translate("PornFetch_Desktop", u"Apply  (needs restart)", None))
        self.settings_button_reset.setText(QCoreApplication.translate("PornFetch_Desktop", u"Reset Porn Fetch to default settings", None))
        self.textbrowser_websites.setHtml(QCoreApplication.translate("PornFetch_Desktop", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">Supported Websites:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">Downloading:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- PornHub.com (supports total progress)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- HQPorner.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- Eporner.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- XNXX.com (supports total progress)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- XVideos.com (supports total progress)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- Spankbang.com (supports total progress)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">All sites suppo"
                        "rt *threaded* downloads and selectable quality!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">* hqporner and eporner running in QThreads, but they don't fetch segments. The video is directly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">downloaded, therefore threading in a segment isn't needed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\" ma"
                        "rgin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">Model / Channel Downloads</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- PornHub.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- HQPorner.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- EPorner.com</span><"
                        "/p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- XNXX.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- XVideos.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">Searching:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>"
                        "\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- PornHub.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- HQPorner.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- Xvideos.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- Eporner.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">- XNXX.c"
                        "om</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">I am constantly working to support more websites.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">If you want a specific site to be supported, just ask:<br /><br />Discord: echteralsfake</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">GitHub.com/echteralsfake/Porn_Fetch/issues</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; marg"
                        "in-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; mar"
                        "gin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p></body></html>", None))
        self.main_label_progressbar_total.setText(QCoreApplication.translate("PornFetch_Desktop", u"Total:", None))
        self.main_label_progressbar_converting.setText(QCoreApplication.translate("PornFetch_Desktop", u"Converting:", None))
    # retranslateUi

