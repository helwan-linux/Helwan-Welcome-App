#!/usr/bin/env python3
# CREATED BY Saeed Badrelden <saeedbadrelden2021@gmail.com>

import sys
import os
import webbrowser
import subprocess
import shutil
import platform
import psutil

from PyQt5.QtWidgets import (
	QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox,
	QComboBox, QGroupBox, QGridLayout, QHBoxLayout, QMessageBox,
	QScrollArea, QTabWidget, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer, QSettings
from PyQt5.QtGui import QPixmap

from translations import load_translation, DEFAULT_LANGUAGE_CODE, APP_LANGUAGES, SYSTEM_LANGUAGES
from themes import load_theme
from utils import create_button, create_labeled_combobox, run_terminal_cmd, open_url, is_yay_installed

# === إعداد الترجمة ===
_ = load_translation(DEFAULT_LANGUAGE_CODE)

class WelcomeApp(QWidget):

	def __init__(self):
		super().__init__()
		self.language_code = DEFAULT_LANGUAGE_CODE
		self.show_on_startup = self.check_startup_enabled()
		self.current_theme = "Default"

		self.settings = QSettings("Helwan", "WelcomeApp")
		self.logo = self.load_logo()

		self.app_lang_label = None
		self.app_lang_combobox = None
		self.startup_check = None
		self.pacman_btn = None
		self.yay_btn = None
		self.install_lts_btn = None
		self.install_zen_btn = None
		self.sys_lang_label = None
		self.system_language_combobox = None
		self.apply_lang_btn = None
		self.docs_btn = None
		self.youtube_btn = None
		self.neofetch_btn = None
		self.htop_btn = None
		self.system_info_group = None
		self.disk_space_label = None
		self.disk_space_status = None
		self.processor_label = None
		self.processor_info = None
		self.memory_label = None
		self.memory_info = None
		self.theme_label = None
		self.theme_combobox = None
		self.clean_paccache_keep_two_check = None

		self.tabs = QTabWidget()
		self.main_tab = QWidget()
		self.cleaner_tab = QWidget()

		self.init_ui()
		self.load_theme(self.current_theme)

		self.load_settings()

		self.check_disk_space()
		self.update_system_info()

		self.timer = QTimer()
		self.timer.timeout.connect(self.check_disk_space)
		self.timer.start(5000)

	# def load_logo(self):
		# # المسار الصحيح للوجو في بيئة Linux
		# logo_path = "/usr/share/helwan-welcome-app/sources/logo.png"
		# if os.path.exists(logo_path):
			# logo = QPixmap(logo_path)
			# return logo.scaledToWidth(120, Qt.SmoothTransformation) if not logo.isNull() else None
		# else:
			# print(f"Warning: Logo not found at {logo_path}")
			# return None
			
	def load_logo(self):
	
		if getattr(sys, 'frozen', False):
			base_path = sys._MEIPASS  # لما البرنامج يبقى frozen (مثلاً PyInstaller)
		else:
			base_path = os.path.dirname(os.path.abspath(__file__))

		logo_path = os.path.join(base_path, "sources", "logo.png")

		if os.path.exists(logo_path):
			logo = QPixmap(logo_path)
			return logo.scaledToWidth(120, Qt.SmoothTransformation) if not logo.isNull() else None
		else:
			print(f"Warning: Logo not found at {logo_path}")
			return None

	def load_settings(self):
		if self.app_lang_combobox:
			saved_language_index = self.settings.value("language_index", 0, type=int)
			self.app_lang_combobox.setCurrentIndex(saved_language_index)
			self.change_language(self.app_lang_combobox.currentText())

		if self.theme_combobox:
			saved_theme = self.settings.value("theme", "Default", type=str)
			index = self.theme_combobox.findText(saved_theme)
			if index != -1:
				self.theme_combobox.setCurrentIndex(index)
				self.load_theme(saved_theme)

	def check_startup_enabled(self):
		autostart_dir = os.path.expanduser("~/.config/autostart")
		startup_file_path = os.path.join(autostart_dir, "helwan_welcome.desktop")
		return os.path.exists(startup_file_path)

	def load_theme(self, theme_name):
		load_theme(self, theme_name)

	def init_ui(self):
		main_layout = QVBoxLayout(self)
		self.tabs.addTab(self.create_main_tab(), _("Welcome"))
		self.tabs.addTab(self.create_cleaner_tab(), _("System Cleaner"))
		main_layout.addWidget(self.tabs)

		self.setLayout(main_layout)
		self.setWindowTitle(_("Welcome to Helwan Linux"))
		self.setGeometry(100, 100, 600, 400)

		self.load_settings()

	def create_main_tab(self):
		main_tab_layout = QVBoxLayout(self.main_tab)
		main_tab_layout.setAlignment(Qt.AlignTop)
		main_tab_layout.setSpacing(1)

		if self.logo:
			logo_label = QLabel(self)
			logo_label.setPixmap(self.logo)
			logo_label.setAlignment(Qt.AlignCenter)
			main_tab_layout.addWidget(logo_label)

		self.greeting = QLabel()
		self.greeting.setAlignment(Qt.AlignCenter)
		self.greeting.setStyleSheet("font-size: 15px; margin-top: 10px; margin-bottom: 15px; color: #e0e0e0;")
		main_tab_layout.addWidget(self.greeting)

		controls = QVBoxLayout()
		controls.setSpacing(1)
		main_tab_layout.addLayout(controls)

		# System Updates Group
		update_group = QGroupBox(_("System Updates"))
		update_layout = QVBoxLayout()
		update_layout_buttons = QHBoxLayout()
		self.pacman_btn_bottom = create_button(_("Update System (Pacman)"),
													lambda: run_terminal_cmd("sudo pacman -Syu"), self)
		update_layout_buttons.addWidget(self.pacman_btn_bottom)
		self.yay_btn_bottom = create_button(_("Update System (Yay)"), lambda: run_terminal_cmd("yay -Syu"), self)
		if not is_yay_installed():
			self.yay_btn_bottom.setEnabled(False)
			self.yay_btn_bottom.setToolTip(_("Yay is not installed."))
		update_layout_buttons.addWidget(self.yay_btn_bottom)
		update_layout.addLayout(update_layout_buttons)

		kernel_install_layout = QHBoxLayout()
		self.install_lts_btn = create_button(_("Install Linux LTS"), self.install_linux_lts, self)
		kernel_install_layout.addWidget(self.install_lts_btn)
		self.install_zen_btn = create_button(_("Install Linux Zen"), self.install_linux_zen, self)
		kernel_install_layout.addWidget(self.install_zen_btn)
		update_layout.addLayout(kernel_install_layout)

		update_group.setLayout(update_layout)
		controls.addWidget(update_group)

		# Theme Selection
		theme_layout = QHBoxLayout()
		self.theme_label = QLabel(_("Application Theme:"))
		theme_layout.addWidget(self.theme_label)
		self.theme_combobox = QComboBox()
		self.theme_combobox.addItems(["Default", "Sky Blue", "Light Black", "Light Purple"])
		self.theme_combobox.setCurrentText(self.current_theme)
		self.theme_combobox.currentTextChanged.connect(self.save_theme)
		self.theme_combobox.setStyleSheet("font-size: 10px; padding: 1px;")
		theme_layout.addWidget(self.theme_combobox)
		controls.addLayout(theme_layout)

		# Application Language
		app_lang_layout = create_labeled_combobox(
			self,
			label_attr='app_lang_label',
			combo_attr='app_lang_combobox',
			label_text=_("Application Language:"),
			items=list(APP_LANGUAGES.values()),
			default=APP_LANGUAGES.get(self.language_code, 'English'),
			on_change=self.change_language
		)
		controls.addLayout(app_lang_layout)

		# Startup Settings
		startup_layout = QHBoxLayout()
		self.startup_check = QCheckBox(_("Show on startup"))
		self.startup_check.setChecked(self.show_on_startup)
		self.startup_check.stateChanged.connect(self.update_startup_file)
		startup_layout.addWidget(self.startup_check)
		controls.addLayout(startup_layout)

		# System Language
		sys_lang_layout = QHBoxLayout()
		self.sys_lang_label = QLabel(_("System Language:"))
		sys_lang_layout.addWidget(self.sys_lang_label)
		self.system_language_combobox = QComboBox()
		self.system_language_combobox.addItems(list(SYSTEM_LANGUAGES.values()))
		self.system_language_combobox.setCurrentText(
			'en_US.UTF-8' if 'en_US.UTF-8' in SYSTEM_LANGUAGES else list(SYSTEM_LANGUAGES.keys())[
				0] if SYSTEM_LANGUAGES else '')
		sys_lang_layout.addWidget(self.system_language_combobox)
		controls.addLayout(sys_lang_layout)

		self.apply_lang_btn = create_button(_("Apply System Language"), self.apply_system_language, self)
		controls.addWidget(self.apply_lang_btn)

		# Documentation and Support
		docs_layout = QHBoxLayout()
		self.docs_btn = create_button(_("Open Documentation"),
										lambda: open_url("https://helwan-linux.mystrikingly.com/documentation"), self)
		docs_layout.addWidget(self.docs_btn)
		self.youtube_btn = create_button(_("Open YouTube Channel"),
										  lambda: open_url("https://www.youtube.com/@HelwanO.S"), self)
		docs_layout.addWidget(self.youtube_btn)
		controls.addLayout(docs_layout)

		# System Information Group
		self.system_info_group = QGroupBox(_("System Information"))
		system_info_layout = QGridLayout()
		self.disk_space_label = QLabel(_("Available Disk Space:"))
		self.disk_space_status = QLabel()
		self.disk_space_status.setObjectName("disk_space_status")
		system_info_layout.addWidget(self.disk_space_label, 0, 0)
		system_info_layout.addWidget(self.disk_space_status, 0, 1)
		self.processor_label = QLabel(_("Processor:"))
		self.processor_info = QLabel()
		self.processor_info.setObjectName("system_info")
		system_info_layout.addWidget(self.processor_label, 1, 0)
		system_info_layout.addWidget(self.processor_info, 1, 1)
		self.memory_label = QLabel(_("RAM:"))
		self.memory_info = QLabel()
		self.memory_info.setObjectName("system_info")
		system_info_layout.addWidget(self.memory_label, 2, 0)
		system_info_layout.addWidget(self.memory_info, 2, 1)
		self.system_info_group.setLayout(system_info_layout)
		self.system_info_group.setMaximumHeight(110)
		controls.addWidget(self.system_info_group)

		# System Information Buttons (Neofetch, Htop)
		sysinfo_layout = QHBoxLayout()
		self.neofetch_btn = create_button(_("Show System Info Details"), lambda: run_terminal_cmd("helfetch-ng"), self)
		sysinfo_layout.addWidget(self.neofetch_btn)
		self.htop_btn = create_button(_("Performance Monitor"), lambda: run_terminal_cmd("htop"), self)
		sysinfo_layout.addWidget(self.htop_btn)
		controls.addLayout(sysinfo_layout)

		spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
		main_tab_layout.addItem(spacer)

		return self.main_tab

	def create_cleaner_tab(self):
		cleaner_layout = QVBoxLayout(self.cleaner_tab)
		cleaner_group = QGroupBox(_("Pacman Cleaner"))
		cleaner_group.setObjectName("Pacman Cleaner")
		pacman_cleaner_layout = QVBoxLayout()

		self.clean_pacman_cache_full_check = QCheckBox(
			_("Clean Pacman Cache (Full) - Warning! This will remove all downloaded packages."))
		self.clean_pacman_cache_full_check.setObjectName("clean_pacman_cache_full_check")
		pacman_cleaner_layout.addWidget(self.clean_pacman_cache_full_check)

		self.remove_orphan_packages_check = QCheckBox(
			_("Remove Orphan Packages - Packages that are no longer required by any installed package."))
		self.remove_orphan_packages_check.setObjectName("remove_orphan_packages_check")
		pacman_cleaner_layout.addWidget(self.remove_orphan_packages_check)

		self.clean_paccache_keep_two_check = QCheckBox(_("Clean Old Packages (Keep Last 2 Versions)"))
		self.clean_paccache_keep_two_check.setObjectName("clean_paccache_keep_two_check")
		pacman_cleaner_layout.addWidget(self.clean_paccache_keep_two_check)

		self.run_pacman_cleanup_button = create_button(_("Run Pacman Cleanup"), self.run_pacman_cleanup, self)
		self.run_pacman_cleanup_button.setObjectName("run_pacman_cleanup_button")
		pacman_cleaner_layout.addWidget(self.run_pacman_cleanup_button)

		cleaner_group.setLayout(pacman_cleaner_layout)
		cleaner_layout.addWidget(cleaner_group)
		cleaner_layout.addStretch(1)
		return self.cleaner_tab

	def run_pacman_cleanup(self):
		commands = []

		if self.clean_pacman_cache_full_check.isChecked():
			commands.append("sudo pacman -Scc")

		if self.remove_orphan_packages_check.isChecked():
			orphans = subprocess.getoutput("pacman -Qtdq")
			if orphans.strip():
				commands.append("sudo pacman -Rns $(pacman -Qtdq)")
			else:
				pass

		if self.clean_paccache_keep_two_check.isChecked():
			commands.append("sudo paccache -rk2 --quiet")

		if commands:
			full_command = " && ".join(commands)
			confirmation_text = _("You are about to run the following commands with root privileges:\n\n") + \
								"\n".join(commands) + _("\n\nAre you sure you want to continue?")
			reply = QMessageBox.question(self, _("Confirmation"), confirmation_text,
										 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

			if reply == QMessageBox.Yes:
				run_terminal_cmd(full_command, _("Running Pacman Cleanup"))
				QMessageBox.information(self, _("Cleanup Done"), _("Pacman cleanup tasks completed."))
		else:
			QMessageBox.information(self, _("Info"), _("No Pacman cleanup options selected."))

	def update_startup_file(self, state):
		autostart_dir = os.path.expanduser("~/.config/autostart")
		startup_file_path = os.path.join(autostart_dir, "helwan_welcome.desktop")
		if state == Qt.Checked:
			if not os.path.exists(autostart_dir):
				os.makedirs(autostart_dir, exist_ok=True)
			with open(startup_file_path, "w") as f:
				f.write("[Desktop Entry]\n")
				f.write("Type=Application\n")
				f.write(f"Exec={sys.executable} {os.path.abspath(__file__)}\n")
				f.write("Hidden=false\n")
				f.write("X-GNOME-Autostart-enabled=true\n")
				f.write("Name=Helwan Welcome\n")
				f.write("Comment=Welcome application for Helwan Linux\n")
				if self.logo:
					logo_base_name = os.path.basename(
						os.path.join(os.path.dirname(os.path.abspath(__file__)), "sources", "logo.png"))
					f.write(
						f"Icon={os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sources', logo_base_name)}\n")
		else:
			if os.path.exists(startup_file_path):
				os.remove(startup_file_path)
		self.show_on_startup = state == Qt.Checked

	def change_language(self, language_name):
		for code, name in APP_LANGUAGES.items():
			if name == language_name:
				if code == getattr(self, 'language_code', None):
					return

				new_gettext = load_translation(code)
				global _
				_ = new_gettext
				self.language_code = code
				self.retranslate_ui()
				self.settings.setValue("language_index", self.app_lang_combobox.currentIndex())

				QMessageBox.information(self, _("Language Changed"),
										_("Application language has been changed. Some changes may require an application restart."))
				return
		print(f"Warning: Language code not found for {language_name}")

	def save_theme(self, theme_name):
		self.current_theme = theme_name
		self.load_theme(theme_name)
		self.settings.setValue("theme", theme_name)

	def install_linux_lts(self):
		cmd = (
			"pkexec bash -c '"
			"pacman -S --needed linux-lts linux-lts-headers && "
			"if pacman -Qs linux-lts > /dev/null; then "
			"echo \"linux-lts installed successfully.\"; "
			"grub-mkconfig -o /boot/grub/grub.cfg; "
			"else "
			"echo \"Failed to install linux-lts.\" >&2; exit 1; "
			"fi'"
		)

		subprocess.run(cmd, shell=True)

		reply = QMessageBox.question(
			self,
			_("Set LTS as default"),
			_("Do you want to make the LTS kernel the default boot option?"),
			QMessageBox.Yes | QMessageBox.No
		)

		if reply == QMessageBox.Yes:
			set_default_cmd = (
				"pkexec bash -c '"
				"grub-set-default \"Advanced options for Arch Linux>Arch Linux, with Linux lts\" && "
				"grub-mkconfig -o /boot/grub/grub.cfg'"
			)
			subprocess.run(set_default_cmd, shell=True)

	def install_linux_zen(self):
		cmd = (
			"pkexec bash -c '"
			"pacman -S --needed linux-zen linux-zen-headers && "
			"if pacman -Qs linux-zen > /dev/null; then "
			"echo \"linux-zen installed successfully.\"; "
			"grub-mkconfig -o /boot/grub/grub.cfg; "
			"else "
			"echo \"Failed to install linux-zen.\" >&2; exit 1; "
			"fi'"
		)

		subprocess.run(cmd, shell=True)

		reply = QMessageBox.question(
			self,
			_("Set LTS as default"),
			_("Do you want to make the zen kernel the default boot option?"),
			QMessageBox.Yes | QMessageBox.No
		)

		if reply == QMessageBox.Yes:
			set_default_cmd = (
				"pkexec bash -c '"
				"grub-set-default \"Advanced options for Arch Linux>Arch Linux, with Linux zen\" && "
				"grub-mkconfig -o /boot/grub/grub.cfg'"
			)
			subprocess.run(set_default_cmd, shell=True)

	def apply_system_language(self):
		selected_lang_name = self.system_language_combobox.currentText()
		lang_code = None
		for code, name in SYSTEM_LANGUAGES.items():
			if name == selected_lang_name:
				lang_code = code
				break

		if not lang_code:
			QMessageBox.critical(self, _("Error"), _("Please select a valid system language."))
			return

		base_lang_code = lang_code.replace('.UTF-8', '')

		try:
			current_locale_output = subprocess.check_output("localectl status", shell=True).decode()
			if f"LANG={base_lang_code}.UTF-8" in current_locale_output:
				QMessageBox.information(
					self,
					_("No Change Needed"),
					_("The selected language is already active.")
				)
				return
		except Exception as e:
			QMessageBox.warning(self, _("Warning"), _("Could not verify current system language:\n") + str(e))

		locale_line = f"{base_lang_code}.UTF-8 UTF-8"
		cmd = (
			'pkexec bash -c "'
			f"sed -i 's/^#\\s*{locale_line}/{locale_line}/' /etc/locale.gen && "
			"locale-gen && "
			f"localectl set-locale LANG={base_lang_code}.UTF-8"
			'"'
		)

		try:
			process = subprocess.Popen(
				cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
			)
			stdout, stderr = process.communicate()

			if process.returncode == 0:
				QMessageBox.information(
					self,
					_("Success"),
					_("System language changed successfully. Please restart your system to apply changes.")
				)
			else:
				error_message = stderr.decode().strip()
				QMessageBox.critical(self, _("Error"), _("Failed to apply system language:\n") + error_message)

		except FileNotFoundError:
			QMessageBox.critical(self, _("Error"), _("Required system tools not found. Please ensure 'pkexec', 'sed', and 'locale-gen' are installed."))
		except Exception as e:
			QMessageBox.critical(self, _("Error"), _("An unexpected error occurred:\n") + str(e))


	def check_disk_space(self):
		try:
			total, used, free = shutil.disk_usage("/")
			free_gb = free // (2 ** 30)
			warning_threshold = 10
			error_threshold = 5

			self.disk_space_status.setText(f"{free_gb} GB {_('Free')}")
			if free_gb < error_threshold:
				self.disk_space_status.setStyleSheet("font-weight: bold; color: red;")
			elif free_gb < warning_threshold:
				self.disk_space_status.setStyleSheet("font-weight: bold; color: orange;")
			else:
				self.disk_space_status.setStyleSheet("font-weight: bold; color: green;")
		except Exception as e:
			print(f"Error checking disk space: {e}")
			self.disk_space_status.setText(_("N/A"))

	def update_system_info(self):
		processor_info = None
		if platform.system() == "Linux":
			try:
				with open("/proc/cpuinfo", "r") as f:
					for line in f:
						if "model name" in line:
							processor_info = line.split(":")[1].strip()
							break
			except FileNotFoundError:
				print("Error: /proc/cpuinfo not found.")
			except Exception as e:
				print(f"Error reading /proc/cpuinfo: {e}")

		if not processor_info:
			processor_info = platform.processor() or _("N/A")

		self.processor_info.setText(processor_info)

		try:
			mem = psutil.virtual_memory()
			total_memory_gb = round(mem.total / (1024 ** 3), 2)
			self.memory_info.setText(f"{total_memory_gb} GB")
		except Exception as e:
			print(f"Error getting memory info: {e}")
			self.memory_info.setText(_("N/A"))

	def retranslate_ui(self):
		self.setWindowTitle(_("Welcome to Helwan Linux"))
		self.tabs.setTabText(0, _("Welcome"))
		self.tabs.setTabText(1, _("System Cleaner"))

		if self.app_lang_label:
			self.app_lang_label.setText(_("Application Language:"))
		if self.startup_check:
			self.startup_check.setText(_("Show on startup"))
		if self.pacman_btn_bottom:
			self.pacman_btn_bottom.setText(_("Update System (Pacman)"))
		if self.yay_btn_bottom:
			self.yay_btn_bottom.setText(_("Update System (Yay)"))
			if not is_yay_installed():
				self.yay_btn_bottom.setToolTip(_("Yay is not installed."))
			else:
				self.yay_btn_bottom.setToolTip("")
		if self.install_lts_btn:
			self.install_lts_btn.setText(_("Install Linux LTS"))
		if self.install_zen_btn:
			self.install_zen_btn.setText(_("Install Linux Zen"))
		if self.sys_lang_label:
			self.sys_lang_label.setText(_("System Language:"))
		if self.apply_lang_btn:
			self.apply_lang_btn.setText(_("Apply System Language"))
		if self.docs_btn:
			self.docs_btn.setText(_("Open Documentation"))
		if self.youtube_btn:
			self.youtube_btn.setText(_("Open YouTube Channel"))
		if self.system_info_group:
			self.system_info_group.setTitle(_("System Information"))
		if self.disk_space_label:
			self.disk_space_label.setText(_("Available Disk Space:"))
		if self.processor_label:
			self.processor_label.setText(_("Processor:"))
		if self.memory_label:
			self.memory_label.setText(_("RAM:"))
		if self.neofetch_btn:
			self.neofetch_btn.setText(_("Show System Info Details"))
		if self.htop_btn:
			self.htop_btn.setText(_("Performance Monitor"))
		if self.theme_label:
			self.theme_label.setText(_("Application Theme:"))

		self.greeting.setText(
			_("Welcome to the world of Helwan Linux! ❤️\nWe are here to help you build your dreams on the strongest foundation!"))
		cleaner_group = self.findChild(QGroupBox, "Pacman Cleaner")
		if cleaner_group:
			cleaner_group.setTitle(_("Pacman Cleaner"))
			clean_cache_check = self.findChild(QCheckBox, "clean_pacman_cache_full_check")
			if clean_cache_check:
				clean_cache_check.setText(
					_("Clean Pacman Cache (Full) - Warning! This will remove all downloaded packages."))
			remove_orphan_check = self.findChild(QCheckBox, "remove_orphan_packages_check")
			if remove_orphan_check:
				remove_orphan_check.setText(
					_("Remove Orphan Packages - Packages that are no longer required by any installed package."))
			clean_paccache_keep_check = self.findChild(QCheckBox, "clean_paccache_keep_two_check")
			if clean_paccache_keep_check:
				clean_paccache_keep_check.setText(_("Clean Old Packages (Keep Last 2 Versions)"))
			run_cleanup_button = self.findChild(QPushButton, "run_pacman_cleanup_button")
			if run_cleanup_button:
				run_cleanup_button.setText(_("Run Pacman Cleanup"))
