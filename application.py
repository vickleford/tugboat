import logging

from config import config, args
from updaters.agentupdater import AgentUpdater
from updaters.puppetupdater import PuppetUpdater


if __name__ == "__main__":
    log = logging.getLogger(__name__)
    logging.basicConfig(filename='tugboat.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    log.info('Started tugboat')
    
    puppetupdater = PuppetUpdater(args.environments, args.projects)
    puppetupdater.update(args.environments)
    
    agentupdater = AgentUpdater()
    agentupdater.update()
    
    log.info('Finished')
