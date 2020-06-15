import os
import xlsxwriter
import pandas as pd

print(os.getcwd())
os.chdir("../test")
print(os.getcwd())

# workbook = xlsxwriter.Workbook('test.xlsx')
# worksheet = workbook.add_worksheet()
# row = 0
# column = 0
# content = ["ankit", "rahul", "priya", "harshita",
#            "sumit", "neeraj", "shivam"]
#
# # iterating through content list
# for item in content:
#     # write operation perform
#     worksheet.write(row, column, item)
#
#     # incrementing the value of row by one
#     # with each iteratons.
#     column += 1
# workbook.close()
# os.startfile("test.xlsx")

df = pd.read_excel("2333.xlsx")
df.to_excel("7777.xlsx", index=False)

