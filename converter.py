import os

class Converter:
    def __init__(self,targets):
        self.targets = targets

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

        for target in self.targets:
            self.convert(target)
    
    def setTargets(self,targets):
        self.targets = targets
    
    def getTargets(self):
        return self.targets