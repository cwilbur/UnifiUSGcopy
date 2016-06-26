# Rick Mur - Maverick.Solutions - (c) 2016
import paramiko
import socket
import logging
import os
from subprocess import check_output

# Fill in variables for your environment
HOST = "localhost"
USERNAME = "test"
PASSWORD = "testtest"
SSHPORT = 22
RUNNING_ON = "USG"
CONTROLLERFILE = "/var/lib/unifi/sites/default/config.gateway.json"
USGFILE = "/config.gateway.json"

# Do not change anything beyond this line, unless you know what you are doing
print ("-----------------------------------------")
print ("Maverick.Solutions - Unifi USG Copy tool")
print ("-----------------------------------------")

try:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    log = logging.getLogger("USGcopy")

    myConfig = check_output(["mca-ctrl", "-t dump-cfg"])
    # DEBUG myConfig = check_output(["cat", "config.gateway.json"])

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((HOST, SSHPORT))
    trans = paramiko.Transport(socket)
    trans.connect(username=USERNAME, password=PASSWORD)

    sftpClient = paramiko.SFTPClient.from_transport(trans)

    if RUNNING_ON.lower() == "usg":
        sftpClient.put(os.path.realpath(os.path.dirname(__file__)) + USGFILE, CONTROLLERFILE)
        log.info("File copied to controller")
    elif RUNNING_ON.lower() == "controller":
        sftpClient.get(USGFILE, CONTROLLERFILE)
        log.info("File copied from usg")
    else:
        raise Exception("RUNNING_ON variable is not set to USG or Controller")

    log.info("All done! Thank you!")

except Exception as e:
  msg = "Something went wrong: " + str(e.message)
  log.error(msg)



