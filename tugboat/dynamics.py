"""dynamics

Because the command line args can specify an alternate config file, I kind of
ran into a catch-22 between loading the args before config and vice-versa.
Didn't want to pass around an entire config dict to all my classes to fix.

"""


from argparse import ArgumentParser
from configobj import ConfigObj


def _get_arguments():
    """Build and parse command-line arguments."""
    
    parser = ArgumentParser()
    
    parser.add_argument('-e', '--environments', nargs='+', help='Apply puppet updates to these environments')
    parser.add_argument('-p', '--projects', nargs='+', help='Apply puppet updates to these projects')
    parser.add_argument('-m', '--manifests', action='store_true', default=False, help='Apply updates to the puppet manifests directory')
    parser.add_argument('-f', '--config', default='tugboat/config.ini', help='Use configuration file specified instead')
    parser.add_argument('-d', '--delay', default=5, type=int, help='Specify delay s seconds between updates to each host')
    parser.add_argument('-s', '--deploy-suite', help='Specify a file containing a suite of commands to run during deploy')

    return parser.parse_args()
        
def _get_config(cmd_line_args):
    """Load configuration file from command-line args or default tugboat.cfg."""
    
    config = ConfigObj(cmd_line_args.config)
    
    # maybe use ConfigObjError later?
    # http://www.voidspace.org.uk/python/articles/configobj.shtml
    if config == {}:
        raise Exception("Empty configuration file or could not find {it}".format(it=cmd_line_args.config))
    else:
        return config


args = _get_arguments()
config = _get_config(args)
