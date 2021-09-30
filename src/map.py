import json
from image import Image
from pprint import PrettyPrinter
from pygame import Surface

class Map:

    def __init__(self, name: str):
        self.name = name
        with open(f'maps/{self.name}.json') as json_file:
            self.map_data = json.load(json_file)
        self.map_tile_width = self.map_data['tilewidth']
        self.map_tile_height = self.map_data['tileheight']
        self.tileset_names = []
        self.tileset_data = {}
        for tileset in self.map_data['tilesets']:
            self.tileset_names.append(tileset['source'].split('.tsx')[0].split('/')[-1])
        
        for tileset_name in self.tileset_names:
            with open(f'assets/tilesets/{tileset_name}/{tileset_name}.json') as json_file:
                self.tileset_data[tileset_name] = json.load(json_file)
        PrettyPrinter(indent=4).pprint(self.tileset_data)

        self.layer_surfaces = [Surface((layer['width'] * self.map_tile_width, layer['height'] * self.map_tile_height)) for layer in self.map_data['layers']]
        self.render()

    def render(self):
        for layer_surface in self.layer_surfaces:
            for layer in self.map_data['layers']:
                layer_data = layer['data']
                layer_width = layer['width']
                layer_height = layer['height']
                tile_x = 0
                tile_y = 0
                for tile_id in layer_data:
                    for tileset in self.tileset_data:
                        tiles = self.tileset_data[tileset]['tiles']
                        for tile in tiles:
                            tileset_tile_id = tile['id']
                            if tile_id == tileset_tile_id:
                                tile_image_width = tile['imagewidth']
                                tile_image_height = tile['imageheight']
                                tile_image_file_name = tile['image'].split('/')[-1]
                                tile_image = Image(f'assets/tilesets/{tileset}/{tile_image_file_name}', tile_image_width, tile_image_height).image
                                tile_image_rect = tile_image.get_rect()
                                tile_image_rect.center = (tile_x * tile_image_width, tile_y * tile_image_height)
                                layer_surface.blit(tile_image, tile_image_rect.center)
                    tile_x += 1
                    if tile_x > layer_width:
                        tile_x = 0
                        tile_y += 1

    def draw(self, screen, player):
        for layer_surface in self.layer_surfaces:
            layer_surface_rect = layer_surface.get_rect()
            layer_surface_rect.center = (player.x, player.y)
            screen.blit(layer_surface, layer_surface_rect)
