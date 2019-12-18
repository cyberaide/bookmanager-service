from __future__ import print_function

from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command

"""
host = "127.0.0.1"
host = "0.0.0.0"
port = "5000"
path = /opt/project
path = .

volume = "host" if left out or host just do loacl
volume = "local" if true do volume 


def bmservice():
    p = str(Path('.').absolute())
    strt = f'docker run --rm -it -p {host}:{port}:{port}/tcp -w {path}/bookmanager-service '
    envs = '-e "FLASK_APP={path}/cloudmesh/bookmanagerservice/service/app.py" -e "FLASK_ENV=development" ' # ????
    vol = '-v ' + str(
        Path(
            '.').absolute()) + ':/opt/project/bookmanager-service bigdata:v1 '
    pcmd = f'python -u -m flask run --host {host}'
    final = strt + envs + vol + pcmd
    print(final)
    subprocess.run(final, shell=True)   # repace this with detached ? or use Shell.execute ?

#if __name__ is "__main__":
#    bmservice()
"""

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

        import subprocess
        from pathlib import Path

        #
        # sshoudl that not be integrated into
        #
        # bbookmanagerserice.command.bookmanagerservice.
        # than we can use cms bookmanagerservice ....?
        #


        if arguments.start:
            print("Starts the service")
            raise NotImplementedError

        elif arguments.stop:
            print("Stops the service")
            raise NotImplementedError

            "get cloudmesh.common.Shell    shell.ps shell.ps byname find and kill"

        elif arguments.status:
            print("Status of the service")
            raise NotImplementedError

            " just show waht ps gives us cloudmesh for t"

        return ""
