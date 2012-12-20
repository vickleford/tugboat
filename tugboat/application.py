import logging

from dynamics import args, config
from updaters.agentupdater import AgentUpdater
from updaters.puppetupdater import PuppetUpdater


def run():
    """Start tugboat."""
        
    log = logging.getLogger(__name__)
    logging.basicConfig(filename='tugboat/tugboat.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
                        
    log.info('Started tugboat')

    puppetupdater = PuppetUpdater(args.environments, args.projects)
    puppetupdater.update()

    agentupdater = AgentUpdater(args.environments)
    agentupdater.update()

    log.info('Finished')
