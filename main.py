import json
from PIL import Image
import glob
import os
import re

class CONVERTER():

  """
  ## settings params
  
  ### target_dir: 
  
  You should specified null or path.

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
    if not self.settings["target_dir"]:
      self.settings["target_dir"] = "."

    # set global target dir setting
    if os.path.isabs(self.settings["target_dir"]):
      target_path = self.settings["target_dir"]
    else:
      target_path = os.path.abspath(self.settings["target_dir"])

    if not os.path.exists(target_path):
      raise Exception("Error: Tareget directry does not exist.")
  
  
    # set converted files dire settings
    if self.settings["converted_files_dir"]:
        os.makedirs(self.settings["converted_files_dir"], exist_ok=True)      

    self.path_list = glob.glob(target_path)

  ##E def __init__

  def convert(self):
    print(self.settings["to_convert_type"])
    if ("jpg" or ".jpg" or "jpeg" or ".jpeg") in self.settings["to_convert_type"]:
      self.settings["to_convert_type"] = "jpg"
      print(self.settings["to_convert_type"]) ##d

    if self.settings["to_convert_type"] == ".jpg":
      self.to_jpg()

    ##E if

  ##E def convert
  
  def to_jpg(self):
    


    print("to_jpg")

  ##E def
  def __del__(self):
    pass

if __name__=="__main__":
  con = CONVERTER()
  con.convert()


