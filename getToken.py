import requests,logging

urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)

logging.getLogger('requests').setLevel(logging.CRITICAL)

hosturl= 'http://192.168.0.50:8000/'
token = ""

def getToken():
    urldata = hosturl+'api/auth/token/'
    payload = {'password': 'P@ssw0rd', 'username': 'django'}
    r = requests.post(urldata, data=payload)
    return r.json()['token']


def postData(EndPoint,Payload):
    global token

    if not EndPoint.endswith("/"): EndPoint += "/"
    url = hosturl+EndPoint
    headers = {"Authorization":"JWT "+token}
    r = requests.post(url,headers=headers,data=Payload)
    print(r.status_code)
    if r.status_code == 401:
        token = getToken()
        return postData(EndPoint, Payload)
    return r.text

def patchData(EndPoint,Payload):
    global token

    if not EndPoint.endswith("/"): EndPoint += "/"
    url = hosturl+EndPoint
    headers = {"Authorization":"JWT "+token}
    r = requests.patch(url,headers=headers,data=Payload)
    print(r.status_code)
    #print(r.text)
    if r.status_code == 401:
        token = getToken()
        return patchData(EndPoint, Payload)
    return r.text


