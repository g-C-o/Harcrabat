"""
GUI.py
NewScript
Contains the code for generating a graphical version of the game
"""

class GUI:
  """
  Graphical interface class.
  Initially written by Dallin Guisti
  Manages the rendering of textures to the screen
  """
  def __init__(self):
    self.texture_location = "\Textures\"
    
    biome_name = "null"
    biome_full = true
    if biome_full: suffix = "Full.png"
    else: suffix = "Empty.png"
    texture_file = texture_location + biome_name + suffix
