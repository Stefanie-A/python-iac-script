# Importing paramiko
import paramiko

command = "df"

hostname= input("Please enter your ip address: ")
password = input("Please enter your password: ")
username = input("Login as: ")


ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=hostname, username=username,password=password)
_stdin, _stdout,_stderr = ssh_client.exec_command("df")
print(_stdout.read().decode())
ssh_client.close()