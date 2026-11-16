"""
test_detector.py - automatic tests for detector.py

Run with:
    python3 -m unittest test_detector.py -v
"""

import unittest
from detector import check_url


class TestSafeUrls(unittest.TestCase):

    def test_google(self):
        self.assertEqual(check_url("https://www.google.com")["result"], "Safe")

    def test_github(self):
        self.assertEqual(check_url("https://github.com")["result"], "Safe")

    def test_indian_bank(self):
        self.assertEqual(check_url("https://www.sbi.co.in")["result"], "Safe")

    def test_real_login_page(self):
        self.assertEqual(check_url("https://accounts.google.com/signin")["result"], "Safe")


class TestPhishingUrls(unittest.TestCase):

    def test_fake_paypal(self):
        report = check_url("http://paypal-secure-login.verify-account.tk/signin")
        self.assertEqual(report["result"], "Phishing")

    def test_ip_address(self):
        report = check_url("http://192.168.10.5/login.php")
        self.assertEqual(report["result"], "Phishing")

    def test_at_symbol(self):
        report = check_url("https://www.google.com@evil-site.ml/login")
        self.assertEqual(report["result"], "Phishing")

    def test_fake_amazon(self):
        report = check_url("http://amazon.com.account-update.xyz/confirm")
        self.assertEqual(report["result"], "Phishing")


class TestSuspiciousUrls(unittest.TestCase):

    def test_shortener(self):
        self.assertEqual(check_url("bit.ly/3xYzAbc")["result"], "Suspicious")


class TestReasons(unittest.TestCase):

    def test_reasons_are_given(self):
        report = check_url("http://192.168.10.5/login.php")
        self.assertTrue(len(report["reasons"]) > 0)

    def test_no_reasons_for_safe_site(self):
        self.assertEqual(check_url("https://github.com")["reasons"], [])


if __name__ == "__main__":
    unittest.main()
