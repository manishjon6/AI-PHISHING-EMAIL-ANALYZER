![Banner](./images/banner.png)

# 🛡️ AI Phishing Email Analyzer 2026 - SOC Edition

> **Detects BEC, QR Phishing, AI-Generated Phishing in 2026** - 100% FREE with Groq API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Groq](https://img.shields.io/badge/Groq-gpt--oss--20b-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**No OpenRouter needed. No credit card. Works offline fallback.**

### 🎯 Live Demo Output

![Execution](./images/execution.png)

=== AI PHISHING EMAIL ANALYZER 2026 - Groq Free Edition ===

From: phishing@pot
Subject: Fw: Your Bank Account has been blocked...

[*] Trying Groq model: openai/gpt-oss-20b
[OK] Worked with openai/gpt-oss-20b

FINAL VERDICT: PHISHING | RISK: 95%
TYPE: BEC
REASONS:
 - Sender domain mismatch (no.reply.alerts@chase.com vs boonsupply.com)
 - Suspicious URL (dsgo.to short link)
 - Embedded image from unrelated domain (createsend1.com)
 - Urgency language and account suspension claim


### 🏗️ Architecture

eml_file
  -> eml_parser (extract from, subject, urls, body)
  -> header_analyzer (SPF/DKIM/DMARC checks)
  -> qr_decorder (extract & decode QR codes)
  -> vt_checker (VirusTotal URL scan)
  -> llm_analyzer (Groq AI - SOC Analyst reasoning)
  -> FINAL VERDICT: PHISHING / SAFE / SUSPICIOUS

### ⚡ Features (2026 Threats)

- **BEC Detection**: CEO impersonation, domain lookalike
- **QR Code Phishing**: Decodes QR inside email
- **AI Phishing**: Detects LLM-written urgent language
- **URL Obfuscation**: Shorteners, `dsgo.to`, homograph attacks
- **Header Forensics**: SPF/DKIM failure detection

### 🚀 Setup - 2 Minutes, 100% FREE

**1. Get FREE Groq API Key (No credit card)**

Go to: https://console.groq.com/keys
Login with Google -> Create API Key -> Copy `gsk_...`

**2. Install & Run**

```bash
git clone https://github.com/yourusername/ai-phishing-detector.git
cd ai-phishing-detector
pip install groq python-dotenv requests beautifulsoup4 tldextract qrcode[pil] opencv-python

# Create.env file
echo "GROQ_API_KEY=gsk_your_key_here" >.env

python3 main.py
*3. Add your own.eml files*

Drop any phishing email into `samples/` and change path in `main.py`

### 🔧 Models Used

We auto-fallback to latest working free models (Groq changes models monthly):

- `openai/gpt-oss-20b` (Primary - Free, 2026)
- `openai/gpt-oss-120b` (Fallback)
- `qwen/qwen3-32b`
- Local heuristic fallback (if API fails)

> *Note*: Old models `llama-3.3-70b-versatile`, `llama3-8b-8192`, `gemma2-9b-it` are now Enterprise-only or decommissioned on Groq. This project is updated for 2026.

### 📂 Project Structure
├── main.py - Entry point
├── eml_parser.py - Parse.eml
├── llm_analyzer.py - Groq AI SOC analyst
├── header_analyzer.py - Email headers
├── vt_checker.py - VirusTotal
├── qr_decorder.py - QR code decoder
├── samples/bec_test.eml - Test phishing email
└──.env - Your FREE Groq key
### 🤝 Why This Project?

Built after OpenRouter killed all free models in 2026. This version proves you can still build SOC-grade AI tools 100% free using Groq.

*Star ⭐ this repo if it helped you!*
