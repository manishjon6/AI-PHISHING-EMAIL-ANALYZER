from eml_parser import parse_eml
from qr_decorder import extract_qr_links
import header_analyzer
import vt_checker
import llm_analyzer

print("=== AI PHISHING EMAIL ANALYZER 2026 - Groq Free Edition ===\n")
file = "samples/bec_test.eml"
eml = parse_eml(file)

print(f"From: {eml['from']}\nSubject: {eml['subject']}\nURLs: {eml['urls']}")

header_score = header_analyzer.analyze_headers(eml)
vt_flags = vt_checker.check_urls_vt(eml['urls'])
ai_result = llm_analyzer.analyze_with_llm(eml)

print("\n" + "="*50)
print(f"✅ FINAL VERDICT: {ai_result.get('verdict')} | RISK: {ai_result.get('risk_score')}%")
print(f"📧 TYPE: {ai_result.get('type')}")
print(f"🔍 REASONS:")
for r in ai_result.get('reasons', []):
    print(f"   - {r}")
print(f"🔗 URLs: {eml['urls']}")
print(f"🛡️  VirusTotal Flags: {vt_flags}")
print(f"📷 QR Links: {qr_found}")
print("="*50)
