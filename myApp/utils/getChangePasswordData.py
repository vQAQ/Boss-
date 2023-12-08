from myApp.models import User
import hashlib


def changePassword(userInfo, passwordInfo):
    oldPwd = passwordInfo['oldPassword']
    newPwd = passwordInfo['newPassword']
    checkNewPwd = passwordInfo['checkNewPassword']

    user = User.objects.get(username=userInfo.username)

    md5 = hashlib.md5()
    md5.update(oldPwd.encode())
    oldPwd = md5.hexdigest()

    if oldPwd != user.password:
        return '原始密码不正确'
    if newPwd != checkNewPwd:
        return '两次新密码不相同'

    md5 = hashlib.md5()
    md5.update(newPwd.encode())
    newPwd = md5.hexdigest()

    user.password = newPwd
    user.save()