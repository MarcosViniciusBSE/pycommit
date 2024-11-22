import subprocess
class Executer:
    def execute(self, command):     
        resultado = subprocess.run(command, shell=True, text=True, capture_output=True)
        print("Saída do comando:", resultado.stdout)