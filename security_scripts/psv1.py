# Coding needs to be run with python3
#  Reminder (py2's raw_input() is just input() in py3)
# Port scanner for ethical hacking 2019 course

from socket import *
from termcolor import colored 
import optparse
from threading import *

# ^^ importing like this allows you to call functions directly instead of calling the name each time

# !!!!!!
# sock = socket(AF_INET, SOCK_STREAM)

# get user input for host ip address
host = input("--- Enter the host to scan: ")

def portScan(tgtHost, tgtPorts):

def main():
  parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>')
  # dest is a varname, help is a docstring explanation
  parser.add_option('-H', dest="tgHost", type='string', help='specify target host')
  parser.add_option('-H', dest="tgPort", type='string', help='specify target ports, sep by COMMAS')
  (options, args) = parser.parse_args()
  tgtHost = options.tgtHost
  tgtPorts = str(options.tgtPort.split(","))
  if (tgtHost == None) | (tgtPorts[0] == None):
    print parser.usage
    exit(0)
  portScan(tgtHost, tgtPorts)

if __name__ ='__main__':
  main()
# OLDCODE  BELOW
# def portscanner(port):
#   if sock.connect.ex(host.port()):
#     # interpolated var call, second arg is color
#     print(colored("port %d is closed :(" % (port), 'red'))
#   else:
#     print(colored("LOOKIE HERE!!! port %d is open" % (port), 'green'))

# # Scanning range determined below
# for port in range (1, 100):
#   portscanner(port)