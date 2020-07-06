import os

def mkDir(path):
    path = path.strip()
    path = path.rstrip('\\')

    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print('创建成功！')
        return path
    else:
        print('目录已存在！')
        return False

# mydir = 'f:\\pyfiles\\web\\'
# mkDir(mydir)