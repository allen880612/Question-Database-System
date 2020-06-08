# coding=UTF-8
import sys
import os
sys.path.append('../controller')
sys.path.append('../model')

import test

now_path = os.getcwd()
print("當前路徑" + now_path)
now_path = "../database"

path_list = os.listdir(now_path)
print("當前資料 ", end = ' ')
print(path_list)

sub_dir = now_path + "/" + path_list[0];
print("底目錄data ", end = ' ')
words = os.listdir(sub_dir)
print(words)

print("===================================")
final_path = sub_dir + "/" + words[0]
print(final_path)
f = open(final_path, encoding="UTF-8", errors="ignore")
data = f.read()
print(data)
f.close()

# pass_correct = True
# if pass_correct:
#     print("路徑無誤")
#
# else:
#     print("路徑錯誤")
#     print()


