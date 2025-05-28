import re

def password_strength(password):
    """
    Basit parola gücü ölçümü.
    5 kriter kontrolü:
    - En az 8 karakter
    - Küçük harf
    - Büyük harf
    - Rakam
    - Özel karakter
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/]", password):
        score += 1

    if score == 5:
        return "Çok Güçlü"
    elif score >= 3:
        return "Orta"
    elif score >= 1:
        return "Zayıf"
    else:
        return "Çok Zayıf"
