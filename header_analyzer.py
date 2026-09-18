def analyze_headers(eml_data):
    print("\n[!] Checking Email Headers...")
    from_addr = eml_data['from']
    # Check for display name spoofing: CEO <attacker@evil.com>
    if "ceo" in from_addr.lower() or "cfo" in from_addr.lower():
        if "gmail.com" not in from_addr and "yourdomain.com" not in from_addr:
            print(f" [HIGH] Possible BEC: Display name spoofing -> {from_addr}")
            return 80
    # Check typosquat
    if "micorsoft" in from_addr or "gooogle" in from_addr:
        print(f" [CRITICAL] Typosquat domain: {from_addr}")
        return 90
    return 10
