import paramiko
import logging

from tugboat.config import config
from tugboat.config import args

log = logging.getLogger(__name__)

def _log_command_output(output, error):
    """Log stdout and stderr from Paramiko.SSHClient.exec_command()."""
    
    stdout = output.read()
    stderr = error.read()
    log.info(stdout)
    if stderr:
        log.error(stderr)

def _shell_in(host, username, keyfile):
    """SSH into the puppetmaster to do your stuff."""
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, keyfile=keyfile)

def _git_pull(directory, branch='master'):
    """Pull the latest from a git repository."""
    
    cd = "cd " + directory
    go_to_branch = "git checkout " + branch
    pull = "sudo git pull"

    stdin, stdout, stderr = self.ssh.exec_command(cd)
    _log_command_output(stdout, stderr)
    
    stdin, stdout, stderr = self.ssh.exec_command(go_to_branch)
    _log_command_output(stdout, stderr)
    
    stdin, stdout, stderr = self.ssh.exec_command(pull)
    _log_command_output(stdout, stderr)

def update():
    """Update each environment specified and each project specified in each environment."""

    try:
        _shell_in()

        if args.manifests:
            # Update site manifests if asked to
            _git_pull(config['puppetmaster']['manifests'])
    
        # expect multiple projects in multiple envs or just one env
        for environment in args.environments:
            update_target = ['puppetmaster']['modulepath'] + '/' + environment
            _git_pull(update_target)
            for project in args.projects:
                update_target += '/' + project
                _git_pull(update_target)
    
    finally:
        ssh.close()