import logging

import updaters.agentupdater
import updaters.puppetupdater

if __name__ == "__main__":
    logging.basicConfig(filename='tugboat.log', level=logging.INFO,
                        format='%(levelname)s:%(asctime)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started tugboat')
    puppetupdater = PuppetUpdater()
    puppetupdater.update()
    
    agentupdater = AgentUpdater()
    agentupdater.update()
    logging.info('Finished')
    