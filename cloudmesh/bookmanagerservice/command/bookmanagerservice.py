from __future__ import print_function

from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command


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
