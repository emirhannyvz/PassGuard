# 🔐 PassGuard -Parola Güvenlik Analiz Aracı

**Parola Güvenlik Analiz Aracı**, kullanıcıların girdikleri parolaların güçlü olup olmadığını analiz eden ve parolanın veri sızıntılarında yer alıp almadığını kontrol eden Python tabanlı bir uygulamadır. Proje, parola güvenliği ve dijital adli bilişim alanlarında pratik bir araç sunar.

---

## 🛠️ Özellikler

- 🔍 **Parola Veri Sızıntısı Kontrolü**  
  Parolanın daha önce veri sızıntılarında (HaveIBeenPwned API kullanılarak) yer alıp almadığını sorgular.

- 🔐 **Güçlü Parola Analizi**  
  Parolanın uzunluk, karakter çeşitliliği ve karmaşıklığına göre güvenlik seviyesi hesaplanır.

- 🗂️ **Hash Fonksiyonları ile Parola İşleme**  
  Parola MD5, SHA-1, SHA-256 gibi algoritmalarla hash’lenir ve adli bilişim amaçlı loglanır. Parola düz metin olarak loglanmaz.

- 📋 **Loglama ve Analiz**  
  Tüm analiz sonuçları, şifrelenmiş hash’ler ve kontrol sonuçları CSV dosyasına kaydedilir. Loglar kolay okunabilir formatta saklanır.

- 💻 **Kullanıcı Dostu Arayüz**  
  PyQt5 ile geliştirilmiş sade ve modern GUI, kullanıcıların kolayca parola girmesini, kontrol yapmasını ve logları görüntülemesini sağlar.

---

## 📂 Proje Yapısı

```plaintext
PassGuard/
│
├─ src/
│   ├─ main.py
│   ├─ api_check.py
│   ├─ password_strength.py
│   └─ logging_utils.py
├─ logs/
│   └─ password_logs.txt
├─ requirements.txt
├─ README.md
└─ LICENSE

```

## 🚀 Kurulum ve Kullanım

### Gereksinimler

- Python 3.7+
- Gerekli paketler: `PyQt5`, `requests`

### Kurulum

```bash
pip install -r requirements.txt
```
