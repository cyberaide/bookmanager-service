from __future__ import print_function

import os
import subprocess
from pathlib import Path

from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command

# host = "0.0.0.0"

host = "127.0.0.1"
port = "5000"
path = "."
image = "bookmanager-service:4.1.3"

#volume = "host" if left out or host just do loacl
#volume = "local" if true do volume



class BookmanagerserviceCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_bookmanagerservice(self, args, arguments):
        """
        ::

          Usage:
                bookmanagerservice [-v] start [--dryrun]
                bookmanagerservice stop
                bookmanagerservice status
                bookmanagerservice create image
                bookmanagerservice shell
                bookmanagerservice [-v] local [--dryrun]

          This command manages the bookmanager service.

          Options:
              -h      help

        """
        VERBOSE(arguments)


        #
        # sshoudl that not be integrated into
        #
        # bbookmanagerserice.command.bookmanagerservice.
        # than we can use cms bookmanagerservice ....?
        #


        if arguments.start:

            print("Starts the service")

            p = str(Path('.').absolute())
            strt = f'docker run --rm -it -p {host}:{port}:{port}/tcp '
            workdir =  f'-w /opt/project/bookmanager-service/bookmanager-service '
            envs = f'-e "FLASK_APP={path}/cloudmesh/bookmanagerservice/service/app.py" -e "FLASK_ENV=development"'
            host_path = str(Path('.').absolute())
            vol = f'{host_path}:/opt/project/bookmanager-service {image} '
            pcmd = f'python -u -m flask run --host {host}'
            command = f"{strt} {workdir} {envs} -v {vol} {pcmd}"

            if arguments["-v"] or arguments["--dryrun"]:
                print(command)
            if not arguments["--dryrun"]:
                subprocess.run(command, shell=True)


            # repace this with detached ? or use Shell.execute ?

            return ""

        elif arguments.stop:
            print("Stops the service")
            raise NotImplementedError

            "get cloudmesh.common.Shell    shell.ps shell.ps byname find and kill"

        elif arguments.status:
            print("Status of the service")
            raise NotImplementedError

            " just show waht ps gives us cloudmesh for t"

        elif arguments.create and arguments.image:
            # schould use subprocess ;-)
            #
            # creat subdir with Dockerfile in it and than run this command in that dir
            #
            os.system (f"docker build -t {image} .")

        elif arguments.local:

            print("Starts the service")

            p = str(Path('.').absolute())
            envs = f'FLASK_APP={path}/cloudmesh/bookmanagerservice/service/app.py FLASK_ENV=development'
            pcmd = f'python -u -m flask run --host {host}'
            command = f" {envs} {pcmd}"

            if arguments["-v"] or arguments["--dryrun"]:
                print(command)
            if not arguments["--dryrun"]:
                subprocess.run(command, shell=True)


        return ""
