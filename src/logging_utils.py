import os
from datetime import datetime

def log_password_info(pwned_count, strength, length):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_path = os.path.join(log_dir, "password_logs.txt")

    with open(log_path, mode="a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}]\n")
        f.write(f"Sızıntı Sayısı: {pwned_count}\n")
        f.write(f"Parola Gücü: {strength}\n")
        f.write(f"Parola Uzunluğu: {length}\n")
        f.write("-" * 40 + "\n")
