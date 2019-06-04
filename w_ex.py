import requests
import sys

var1 = sys.argv[1] # token

URL = 'http://hotsix.kro.kr/re_result.php'
data = {'token': var1, 'CVE2019-1002101': 'ture','CVE2019-9946': 'ture', 'CVE2018-1002105': 'ture'}
res = requests.post(URL, data=data)
print(res.text)

