import json
from pprint import PrettyPrinter

class Map:

    def __init__(self, name: str):
        self.name = name
        with open(f'maps/{self.name}.json') as json_file:
            self.map_data = json.load(json_file)
        self.tileset_names = []
        self.tileset_data = {}
        for tileset in self.map_data['tilesets']:
            self.tileset_names.append(tileset['source'].split('.tsx')[0].split('/')[-1])
        
        for tileset_name in self.tileset_names:
            with open(f'assets/tilesets/{tileset_name}/{tileset_name}.json') as json_file:
                self.tileset_data[tileset_name] = json.load(json_file)
        PrettyPrinter(indent=4).pprint(self.tileset_data) 

        for tileset in self.tileset_data:
             pass

    def draw(self, screen):
        for tileset in self.tileset_data:
             pass
             # print(tileset)
        # for map_layer in self.map_data['layers']:
        #     print(map_layer)