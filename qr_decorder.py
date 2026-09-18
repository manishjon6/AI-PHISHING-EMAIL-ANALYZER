def extract_qr_links(eml_data):
    print("[!] Checking for QR Code Phishing...")
    # For demo we check if email mentions QR + link
    if "qr" in eml_data['body_text'].lower() and "scan" in eml_data['body_text'].lower():
        print(" [SUSPICIOUS] Email asks to scan QR - common 2026 bypass technique")
        return True
    return False
