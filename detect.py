import requests
def sql_detect():
    url = f"http://localhost/vulnerabilities/sqli/?id='&Submit=Submit#"
    cookies = {"security":"low", "PHPSESSID":"471qoj0dus8uq4je00d6fkme24", "security":"low"}
    r = requests.get(url, cookies=cookies)
    if "SQL syntax" in r.text:
        print("SQL Injection Detected")
    else:
        print("SQL Injection Not Detected")

def detect_xss():
    url = f"http://localhost/vulnerabilities/xss_r/?name=%3Ch1%3EHello%3C%2Fh1%3E "
    cookies = {"security":"low", "PHPSESSID":"471qoj0dus8uq4je00d6fkme24", "security":"low"}
    r = requests.get(url, cookies=cookies)
    if  "<h1>Hello</h1>" in r.text:
        print("XSS Detected")
    else:
        print("XSS Not Detected")

def main():
    print("""
    1. Detect SQL
    2. Detect XSS
    """)
    detect = input("Select an option: ")
    if detect == "1":
        sql_detect()
    elif detect == "2":
        detect_xss()
    else:
        print("Invalid Option")

main()