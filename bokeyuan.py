# coding:utf-8

import requests

# 先建立session
session = requests.session()
url1 = 'https://www.cnblogs.com/edison0621/p/11567800.html'
session.get(url = url1)


#设置cookies,并更新
cookiejar = requests.cookies.RequestsCookieJar()
cookiejar.set('.Cnblogs.AspNetCore.Cookies','CfDJ8DeHXSeUWr9KtnvAGu7_dX8Rd4vt2Im3VWgxGKUw9GfhGIkhEPOcXTal-e0J0KbnaNnzk9a6ObYM9aSvWWrVsgmZZ5khLX5SY7aQuj0VJNh6djuAzUVd3gZfBYZ4YzernmYEcmzMd_0hLkWCEpGmhubuapyf1LUp0okJMN2WXrMls9W_RVEZSE5U1ILZMX1dmcvMBba-V9GbzOJJQY7X3zUiuRSnJFEp4VbnFbLNB22zD3L1h8jD_-lsRb9tI3OCBraUoNHmH0ePEEUycJ7ml2BTh9lgRlUckWnKGSUQ2Ba7iWtffUUtDv7ApD4aGRdF5lFhalmoik5cK6YKLqQtgRf_V2Kycc19rmZl-qNqQ0L61JOC_OVFTxwV3dk8_wzTweTja1sP6_RrR4GP3rjnm1YfK7jhcl2o54agqL3mAdJ_oTePfnjYpCTeCqUTredntM7Q9sJXsIK2ZzUljhoeqFo')
cookiejar.set('.CNBlogsCookie','B28417CAE29C77610469EECEADEAEC1A64BE72421D3C599AAD9382367BD8F6A09AA4732FE9DC3A397EE1A0786EE94525E41DE3C1DF3A7B2D10BC960913A861B5C7ACD6684BF25B64D0572FCDEB4C8BEACEE7FE25')
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