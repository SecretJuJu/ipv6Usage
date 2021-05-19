import os

class Converter:
    def __init__(self,targets=None):
        if targets is None:
            self.convertPossible = False
        else :
            self.targets = targets
            self.convertPossible = True

    def convert(self,target):
        command = "python3 ./html2csv/html2csv/__main__.py \"{}\" -o \"{}\"".format(
            target["input"],
            target["output"]
        )
        os.system(command)
        print("command : {}".format(command))
        print(target["output"])
        return True
    
    def convert_targets(self):
        if self.convertPossible:
            for target in self.targets:
                self.convert(target)
            return True
        print("cannot convert\n-> you must set the targets")
        return False
    
    def setTargets(self,targets):
        self.targets = targets
        self.convertPossible = True
    
    def getTargets(self):
        return self.targets