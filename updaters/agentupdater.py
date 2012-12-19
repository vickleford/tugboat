"""agentupdater

Logs into the puppet agents specified in tugboat.cfg
    for each environment specified
Issues a puppetd -t

Assumes user has NOPASSWD sudo to:
- puppetd -t

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


class AgentUpdater(RemotePuppetUpdater):
    
    def __init__(self, environments):
        super(AgentUpdater, self).__init__(environments)
        self.servers = []
    
    def _puppetd_t(self):
        """Invoke puppetd -t on the puppet agent."""
        
        # this should be configurable instead
        puppetd_t = "sudo /usr/sbin/puppetd -t"
        
        stdin, stdout, stderr = self.ssh.exec_command(puppetd_t)
        self._log_command_output(stdout, stderr)
        
    def update(self):
        """Update each server in each environment with puppetd."""
        
        for environment in self.environments:
            user = config[environment]['user']
            key = config[environment]['key']
            hosts = config[environment]['hosts']
            
            # just in case there's only one
            hosts = list(hosts.split(','))
                        
            for host in hosts:
                log.info("Starting update on {node} in {env}".format(node=host, env=environment))
                try:
                    self._shell_in(host, user, key)
                    self._puppetd_t()
                finally:
                    self.ssh.close()
            
            
            
            
