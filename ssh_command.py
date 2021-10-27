from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
import paramiko

pretty.install()
k = paramiko.RSAKey.from_private_key_file("/Users/x/.ssh/newk.pem")

client = SSHClient()
client.load_host_keys('/Users/x/.ssh/known_hosts')
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('54.147.174.78', username='ubuntu', pkey= k, port=19999)

#inspect(client, methods=True)

stdin, stdout, stderr = client.exec_command('free')

if stdout.channel.recv_exit_status() == 0:
	print(f'STDOUT: {stdout.read().decode("utf8")}')
else:
	print(f'STDOUT: {stdout.read().decode("utf8")}')

stdin.close()
stdout.close()
stderr.close()

#CLOSE SSH CLIENT
client.close
