from paramiko import SSHClient, AutoAddPolicy
from righ import print, pretty, inspect
pretty.install()

client = SSHClient()
client.load_host_keys('~/.ssh/newk.pem')

client.connect('54.147.174.78', username='ubuntu')
