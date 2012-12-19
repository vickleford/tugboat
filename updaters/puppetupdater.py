"""puppetupdater

Logs into the puppetmaster specified in tugboat.cfg
Makes sure we're on the given branch (default master)
Issues a git pull

Assumes user has NOPASSWD sudo to:
- git checkout branchname
- git pull

TODO: 
- add better error handling around the command executions
- get environments and projects names by args instead of 
    directly inspecting config and args?

"""


import paramiko
import logging

from updater import RemotePuppetUpdater
from config import config


log = logging.getLogger(__name__)


class PuppetUpdater(RemotePuppetUpdater):
    
    def __init__(self, environments, projects = []):
        super(PuppetUpdater, self).__init__(environments)
        
        self.log = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)
            
    def _git_pull(self, directory, branch='master'):
        """Pull the latest from a git repository."""
    
        cd = "cd " + directory + ';'
        go_to_branch = "sudo git checkout " + branch + ';'
        pull = "sudo git pull"+ ';'
        
        stdin, stdout, stderr = self.ssh.exec_command(cd + go_to_branch + pull)
        self._log_command_output(stdout, stderr)
    
    def update(self):
        """Update each environment specified and each project specified in each environment."""
        
        host = config['puppetmaster']['server']
        user = config['puppetmaster']['user']
        key = config['puppetmaster']['key']
        
        try:
            self._shell_in(host, user, key)

            if args.manifests:
                # Update site manifests if asked to
                self.log.info("Updating site manifests on {pmaster}".format(pmaster = host))
                self._git_pull(config['puppetmaster']['manifests'])
    
            # expect multiple projects in multiple envs or just one env
            for environment in self.environments:
                update_target = config['puppetmaster']['modulepath'] + '/' + environment
                self.log.info("Updating environment in {env}".format(env=update_target))
                self._git_pull(update_target)
                for project in self.projects:
                    update_target += '/' + project
                    self.log.info("Updating project in {proj}".format(proj=update_target))
                    self._git_pull(update_target)
    
        finally:
            self.ssh.close()