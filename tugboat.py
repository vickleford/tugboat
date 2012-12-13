import paramiko

from config import config
from config import args

#for git, mike says there's a python library called dulwich
# all of the git capatilities exposed pythonically 

def ssh_puppetmaster():
    """SSH into the puppetmaster to do your stuff."""
    
    pass
    
    
def git_pull(directory, branch='master'):
    """Pull the latest from a git repository."""
    
    pass

def pull_updates():
    """Update each environment specified and each project specified in each environment."""
    
    ssh_puppetmaster()
    
    if args.manifests:
        #cd to config['puppetmaster']['manifests']
        git_pull(config['puppetmaster']['manifests'])
        
    for environment in args.environments:
        git_pull(environment)
        for project in args.projects:
            git_pull(project)

