from argparse import ArgumentParser
from configobj import ConfigObj


parser = ArgumentParser()
parser.add_argument('-e', '--environments', nargs='+', help='Apply puppet updates to these environments')
parser.add_argument('-p', '--projects', nargs='+', help='Apply puppet updates to these projects')
parser.add_argument('-m', '--manifests', action='store_true', default=False, help='Apply updates to the puppet manifests directory')
parser.add_argument('-f', '--config', default='tugboat.cfg', help='Use configuration file specified instead')
parser.add_argument('-d', '--delay', default=5, type=int, help='Specify delay s seconds between updates to each host')


args = parser.parse_args()
config = ConfigObj(args.config)
