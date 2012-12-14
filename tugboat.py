import updaters.agentupdater
import updaters.puppetupdater

if __name__ == "__main__":
    puppetupdater = PuppetUpdater()
    puppetupdater.update()
    
    agentupdater = AgentUpdater()
    agentupdater.update()