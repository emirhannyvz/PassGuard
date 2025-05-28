"""
Password Security Analyzer
--------------------------
Basit bir parola güvenlik analiz aracı.
Simple password security analyzer app with PyQt5.

Author: Emirhan
License: MIT
"""

import sys
import os
import time
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QStackedWidget
)
from PyQt5.QtCore import Qt, QTimer
from hashlib import md5, sha1, sha256

from api_check import check_password_pwned_sha1
from password_strength import password_strength
from logging_utils import log_password_info

class MainMenu(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.title = QLabel("Parola Güvenlik Analiz Aracı")
        self.title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(self.title, alignment=Qt.AlignCenter)

        self.start_button = QPushButton("Parola Analizi Başlat")
        self.start_button.setFixedSize(220, 40)
        self.start_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.start_button.setStyleSheet("border-radius: 8px; padding: 6px; background-color: #007BFF; color: white;")
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)

        self.logs_button = QPushButton("Logları Görüntüle")
        self.logs_button.setFixedSize(220, 40)
        self.logs_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.logs_button.setStyleSheet("border-radius: 8px; padding: 6px; background-color: #6c757d; color: white;")
        layout.addWidget(self.logs_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

class PasswordCheckerApp(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #f4f4f4; font-family: Arial;")
        layout = QVBoxLayout()

        self.label = QLabel("Parola girin:")
        self.label.setStyleSheet("font-size: 16px; margin: 10px;")
        layout.addWidget(self.label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(
            "padding: 8px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; background-color: white;"
        )
        layout.addWidget(self.password_input)

        self.check_button = QPushButton("Kontrol Et")
        self.check_button.setStyleSheet(
            "background-color: #28a745; color: white; padding: 10px; font-weight: bold; border-radius: 8px;"
        )
        self.check_button.clicked.connect(self.start_delay)
        layout.addWidget(self.check_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 6px;")
        layout.addWidget(self.result_text)

        self.back_button = QPushButton("Ana Menüye Dön")
        self.back_button.setStyleSheet("background-color: #dc3545; color: white; padding: 8px; border-radius: 6px;")
        self.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def start_delay(self):
        self.result_text.setText("Parola kontrol ediliyor, lütfen bekleyin...")
        QTimer.singleShot(1500, self.check_password)

    def check_password(self):
        pwd = self.password_input.text()
        if not pwd:
            self.result_text.setText("Lütfen bir parola girin.")
            return

        # Hash işlemleri yine yapılacak, ama kullanıcıya gösterilmeyecek
        md5_hash = md5(pwd.encode()).hexdigest()
        sha1_hash = sha1(pwd.encode()).hexdigest()
        sha256_hash = sha256(pwd.encode()).hexdigest()

        pwned_result, pwned_info = check_password_pwned_sha1(sha1_hash)
        strength = password_strength(pwd)

        # Mesajı sadece anlamlı bilgilerle oluştur
        msg = ""
        if pwned_result is True:
            msg += f"⚠️ Parola {pwned_info} kez sızdırıldı!\n"
        elif pwned_result is False:
            msg += "✅ Parola veri sızıntısında bulunamadı.\n"
        else:
            msg += f"Hata: {pwned_info}\n"

        msg += f"Parola Gücü: {strength}"
        self.result_text.setText(msg)

        # Loglama için hashler burada kullanılabilir, ama gösterme
        if pwned_result is not None:
            log_password_info(
                pwned_count=pwned_info if isinstance(pwned_info, int) else 0,
                strength=strength,
                length=len(pwd)
            )


class LogViewer(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setStyleSheet("background-color: #f4f4f4; font-family: Arial;")

        self.label = QLabel("Log Kayıtları:")
        self.label.setStyleSheet("font-size: 16px; margin: 10px;")
        layout.addWidget(self.label)

        self.log_viewer = QTextEdit()
        self.log_viewer.setReadOnly(True)
        self.log_viewer.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 6px;")
        layout.addWidget(self.log_viewer)

        self.back_button = QPushButton("Ana Menüye Dön")
        self.back_button.setStyleSheet("background-color: #dc3545; color: white; padding: 8px; border-radius: 6px;")
        self.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(self.back_button)

        # Klasör ve dosya kontrolü:
        log_path = os.path.join("logs", "password_logs.txt")
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                self.log_viewer.setText(f.read())
        else:
            self.log_viewer.setText("Log dosyası bulunamadı.")




        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    menu = MainMenu(stacked_widget)
    checker = PasswordCheckerApp(stacked_widget)
    logs = LogViewer(stacked_widget)
    stacked_widget.addWidget(menu)
    stacked_widget.addWidget(checker)
    stacked_widget.addWidget(logs)
    stacked_widget.setFixedSize(500, 400)
    stacked_widget.show()
    sys.exit(app.exec_())
