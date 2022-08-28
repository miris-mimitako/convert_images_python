import json
from PIL import Image
import glob
import os


class CONVERTER():

  """
  ## settings params
  
  ### target_dir: 
  
  You should specified null or path.

  ### converted_files_dir: null
  
  converted image files put into same directry of tareget directory.
  
  ### converted_files_dir: specified
  
  Create new directory and put into converted images. If directory is existed, does not create directory.

  ### quality: 0 ~ 95

  Only jpg image, you can choose compression quality between 0 and 95.
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
    self.converted_path = ""
    if self.settings["converted_files_dir"]:
        os.makedirs(self.settings["converted_files_dir"], exist_ok=True)
        self.converted_path = os.path.abspath(self.settings["converted_files_dir"])

    # self.settings["serch_depth"] number 以外の除外規定

    print (target_path.count("\\")) ##d

    try:
      self.settings["serch_depth"] = int(self.settings["serch_depth"])
    except ValueError:
      raise Exception ("Type error: serch_depth of settings.json is not numeric type.")
    
    
    self.path_list = []

    if self.settings["serch_depth"] >= 0:
      depth_target = target_path.count("\\")
      for current_dir, sub_dirs, files_list in os.walk(target_path):
        if current_dir.count("\\") <= depth_target + self.settings["serch_depth"]:
          self.path_list.append(current_dir)
    elif self.settings["serch_depth"] < 0:
      for current_dir, sub_dirs, files_list in os.walk(target_path):
        self.path_list.append(current_dir)

    # self.path_list = glob.glob(os.path.join(target_path, path_depth)) # serach depth cannot use.
    print(self.path_list)

  ##E def __init__

  def convert(self):
    print(self.settings["to_convert_type"]) ##d
    if ("jpg" or ".jpg" or "jpeg" or ".jpeg") in self.settings["to_convert_type"]:
      self.settings["to_convert_type"] = "jpg"
      print(self.settings["to_convert_type"]) ##d

    if self.settings["to_convert_type"] == "jpg":
      self.to_jpg()
    else:
      raise Exception ("Type error: to_convert_type cannot read.")

    ##E if
  ##E def convert
  
  def to_jpg(self):
    print("to_jpg") ##d
    # convert any to jpg
    for dir_path in self.path_list:
      dir_target_path = glob.glob(os.path.join(dir_path,"*"))
      print (dir_target_path) ##d
      for file_path in dir_target_path:
        if ".jpg" in file_path:
          print ("test: ", file_path) ##d
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-5] + "_converted" + ".jpg"
          img.save(img_path, quality=self.settings["quality"])
        elif ".jpeg" in file_path:
          print ("test: ", file_path) ##d
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-5] + "_converted" + ".jpg"
          img.save(img_path, quality=self.settings["quality"])
        elif ".png" in file_path:
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-4] + "_converted" + ".jpg"
          rgb_img = img.convert("RGB")
          rgb_img.save(img_path, quality=self.settings["quality"])
        elif ".tiff" in file_path:
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-5] + "_converted" + ".jpg"
          rgb_img = img.convert("RGB")
          rgb_img.save(img_path, quality=self.settings["quality"])
        elif ".tif" in file_path:
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-4] + "_converted" + ".jpg"
          rgb_img = img.convert("RGB")
          rgb_img.save(img_path, quality=self.settings["quality"])
        elif ".bmp" in file_path:
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-4] + "_converted" + ".jpg"
          rgb_img = img.convert("RGB")
          rgb_img.save(img_path, quality=self.settings["quality"])
        ##E if
      ##E for
    ##E for
  ##E def to_jpg

  def __del__(self):
    pass

if __name__=="__main__":
  con = CONVERTER()
  con.convert()

