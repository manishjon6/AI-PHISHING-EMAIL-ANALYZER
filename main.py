from eml_parser import parse_eml
from qr_decorder import extract_qr_links
import header_analyzer
import vt_checker
import llm_analyzer

print("=== AI PHISHING EMAIL ANALYZER 2026 - Groq Free Edition ===\n")

# Your real phishing email file
file = "samples/bec_test.eml"

try:
    eml = parse_eml(file)
except Exception as e:
    print(f"[*] No EML file, using dummy: {e}")
    eml = {
        "from": "CEO <ceo@micorsoft-secure.com>",
        "subject": "Urgent Wire Transfer Needed",
        "body_text": "Please process urgent wire $45000. Scan QR to view invoice. Click http://micorsoft-secure-payments.com",
        "urls": ["http://micorsoft-secure-payments.com/invoice/123"],
        "html": ""
    }

print(f"From: {eml['from']}\nSubject: {eml['subject']}\nURLs: {eml['urls']}")

# FIX: Define all vars first so no NameError
header_score = 0
qr_found = []
vt_flags = 0

print("\n[!] Checking Email Headers...")
try:
    header_score = header_analyzer.analyze_headers(eml)
except Exception as e:
    print(f"Header check skipped: {e}")

print("\n[!] Checking QR Codes...")
try:
    qr_found = extract_qr_links(eml)
except Exception as e:
    print(f"QR check skipped: {e}")
    qr_found = []

print("\n[!] Checking VirusTotal...")
try:
    vt_flags = vt_checker.check_urls_vt(eml['urls'])
except Exception as e:
    print(f"VT check skipped: {e}")
    vt_flags = 0

print("\n[!] AI Analysis...")
ai_result = llm_analyzer.analyze_with_llm(eml)

print("\n" + "="*50)
print(f"FINAL VERDICT: {ai_result.get('verdict')} | RISK: {ai_result.get('risk_score')}%")
print(f"TYPE: {ai_result.get('type')}")
print(f"REASONS:")
for r in ai_result.get('reasons', []):
    print(f" - {r}")
print(f"VT Flags: {vt_flags}")
print(f"QR Links: {qr_found}")
print("="*50)
