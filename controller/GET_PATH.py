import os

class PathPaser():

    def __init__(self, _path):
        self.path = _path

    def GetPath(self):
        # 設定出示路徑
        base_path = "database/"
        # 對輸入處理
        if self.path != "":
            path = base_path
            #path = ""
            for dir in self.path:
                path += dir + "/"
            print(path)
            return path

        return False


# 給目前路徑，回傳底下資料夾
class FolderManager():
    def __init__(self):
        pass

    def GetNextLevel(self, _path):
        if os.path.isdir(_path):
            return os.listdir(_path)
        return False





