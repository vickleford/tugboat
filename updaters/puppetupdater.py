import paramiko
import logging

from tugboat.config import config
from tugboat.config import args

log = logging.getLogger(__name__)

class PuppetUpdater(object):
    
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def _log_command_output(self, output, error):
        """Log stdout and stderr from Paramiko.SSHClient.exec_command()."""
    
        stdout = output.read()
        stderr = error.read()
        log.info(stdout)
        if stderr:
            log.error(stderr)

    def _shell_in(self, host, username, keyfile):
        """SSH into the puppetmaster to do your stuff."""
    
        self.ssh.connect(host, username=username, keyfile=keyfile)
        
        # alternate for key or password login
        # ...

    def _git_pull(self, directory, branch='master'):
        """Pull the latest from a git repository."""
    
        cd = "cd " + directory
        go_to_branch = "sudo git checkout " + branch
        pull = "sudo git pull"

        stdin, stdout, stderr = self.ssh.exec_command(cd)
        _log_command_output(stdout, stderr)
    
        stdin, stdout, stderr = self.ssh.exec_command(go_to_branch)
        _log_command_output(stdout, stderr)
    
        stdin, stdout, stderr = self.ssh.exec_command(pull)
        _log_command_output(stdout, stderr)

    def update(self):
        """Update each environment specified and each project specified in each environment."""
        
        host = config['puppetmaster']['server']
        user = config['puppetmaster']['user']
        key = config['puppetmaster']['key']
        
        try:
            self._shell_in(host, user, key)

            if args.manifests:
                # Update site manifests if asked to
                self._git_pull(config['puppetmaster']['manifests'])
    
            # expect multiple projects in multiple envs or just one env
            for environment in args.environments:
                update_target = config['puppetmaster']['modulepath'] + '/' + environment
                self._git_pull(update_target)
                for project in args.projects:
                    update_target += '/' + project
                    self._git_pull(update_target)
    
        finally:
            self.ssh.close()