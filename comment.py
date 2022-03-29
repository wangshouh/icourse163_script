import re
import requests


def get_comments_list(s, pid):

    url = "https://www.icourse163.org/dwr/call/plaincall/PostBean.getPaginationReplys.dwr"

    payload = f"callCount=1\nscriptSessionId=$scriptSessionId190\nc0-scriptName=PostBean\nc0-methodName=getPaginationReplys\nc0-id=0\nc0-param0=number:{pid}\nc0-param1=number:2\nc0-param2=number:2\nbatchId=1648445424731"
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }

    response = s.post(url, headers=headers, data=payload)

    comment_list = re.findall('''(?<=content=\").*(?=\";)''', response.text)
    comments_list = []
    for comment in comment_list:
        comments_list.append(comment.encode('ascii').decode('unicode-escape'))

    return comments_list