import os, os.path
import importlib
import sys
from Options import Options
class BbManager:
    html_code = []
    """
    def Validation(filepath)
        if os.path.exists(Options.root_blocks +filepath ):
            files = os.listdir(Options.root_blocks + filepath)
            return files
        else:
            # if the path does not exists then we return index.html file as front page
            return Options.root_dir + "/index.html"
    """
    def start(self, filepath):
        if os.path.exists(filepath):#Options.root_blocks + filepath):
            files = os.listdir(filepath)#Options.root_blocks + filepath)
            for sysfile in files:
                if sysfile.endswith(".py"):
                    path = os.path.join(filepath,sysfile)
                    print(path)
                    path = path.replace("/",".")[:-3]
                    #path = path[:-3]
#                    print("path: \n"+ path)
#                    foo = __import__(path)
#                    x = (eval("foo." + "uge1" + ".test"))
#                    print(x)
#                    print(x.test.show_in_menu())
                    #fl = sysfile
                    #foo = SourceFileLoader(str(fl), filepath+str(fl)).load_module()
                    #test = foo.test()
                    #print(test)
#                    done = test.show_in_menu()
                    #print(foo.show_in_menu())
#                    self.html_code.append(done)

#                    ps = filepath.split("/")
#                    sysfile = sysfile.replace(".py", "")
#                    path = ps[0]+"."+ps[1]+"."+sysfile
#                    print("FORLOOP\n"+ path)

#                    print("YEs WE CAN")
                    sy = importlib.import_module(path)
                    print(sy)
                    #print(sy.test.show_in_menu())
#                    print("DONE")
#                    print(sy.show_in_menu)
                    self.html_code.append(sy.test.show_in_menu())
                    print(self.html_code)

#        else:
#            print("ELSE")

if __name__ == '__main__':
    manager = BbManager()
    ls = manager.start("assignments/uge1/")
#    print("=============" + ls)
