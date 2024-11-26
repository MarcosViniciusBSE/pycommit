import fire
from model.patternCreator import PatternCreator
from model.pattern import Pattern
from model.executer import Executer

class Cli:
    def add_pattern(self, pattern, name):
        pn = PatternCreator(pattern, name)
        response = pn.create_pattern()
        if response:
            print(f"Pattern {name} criada com sucesso")
        else: raise Exception("Ocorreu um erro")

    def commit(self, name):
        pattern : Pattern = PatternCreator.load_pattern(self,name)
        command = self.create_commit_command(pattern)
        print(command)
        Executer.execute(self, command)

    def create_commit_command(self, pattern : Pattern):
        commit_command = "git commit -m " + f"\"{pattern.pattern}\""
        print(f"Commit for {pattern.name} pattern")
        for item in pattern.attributes:
            valor = input(f"{item} : ")
            commit_command = commit_command.replace(f"{{{item}}}", valor)
        return commit_command

if __name__ == '__main__':
    fire.Fire(Cli)
