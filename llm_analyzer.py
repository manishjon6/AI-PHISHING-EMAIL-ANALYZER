import os
import json
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

PROMPT = """You are a SOC Analyst. Score this email.
FROM: {from_addr}
SUBJECT: {subject}
BODY: {body}
URLS: {urls}
Return ONLY JSON: {{"risk_score": 0-100, "verdict": "PHISHING or SAFE", "type": "BEC/QR/AI/NONE", "reasons": ["reason1"]}}"""

def analyze_with_llm(email_data):
    api_key = os.getenv("GROQ_API_KEY")
    client = Groq(api_key=api_key)

    models = [
        "openai/gpt-oss-20b", # NEW FREE MODEL - works now
        "openai/gpt-oss-120b", # NEW FREE MODEL
        "qwen/qwen3-32b",
        "groq/compound-mini"
    ]

    for model in models:
        try:
            print(f"[*] Trying Groq model: {model}")
            completion = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": PROMPT.format(
                    from_addr=email_data['from'],
                    subject=email_data['subject'],
                    body=email_data['body_text'][:2000],
                    urls=email_data['urls']
                )}],
                temperature=0.1
            )
            result = completion.choices[0].message.content
            if "```" in result:
                result = result.split("```")[1].replace("json","").strip()
            print(f"[OK] Worked with {model}")
            return json.loads(result)
        except Exception as e:
            print(f" -> Failed: {e}")
            continue
