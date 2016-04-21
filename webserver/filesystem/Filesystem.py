import os
from webserver.Options import Options


class Filesystem:

    @staticmethod
    def file_exists(filepath, filename):
        """ Check the requested filename if exists in this specified path
	    Return True on success or False on fail
        """
        filename = filename.replace("/", "")
        files = os.listdir(Options.root_dir + filepath)
	print(files)

        for sysfile in files:
            if sysfile == filename:
                return True
        return False

