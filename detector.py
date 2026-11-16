"""
detector.py - the brain of the Phishing URL Detector.

It checks a URL against a list of simple rules. Every rule that matches
adds points to a "risk score". The final score decides the result:

    score 0 - 2  -> Safe
    score 3 - 5  -> Suspicious
    score 6+     -> Phishing
"""

import re
from urllib.parse import urlparse

# Words that phishing links often use to trick people
SUSPICIOUS_WORDS = [
    "login", "signin", "verify", "update", "secure", "account",
    "banking", "confirm", "password", "wallet", "free", "lucky",
    "bonus", "prize", "suspend", "unlock",
]

# Popular link-shortening services (they hide the real website)
SHORTENERS = ["bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly", "is.gd", "cutt.ly"]

# Cheap / free domain endings that are often misused
RISKY_TLDS = [".tk", ".ml", ".ga", ".cf", ".gq", ".xyz", ".top", ".zip", ".click"]

# Big brands that scammers like to copy
BRANDS = ["paypal", "google", "facebook", "instagram", "amazon", "apple",
          "microsoft", "netflix", "sbi", "hdfc", "icici", "paytm"]


def add_scheme(url):
    """Add http:// if the user forgot it, so urlparse can read the URL."""
    if not url.startswith(("http://", "https://")):
        return "http://" + url
    return url


def check_url(url):
    """
    Check one URL and return a dictionary like:
    {"url": ..., "score": 4, "result": "Suspicious", "reasons": [...]}
    """
    url = url.strip()
    full_url = add_scheme(url)
    parsed = urlparse(full_url)
    domain = (parsed.hostname or "").lower()
    lower_url = full_url.lower()

    score = 0
    reasons = []

    # Rule 1: IP address used instead of a domain name
    if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", domain):
        score += 3
        reasons.append("Uses an IP address instead of a website name")

    # Rule 2: '@' symbol (browser ignores everything before it)
    if "@" in full_url:
        score += 3
        reasons.append("Contains '@' symbol which can hide the real website")

    # Rule 3: very long URL
    if len(full_url) > 75:
        score += 1
        reasons.append("URL is very long (" + str(len(full_url)) + " characters)")

    # Rule 4: no HTTPS
    if parsed.scheme != "https":
        score += 1
        reasons.append("Does not use HTTPS (connection is not secure)")

    # Rule 5: hyphen in domain, e.g. paypal-secure-login.com
    if "-" in domain:
        score += 1
        reasons.append("Domain name contains '-' (common in fake sites)")

    # Rule 6: too many sub-domains, e.g. login.paypal.com.secure.xyz
    if domain.count(".") >= 3:
        score += 2
        reasons.append("Too many sub-domains (" + str(domain.count(".")) + " dots)")

    # Rule 7: suspicious words
    found_words = [word for word in SUSPICIOUS_WORDS if word in lower_url]
    if found_words:
        score += min(len(found_words), 3)
        reasons.append("Suspicious words found: " + ", ".join(found_words))

    # Rule 8: URL shortener
    if domain in SHORTENERS:
        score += 2
        reasons.append("Uses a URL shortener which hides the real link")

    # Rule 9: risky domain ending
    for tld in RISKY_TLDS:
        if domain.endswith(tld):
            score += 2
            reasons.append("Uses a risky domain ending (" + tld + ")")
            break

    # Rule 10: brand name used but it is NOT the real brand website
    for brand in BRANDS:
        if brand in domain and not is_official_domain(domain, brand):
            score += 2
            reasons.append("Pretends to be '" + brand + "' but is not the official site")
            break

    # Rule 11: punycode (look-alike letters, e.g. xn--pple-43d.com)
    if "xn--" in domain:
        score += 2
        reasons.append("Uses punycode (look-alike characters)")

    # Rule 12: '//' after the domain (hidden redirect)
    if "//" in full_url[full_url.find("://") + 3:]:
        score += 1
        reasons.append("Contains '//' redirect inside the URL")

    return {
        "url": url,
        "score": score,
        "result": get_result(score),
        "reasons": reasons,
    }


def is_official_domain(domain, brand):
    """True if domain is like 'paypal.com' or 'www.paypal.com' or 'paypal.co.in'."""
    parts = domain.split(".")
    if parts[0] == "www":
        parts = parts[1:]
    return len(parts) >= 2 and parts[0] == brand and len(parts) <= 3 and "-" not in domain


def get_result(score):
    """Turn the score into Safe / Suspicious / Phishing."""
    if score >= 6:
        return "Phishing"
    if score >= 3:
        return "Suspicious"
    return "Safe"
