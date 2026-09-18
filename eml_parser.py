import email, re
from email import policy
from bs4 import BeautifulSoup

def parse_eml(file_path):
    with open(file_path, 'rb') as f:
        msg = email.message_from_binary_file(f, policy=policy.default)

    body_text, urls = "", []
    body_html = ""

    for part in msg.walk():
        try:
            if part.get_content_type() == "text/plain":
                body_text += part.get_content()
            if part.get_content_type() == "text/html":
                body_html = part.get_content()
                soup = BeautifulSoup(body_html, 'html.parser')
                urls = [a['href'] for a in soup.find_all('a', href=True)]
        except: pass

    urls += re.findall(r'https?://[^\s"<>]+', body_text)

    return {
        "subject": str(msg['subject']),
        "from": str(msg['from']),
        "headers": dict(msg.items()),
        "body_text": body_text[:4000],
        "urls": list(set(urls))[:10],
        "html": body_html
    }
