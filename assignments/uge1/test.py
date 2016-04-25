import os
import sys

class test:
    def name(self):
        return "test1"

    def show_in_menu(self):
        code = """<button class="btn btn-primary active custom" type="submit"z> Test </button> """

        return code


if __name__ == "__main__":
    t = test()
    print(t.show_in_menu())
