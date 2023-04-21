
def palindrom(text):
    words = text.split()
    palindromes = []
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes

import re

def validate_ip(ip_address):
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if not re.match(pattern, ip_address):
        return False
    octets = ip_address.split('.')
    for octet in octets:
        if not 0 <= int(octet) <= 255:
            return False
    return True

import platform

def get_os():
    system = platform.system()
    if system == 'Darwin':
        return 'Mac'
    elif system == 'Windows':
        return 'Windows'
    elif system == 'Linux':
        return 'Linux'
    else:
        return None