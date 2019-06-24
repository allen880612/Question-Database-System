
class PathPaser():

    def __init__(self, _path):
        self.path = _path

    def GetPath(self):
        # 設定出示路徑
        base_path = "../database/"
        # 對輸入處理
        if self.path != "":
            path = base_path
            for dir in self.path:
                path += dir + "/"
            print(path)
            return path

        return False



