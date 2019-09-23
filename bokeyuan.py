# coding:utf-8

import requests

# 先建立session
session = requests.session()
url1 = 'https://www.cnblogs.com/edison0621/p/11567800.html'
session.get(url = url1)


#设置cookies,并更新
cookiejar = requests.cookies.RequestsCookieJar()
cookiejar.set('.Cnblogs.AspNetCore.Cookies','输入抓到的信息')
cookiejar.set('.CNBlogsCookie','输入抓到的信息')
session.cookies.update(cookiejar)


# 保存草稿箱
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {
    "__VIEWSTATE": "",
    "__VIEWSTATEGENERATOR":"FE27D343",
    "Editor$Edit$txbTitle":"python_caogao",
    "Editor$Edit$EditorBody":"<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
    "Editor$Edit$Advanced$ckbPublished":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkComments":"on",
    "Editor$Edit$Advanced$chkMainSyndication":"on",
    "Editor$Edit$Advanced$txbEntryName":"",
    "Editor$Edit$Advanced$txbExcerpt":"",
    "Editor$Edit$Advanced$txbTag":"",
    "Editor$Edit$Advanced$tbEnryPassword":"",
    "Editor$Edit$lkbDraft":"存为草稿"
}

r2 = session.post(url = url2, data=body, verify=False)
print (r2)