import requests
import json
def test111():
    url = "http://web.dcyun.com:10096/RiverMasterUpload/api/CitySent/ListProblemlPage"
    payload = {'userName': 'jhpt',
               'authkey': '41FA7112',
               'token': '41FA7112',
               'startTime': '2021-11-1',
               'endTime': '2021-11-17',
               'PageIndex': '1',
               'PageSize': '20'}
    res = requests.post(url=url, data=payload)
    r = res.json()
    print(json.dumps(r, indent=4))
test111()