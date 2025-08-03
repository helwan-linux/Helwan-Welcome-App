#!/usr/bin/env python3
# CREATED BY Saeed Badrelden <saeedbadrelden2021@gmail.com>

import subprocess
import webbrowser
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox
from translations import _
import sys
import os

def create_labeled_combobox(parent, label_attr, combo_attr, label_text, items, default, on_change=None):
    layout = QHBoxLayout()
    label = QLabel(label_text)
    combo = QComboBox()
    combo.addItems(items)
    index = combo.findText(default)
    if index != -1:
        combo.setCurrentIndex(index)
    if on_change:
        combo.currentTextChanged.connect(on_change)
    combo.setStyleSheet("font-size: 10px; padding: 4px;")
    setattr(parent, label_attr, label)
    setattr(parent, combo_attr, combo)
    layout.addWidget(label)
    layout.addWidget(combo)
    return layout

def create_button(text, on_click, parent):
    button = QPushButton(text)
    button.clicked.connect(on_click)
    button.setStyleSheet("font-size: 10px; padding: 4px 8px;")
    return button

def open_url(url):
    webbrowser.open(url)

def run_terminal_cmd(command, title=_("Running Command")):
    try:
        subprocess.Popen([
            "xfce4-terminal",
            "--hold",
            "--title", title,
            "--command",
            f"bash -ic '{command}; echo; echo Press Enter to exit...; read'"
        ])
    except FileNotFoundError:
        QMessageBox.critical(None, _("Error"), _("xfce4-terminal is not installed. Please install xfce4-terminal."))

def is_yay_installed():
    try:
        process = subprocess.run(['yay', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.returncode == 0
    except FileNotFoundError:
        return False
