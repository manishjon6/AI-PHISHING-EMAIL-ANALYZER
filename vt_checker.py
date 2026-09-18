import requests, os, tldextract

def check_urls_vt(urls):
    print("\n[!] Checking VirusTotal...")
    key = os.getenv("VIRUSTOTAL_API_KEY")
    if not key:
        print(" [SKIP] No VT key, skipping")
        return []

    flagged = 0
    for url in urls:
        try:
            domain = tldextract.extract(url).registered_domain
            if not domain: continue
            r = requests.get(f"https://www.virustotal.com/api/v3/domains/{domain}",
                             headers={"x-apikey": key}, timeout=10)
            if r.status_code == 200:
                m = r.json()['data']['attributes']['last_analysis_stats']['malicious']
                if m > 2:
                    print(f" [CRITICAL] VT: {domain} flagged by {m} engines")
                    flagged += 1
        except: pass
    return flagged
