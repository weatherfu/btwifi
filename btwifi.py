import requests

url = 'https://www.btopenzone.com:8443/ante'
successurl = 'http://detectportal.firefox.com/success.txt'
headers = { 'Host': 'www.btopenzone.com:8443',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded',
'Connection': 'keep-alive',
'Referer': 'https://www.btopenzone.com:8443/home' }

logindata = { 'domain':'',
              'realm':'',
              'CPURL':'',
              'partnerNetwork': 'tbb',
              'username': 'emailaddresshere',
              'password': 'passwordhere',
              'login':'Login' }
while True:
    successreq = requests.get(successurl)
    success = successreq.text.strip()
    print(success)
    if success == 'success':
        print("logged in, sleeping")
        sleep(15) #change this if you want
    else:
        login = requests.post(url, data=logindata, headers=headers)
        print("logging in")
