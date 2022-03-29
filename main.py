import requests
import json
from requests.structures import CaseInsensitiveDict
import urllib.parse

def like(s, pid):
    url = "https://www.icourse163.org/dwr/call/plaincall/MocForumBean.markVote.dwr"

    data = f"callCount=1\nscriptSessionId=$scriptSessionId190\nhttpSessionId=9a3b757176934c82b1874ca5bda0eab7\nc0-scriptName=MocForumBean\nc0-methodName=markVote\nc0-id=0\nc0-param0=number:{pid}\nc0-param1=number:{pid}\nc0-param2=number:1\nc0-param3=number:1\nc0-param4=number:0\nbatchId=1648477205532"

    resp = s.post(url, data=data)

    print(resp.text)