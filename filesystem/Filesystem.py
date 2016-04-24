import os
from Options import Options


class Filesystem:

    @staticmethod
    def file_exists(filepath, filename):
        """ Check the requested filename if exists in this specified path
	        Return True on success or False on fail
        """
        filename = filename.replace("/", "")
        if os.path.exists(Options.root_dir + filepath):
            files = os.listdir(Options.root_dir + filepath)
        else:
            return False

        for sysfile in files:
            if sysfile == filename:
                return True
        return False

