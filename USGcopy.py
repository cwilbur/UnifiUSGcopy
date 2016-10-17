# Rick Mur - Maverick.Solutions - (c) 2016
import logging
import os
import socket
from subprocess import check_output
import paramiko

# Fill in variables for your environment
HOST = "localhost"
USERNAME = "test"
PASSWORD = "testtest"
SSHPORT = 22
RUNNING_ON = "USG"
CONTROLLERFILE = "/var/lib/unifi/sites/default/config.gateway.json"
USGFILE = "config.gateway.json"

# Do not change anything beyond this line, unless you know what you are doing
print ("-----------------------------------------")
print ("Maverick.Solutions - Unifi USG Copy tool")
print ("-----------------------------------------")

try:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    log = logging.getLogger("USGcopy")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOST, SSHPORT, username=USERNAME, password=PASSWORD)
    sftpClient = ssh.open_sftp()

    if RUNNING_ON.lower() == "usg":
        myConfig = check_output(["mca-ctrl", "-t dump-cfg"])
        # DEBUG myConfig = check_output(["cat", "config.gateway.json"])

        sftpClient.put(os.path.realpath(os.path.dirname(__file__)) + "/" + USGFILE, CONTROLLERFILE)
        log.info("File copied to controller")
    elif RUNNING_ON.lower() == "controller":
        stdin, stdout, stderr = ssh.exec_command("mca-ctrl -t dump-cfg > config.gateway.json")
        sftpClient.get(USGFILE, CONTROLLERFILE)
        log.info("File copied from usg")
    else:
        raise Exception("RUNNING_ON variable is not set to USG or Controller")

    sftpClient.close()
    ssh.close()
    log.info("All done! Thank you!")

except Exception as e:
    msg = "Something went wrong: " + str(e.message)
    log.error(msg)



