import requests

def check_password_pwned_sha1(sha1_hash):
    """
    HaveIBeenPwned API ile SHA1 hash kontrolü yapar.
    İlk 5 karakteri gönderir, dönen listede devamı aranır.
    """
    try:
        prefix = sha1_hash[:5].upper()
        suffix = sha1_hash[5:].upper()
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)
        if response.status_code != 200:
            return None, f"API hatası: {response.status_code}"

        hashes = (line.split(":") for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return True, int(count)
        return False, 0
    except Exception as e:
        return None, str(e)
