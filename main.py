import json
from PIL import Image
import glob
import os

class CONVERTER():

  """
  ## settings params
  
  ### target_dir: 
  
  You should specified null or full path.

  ### converted_files_dir: null
  
  converted image files put into same directry of tareget directory.
  
  ### converted_files_dir: specified
  
  Create new directory and put into converted images. If directory is existed, does not create directory.
  """

  def __init__(self) -> None:
    # read settings
    open_file = open("settings.json")
    self.settings = json.load(open_file)
    print (self.settings) ##d

    # tareget dir settings
    if self.settings["target_dir"]:
      pass
    else:
      self.settings["target_dir"] = "."

    # set global target dir setting
    if self.settings["target_dir"] == ".":
      self.target_dir = os.getcwd() # set current directry
      print (self.target_dir) ##d
    else:
      if os.path.exists(self.settings["target_dir"]):
        self.target_dir = self.settings["target_dir"]
      else:
        raise Exception("Error: Tareget directry does not exist.")

    # set converted files dire settings
  

  ##E def

  def convert(self):
    if self.settings["to_convert_type"] == "jpg" | ".jpg" | "jpeg" | ".jpeg":
      self.to_jpg()

    ##E if
  ##E def
  
  def to_jpg(self):
    print("to_jpg")

  ##E def
  def __del__(self):
    pass

if __name__=="__main__":
  con = CONVERTER()
  # con.convert()


