import json
from PIL import Image
import pandas as pd

class CONVERTER():
  def __init__(self) -> None:
    # read settings
    json_open = open("settings.json")
    self.df_setting = pd.read_json("settings.json")
    
  def convert(self):
    pass

  def to_jpg(self):
    pass

  def __del__(self):
    pass

if __name__=="__main__":
  con = CONVERTER()
  con.convert()


