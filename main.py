"""
main.py - command line version of the Phishing URL Detector.

How to run:
    python3 main.py https://example.com      (check one URL)
    python3 main.py -f sample_urls.txt       (check every URL in a file)
    python3 main.py                          (type URLs one by one)
"""

import sys
from detector import check_url

# Colours for the terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

COLOURS = {"Safe": GREEN, "Suspicious": YELLOW, "Phishing": RED}


def show_report(report):
    """Print the result of one URL in a neat format."""
    colour = COLOURS[report["result"]]
    print("-" * 60)
    print("URL     :", report["url"])
    print("Score   :", report["score"])
    print("Result  :", colour + report["result"] + RESET)
    if report["reasons"]:
        print("Reasons :")
        for reason in report["reasons"]:
            print("   *", reason)
    print("-" * 60)


def check_file(file_name):
    """Check every URL written in a text file (one URL per line)."""
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                show_report(check_url(line))


def interactive_mode():
    """Keep asking for URLs until the user types 'exit'."""
    print("=== Phishing URL Detector ===")
    print("Type a URL to check it, or 'exit' to quit.\n")
    while True:
        url = input("Enter URL: ").strip()
        if url.lower() in ("exit", "quit", "q"):
            print("Stay safe online. Bye!")
            break
        if url:
            show_report(check_url(url))


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "-f":
        check_file(sys.argv[2])
    elif len(sys.argv) == 2:
        show_report(check_url(sys.argv[1]))
    else:
        interactive_mode()
