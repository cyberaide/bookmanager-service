from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class BookmanagerserviceCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_bookmanagerservice(self, args, arguments):
        """
        ::

          Usage:
                bookmanagerservice start
                bookmanagerservice stop
                bookmanagerservice status

          This command manages the bookmanager service.


          Options:
              -h      help

        """
        VERBOSE(arguments)

        m = Manager()

        if arguments.start:
            print("Starts the service")
            raise NotImplementedError

        elif arguments.stop:
            print("Stops the service")
            raise NotImplementedError

        elif arguments.status:
            print("Status of the service")
            raise NotImplementedError

        return ""
