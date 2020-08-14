import os

exe_name = "cloud_sql_proxy.exe"
sql_id = "psyched-circuit-286314:asia-east1:xtest00=tcp:3306"
key_name = "qds_key.json"
cmd1 = "-instances=" + sql_id
cmd2 = "-credential_file=" + key_name
full_cmd = exe_name + " " + cmd1 + " " + cmd2 + " "
os.popen(full_cmd)