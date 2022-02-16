import itchat
# 登陆
itchat.auto_login()   # 可设置hotReload = True
# 运行并保持在线状态
itchat.run()
itchat.send('Hello', toUserName='filehelper')
