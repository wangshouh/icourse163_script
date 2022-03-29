import requests
import json
from requests.structures import CaseInsensitiveDict
import urllib.parse

def like(s, pid):
    url = "https://www.icourse163.org/dwr/call/plaincall/MocForumBean.markVote.dwr"

    data = f"callCount=1\nscriptSessionId=$scriptSessionId190\nhttpSessionId=9a3b757176934c82b1874ca5bda0eab7\nc0-scriptName=MocForumBean\nc0-methodName=markVote\nc0-id=0\nc0-param0=number:{pid}\nc0-param1=number:{pid}\nc0-param2=number:1\nc0-param3=number:1\nc0-param4=number:0\nbatchId=1648477205532"

    resp = s.post(url, data=data)

    print(resp.text)

def send_comment(pid, comment):
    url = "https://www.icourse163.org/dwr/call/plaincall/MocForumBean.addReply.dwr"

    data = f"callCount=1\nscriptSessionId=$scriptSessionId190\nc0-scriptName=MocForumBean\nc0-methodName=addReply\nc0-id=0\nc0-e1=number:{pid}\nc0-e2=string:{comment}\nc0-e3=number:0\nc0-param0=Object_Object:{{postId:reference:c0-e1,content:reference:c0-e2,anonymous:reference:c0-e3}}\nc0-param1=Array:[]\nbatchId=1648444077749"
    resp = s.post(url, data=data)

    print(resp.status_code)

def get_comment_decode(comments_list):
    comment = random.choice(comments_list)
    comment_decode = urllib.parse.quote(comment)
    return comment_decode

def main(s, pid):
    comments_list = get_comments_list(pid)
    like(pid)
    comment_decode = get_comment_decode(comments_list)
    send_comment(pid, comment_decode)