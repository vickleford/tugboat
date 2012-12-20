import paramiko
import logging

from config import config


class RemotePuppetUpdater(object):
    
    def __init__(self, environments):
        self.environments = environments
        
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        self.log = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)
        
    def _log_command_output(self, output, error):
        """Log stdout and stderr from Paramiko.SSHClient.exec_command()."""

        stdout = output.read()
        stderr = error.read()

        # don't log empty messages
        if stdout:
            self.log.info(stdout)
        if stderr:
            self.log.error(stderr)

    def _shell_in(self, host, username, keyfile):
        """SSH into the puppetmaster to do your stuff."""

        self.ssh.connect(host, username=username, key_filename=keyfile)

        # alternate for key or password login
        # ...
