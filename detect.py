import requests
def sql_detect():
    url = f"http://localhost/vulnerabilities/sqli/?id='&Submit=Submit#"
    cookies = {"security":"low", "PHPSESSID":"471qoj0dus8uq4je00d6fkme24", "security":"low"}
    r = requests.get(url, cookies=cookies)
    if "SQL syntax" in r.text:
        print("SQL Injection Detected")

def detect_xss():
    url = f"http://localhost/vulnerabilities/xss_r/?name=%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E "
    cookies = {"security":"low", "PHPSESSID":"471qoj0dus8uq4je00d6fkme24", "security":"low"}
    r = requests.get(url, cookies=cookies)
    print(r.text)

detect_xss()