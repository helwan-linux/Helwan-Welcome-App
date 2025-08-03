#!/usr/bin/env python3
# CREATED BY Saeed Badrelden <saeedbadrelden2021@gmail.com>

def load_theme(app_instance, theme_name):
    if theme_name == "Default":
        app_instance.setStyleSheet("""
            QWidget { background-color: #f5f5f5; font-family: 'Segoe UI'; font-size: 13px; color: #333; }
            QLabel { color: #333; margin-bottom: 5px; }
            QPushButton { background-color: #e0e0e0; color: #333; border: 1px solid #ccc; border-radius: 5px; padding: 6px 10px; margin-top: 3px; margin-bottom: 3px; font-size: 10px; }
            QPushButton:hover { background-color: #d0d0d0; }
            QCheckBox { color: #333; margin-top: 5px; margin-bottom: 5px; }
            QComboBox { background-color: #fff; color: #333; border: 1px solid #ccc; border-radius: 3px; padding: 4px; margin-top: 3px; margin-bottom: 3px; font-size: 10px; }
            QGroupBox { border: 1px solid #ccc; border-radius: 5px; margin-top: 10px; padding: 10px; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #555; }
            QLabel#disk_space_status { font-weight: bold; }
            QLabel#disk_space_status_ok { color: green; }
            QLabel#disk_space_status_warning { color: orange; }
            QLabel#disk_space_status_error { color: red; }
            QLabel#system_info { margin-bottom: 2px; }
            QTabWidget::pane { border: 1px solid #C2C7CB; background: #f5f5f5; }
            QTabWidget::tab-bar QToolButton { background: #e0e0e0; color: #333; border: 1px solid #ccc; border-radius: 3px; padding: 4px 10px; margin: 2px; font-size: 10px; }
            QTabWidget::tab-bar QToolButton:hover { background: #d0d0d0; }
            QTabWidget::tab-bar QToolButton:selected { background: #d0d0d0; font-weight: bold; }
        """)
        if app_instance.greeting:
            app_instance.greeting.setStyleSheet("font-size: 15px; margin-top: 10px; margin-bottom: 15px; color: #555;")
    elif theme_name == "Sky Blue":
        app_instance.setStyleSheet("""
            QWidget { background-color: #e0f7fa; font-family: 'Segoe UI'; font-size: 13px; color: #212121; }
            QLabel { color: #212121; margin-bottom: 5px; }
            QPushButton { background-color: #81d4fa; color: #212121; border: 1px solid #4fc3f7; border-radius: 5px; padding: 6px 10px; margin-top: 3px; margin-bottom: 3px; font-size: 10px; }
            QPushButton:hover { background-color: #4fc3f7; }
            QCheckBox { color: #212121; margin-top: 5px; margin-bottom: 5px; }
            QComboBox { background-color: #b3e5fc; color: #212121; border: 1px solid #81d4fa; border-radius: 3px; padding: 4px; margin-top: 3px; margin-bottom: 3px; font-size: 10px; }
            QGroupBox { border: 1px solid #4fc3f7; border-radius: 5px; margin-top: 10px; padding: 10px; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #0277bd; }
            QLabel#disk_space_status { font-weight: bold; color: #212121; }
            QLabel#disk_space_status_ok { color: darkgreen; }
            QLabel#disk_space_status_warning { color: darkorange; }
            QLabel#disk_space_status_error { color: darkred; }
            QLabel#system_info { margin-bottom: 2px; }
            QTabWidget::pane { border: 1px solid #4fc3f7; background: #e0f7fa; }
            QTabWidget::tab-bar QToolButton { background: #81d4fa; color: #212121; border: 1px solid #4fc3f7; border-radius: 3px; padding: 4px 10px; margin: 2px; font-size: 10px; }
            QTabWidget::tab-bar QToolButton:hover { background: #4fc3f7; }
            QTabWidget::tab-bar QToolButton:selected { background: #4fc3f7; font-weight: bold; }
        """)
        if app_instance.greeting:
            app_instance.greeting.setStyleSheet("font-size: 15px; margin-top: 10px; margin-bottom: 15px; color: #212121;")
    elif theme_name == "Light Black":
        app_instance.setStyleSheet("""
            QWidget { background-color: #666666; font-family: 'Segoe UI'; font-size: 13px; color: #d0d0d0; }
            QLabel { color: #d0d0d0; margin-bottom: 5px; }
            QPushButton { background-color: #808080; color: #d0d0d0; border: 1px solid #a0a0a0; border-radius: 5px; padding: 6px 10px; margin-top: 3px; margin-bottom: 3px; font-size: 10px; }
            QPushButton:hover { background-color: #a0a0a0; }
            QCheckBox { color: #d0d0d0; margin-top: 5px; margin-bottom: 5px; }
            QComboBox { background-color: #737373; color: #d0d0d0; border: 1px solid #999999; border-radius: 3px; padding: 4px; margin-top: 3px; margin-bottom: 3px; font-size: 10px; }
            QGroupBox { border: 1px solid #999999; border-radius: 5px; margin-top: 10px; padding: 10px; color: #d0d0d0; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #cccccc; }
            QLabel#disk_space_status { font-weight: bold; color: #d0d0d0; }
            QLabel#disk_space_status_ok { color: lightgreen; }
            QLabel#disk_space_status_warning { color: yellow; }
            QLabel#disk_space_status_error { color: red; }
            QLabel#system_info { margin-bottom: 2px; color: #d0d0d0; }
            QTabWidget::pane { border: 1px solid #999999; background: #666666; color: #d0d0d0; }
            QTabWidget::tab-bar QToolButton { background: #808080; color: #d0d0d0; border: 1px solid #a0a0a0; border-radius: 3px; padding: 4px 10px; margin: 2px; font-size: 10px; }
            QTabWidget::tab-bar QToolButton:hover { background: #a0a0a0; }
            QTabWidget::tab-bar QToolButton:selected { background: #a0a0a0; font-weight: bold; }
        """)
        if app_instance.greeting:
            app_instance.greeting.setStyleSheet("font-size: 15px; margin-top: 10px; margin-bottom: 15px; color: #d0d0d0;")
    elif theme_name == "Light Purple":
        app_instance.setStyleSheet("""
            QWidget { background-color: #e6ccff; font-family: 'Segoe UI'; font-size: 13px; color: #4d194d; }
            QLabel { color: #4d194d; margin-bottom: 5px; }
            QPushButton { background-color: #f0d9ff; color: #4d194d; border: 1px solid #b388eb; border-radius: 5px; padding: 6px 10px; margin-top: 3px; margin-bottom: 3px; font-size: 10px; }
            QPushButton:hover { background-color: #b388eb; }
            QCheckBox { color: #4d194d; margin-top: 5px; margin-bottom: 5px; }
            QComboBox { background-color: #f3e5f5; color: #4d194d; border: 1px solid #ce93d8; border-radius: 3px; padding: 4px; margin-top: 3px; margin-bottom: 3px; font-size: 10px; }
            QGroupBox { border: 1px solid #ce93d8; border-radius: 5px; margin-top: 10px; padding: 10px; color: #4d194d; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #8e24aa; }
            QLabel#disk_space_status { font-weight: bold; color: #4d194d; }
            QLabel#disk_space_status_ok { color: darkgreen; }
            QLabel#disk_space_status_warning { color: darkorange; }
            QLabel#disk_space_status_error { color: darkred; }
            QLabel#system_info { margin-bottom: 2px; color: #4d194d; }
            QTabWidget::pane { border: 1px solid #ce93d8; background: #e6ccff; color: #4d194d; }
            QTabWidget::tab-bar QToolButton { background: #f0d9ff; color: #4d194d; border: 1px solid #b388eb; border-radius: 3px; padding: 4px 10px; margin: 2px; font-size: 10px; }
            QTabWidget::tab-bar QToolButton:hover { background: #b388eb; }
            QTabWidget::tab-bar QToolButton:selected { background: #b388eb; font-weight: bold; }
        """)
        if app_instance.greeting:
            app_instance.greeting.setStyleSheet("font-size: 15px; margin-top: 10px; margin-bottom: 15px; color: #4d194d;")
