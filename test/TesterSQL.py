import  pymysql as mysql
#import mysql.connector

if __name__ == '__main__':
	db = mysql.connect(host="192.168.66.45",user="t106590035",passwd="zzxcv1234",db="mysql",port=3306,charset='utf8')
	#db = mysql.connector.connect(host="192.168.179.148",user="newuser",passwd="12345678")