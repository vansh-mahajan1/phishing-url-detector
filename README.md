# Phishing URL Detector

A simple **rule-based phishing URL detector** written in Python.
You give it a website link and it tells you whether the link looks
**Safe**, **Suspicious** or **Phishing**, along with the reasons.

Made as a mini project for the **Version Control System (VCS)** subject.
The whole project was built and managed using basic **Git** and **GitHub CLI** commands.

## Team

| Name | Roll No. |
|------|----------|
| Vansh Mahajan | 2581318 |
| Gaurav Kaushik | 2581213 |
| Aditya Chaturvedi | 2581406 |

**Guided by:** Dr. Pooja Batra

## What is phishing?

Phishing is a cyber attack where scammers send **fake links** that look like
real websites (banks, PayPal, Google, Netflix, etc.) to steal passwords,
OTPs or card details. This tool checks a link **before** you open it.

## Features

- Checks a URL using **12 simple rules** and gives a **risk score**
- Shows the result as **Safe / Suspicious / Phishing** with reasons
- **Command line** version (`main.py`) – single URL, file of URLs, or interactive
- **Web page** version (`app.py`) made with Flask
- **Unit tests** (`test_detector.py`) using Python's `unittest`

## Rules used

| # | Rule | Points |
|---|------|--------|
| 1 | IP address instead of domain name | 3 |
| 2 | `@` symbol in URL | 3 |
| 3 | URL longer than 75 characters | 1 |
| 4 | No HTTPS | 1 |
| 5 | `-` in domain name | 1 |
| 6 | Too many sub-domains | 2 |
| 7 | Suspicious words (login, verify, bank, free…) | 1–3 |
| 8 | URL shortener (bit.ly, tinyurl…) | 2 |
| 9 | Risky domain ending (.tk, .xyz, .top…) | 2 |
| 10 | Brand name in a fake domain (paypal-login.com) | 2 |
| 11 | Punycode look-alike letters (`xn--`) | 2 |
| 12 | Hidden `//` redirect | 1 |

**Score 0–2 → Safe, 3–5 → Suspicious, 6 or more → Phishing**

## Project structure

```
phishing-url-detector/
├── detector.py        # rules + scoring (main logic)
├── main.py            # command line app
├── app.py             # Flask web app
├── templates/
│   └── index.html     # web page
├── test_detector.py   # unit tests
├── sample_urls.txt    # example URLs
├── requirements.txt   # needed libraries (flask)
├── GIT_COMMANDS.md    # all git / GitHub CLI commands used
└── README.md
```

## How to run

```bash
git clone https://github.com/vansh-mahajan1/phishing-url-detector.git
cd phishing-url-detector

# Command line
python3 main.py https://www.google.com
python3 main.py -f sample_urls.txt
python3 main.py

# Web page
pip install -r requirements.txt
python3 app.py          # open http://127.0.0.1:5000

# Tests
python3 -m unittest test_detector.py -v
```

## Example output

```
URL     : http://paypal-secure-login.verify-account.tk/signin
Score   : 9
Result  : Phishing
Reasons :
   * Does not use HTTPS (connection is not secure)
   * Domain name contains '-' (common in fake sites)
   * Suspicious words found: login, signin, verify, secure, account
   * Uses a risky domain ending (.tk)
   * Pretends to be 'paypal' but is not the official site
```

## Version control workflow

- `main` – stable code
- `feature/url-checker` – detection logic + command line app
- `feature/web-app` – Flask web page
- Feature branches were merged into `main` using `git merge`
- Release tagged as `v1.0`

All commands are listed in [GIT_COMMANDS.md](GIT_COMMANDS.md).

## Limitations

This is a rule-based student project. It can miss new tricks and may
sometimes flag a real site. Real tools also use blacklists, machine
learning and website screenshots.
