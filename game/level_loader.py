import os
import pytmx

# Using https://pytmx.readthedocs.io/en/latest/
# TODO: Need to make dynamic eventually for supporting multiple levels
current_level = 'level_1.tmx'
level_data = pytmx.TiledMap(os.path.join('assets', 'levels', current_level))

# Iterate through Tiled layers
for layer in level_data.layers:
    print(layer)
