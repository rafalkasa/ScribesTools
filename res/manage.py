# coding=utf-8

"""
Frontend for managing tools.

TODO: This framework is in construction
Eventually it should support something like

    python manage.py download GitHub
    python manage.py install GitHub
    python manage.py check GitHub
    # python manage.py copyFromLocalST XXX


"""
import importlib
import argparse

from tools import ROOT_SOURCE_DIR, SCRIBETOOLS, PLATFORM


def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        help="install or check",
        type=str)
    parser.add_argument(
        "tool",
        help="name of the tool",
        type=str)
    arguments = parser.parse_args()
    return arguments

def displayContext():
    print('TODO: THIS FRAMEWORK IS IN CONSTRUCTION')
    print('Resource directory    : %s' % ROOT_SOURCE_DIR)
    print('SRIBETOOLS directory  : %s' % SCRIBETOOLS)
    print('Platform              : %s' % PLATFORM)

def processCommand(command, tool):
    try:
        tool_module = importlib.import_module(tool.lower())
    except ImportError:
        raise Exception('No tool named %s' % tool)
    if command == 'install':
        tool_module.Tool().install()
    elif command == 'check':
        tool_module.Tool().check()
    else:
        raise Exception('command is invalid')

args = parseArguments()
processCommand(args.command, args.tool)
