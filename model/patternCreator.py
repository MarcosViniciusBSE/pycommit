import re
import json
import os
from model.pattern import Pattern

class PatternCreator:
    def __init__(self, pattern, name):
        self.pattern = pattern
        self.name = name
    
    def create_pattern(self) -> bool:
        atributes = self.get_atributes()
        data = {
            "pattern": self.pattern,
            "name": self.name,
            "atributes": atributes,
        }
        # Criando o diretório se não existir
        os.makedirs("./patterns", exist_ok=True)

        # Salvando os dados no arquivo JSON
        with open(f"./patterns/{self.name}.json", "w") as file:
            json.dump(data, file, indent=4)
        
        # Verificando se o arquivo foi criado corretamente
        if os.path.exists(f"./patterns/{self.name}.json"):
            print(os.path.realpath(f"./patterns/{self.name}.json"))
            return True
        return False

    def get_atributes(self) -> list:
        regex = r'\{([^{}]+)\}|\(([^()]+)\)|\[(.*?)\]'        
        matches = re.findall(regex, self.pattern)
        values = []
        for grupo in matches:
            for item in grupo:
                if item:
                    clean_item = item.strip("{}()[]")
                    values.append(clean_item)
            
        return values
    
    def load_pattern(self, name):
        with open(f"./patterns/{name}.json", 'r') as file:
            data = json.load(file)
            pattern = Pattern(data['pattern'], data['name'], data['atributes'])
            return pattern