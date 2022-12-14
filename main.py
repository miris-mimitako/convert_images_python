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
    elif self.settings["to_convert_type"] == "png":
      self.to_png()
    elif self.settings["to_convert_type"] == "bmp":
      self.to_bmp()
    elif self.settings["to_convert_type"] == "tif" or self.settings["to_convert_type"] == "tiff":
      self.to_tiff()
    elif self.settings["to_convert_type"] == "webp":
      self.to_webp()
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
            img_path = file_path[:-4] + "_converted" + ".jpg"
          img.save(img_path, quality=self.settings["quality"])
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1

        elif ".jpeg" in file_path:
          print ("test: ", file_path) ##d
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-5] + "_converted" + ".jpg"
          img.save(img_path, quality=self.settings["quality"])
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1

        elif ".png" in file_path:
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-4] + "_converted" + ".jpg"
          rgb_img = img.convert("RGB")
          rgb_img.save(img_path, quality=self.settings["quality"])
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1

        elif ".tiff" in file_path:
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-5] + "_converted" + ".jpg"
          rgb_img = img.convert("RGB")
          rgb_img.save(img_path, quality=self.settings["quality"])
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1

        elif ".tif" in file_path:
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-4] + "_converted" + ".jpg"
          rgb_img = img.convert("RGB")
          rgb_img.save(img_path, quality=self.settings["quality"])
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1

        elif ".bmp" in file_path:
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".jpg"
          else:
            img_path = file_path[:-4] + "_converted" + ".jpg"
          rgb_img = img.convert("RGB")
          rgb_img.save(img_path, quality=self.settings["quality"])
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1

        ##E if
      ##E for
    ##E for
  ##E def to_jpg

  def to_png(self):
    for dir_path in self.path_list:
      dir_target_path = glob.glob(os.path.join(dir_path,"*"))
      print (dir_target_path) ##d
      for file_path in dir_target_path:
        if ".jpg" in file_path or ".jpeg" in file_path or ".tif" in file_path or ".tiff" in file_path or "bmp" in file_path: # version 0.1.1
          print ("test: ", file_path) ##d
          if ".jpeg" in file_path:
            file_path = file_path[:-5] + ".jpg"
          if ".tiff" in file_path:
            file_path = file_path[:-5] + ".tif"
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".png"
          else:
            img_path = file_path[:-4] + "_converted" + ".png"
          img.save(img_path)
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1
        ##E if
      ##E for
    ##E for
  ##E def to_png

  def to_tiff(self):
    for dir_path in self.path_list:
      dir_target_path = glob.glob(os.path.join(dir_path,"*"))
      print (dir_target_path) ##d
      for file_path in dir_target_path:
        if ".jpg" in file_path or ".jpeg" in file_path or ".png" in file_path or "bmp" in file_path in file_path: # version 0.1.1
          print ("test: ", file_path) ##d
          if ".jpeg" in file_path:
            file_path = file_path[:-5] + ".jpg"
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".tiff"
          else:
            img_path = file_path[:-4] + "_converted" + ".tiff"
          img.save(img_path)
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1

        ##E if
      ##E for
    ##E for
  ##E def to_tiff

  def to_bmp(self):
    for dir_path in self.path_list:
      dir_target_path = glob.glob(os.path.join(dir_path,"*"))
      print (dir_target_path) ##d
      for file_path in dir_target_path:
        if ".jpg" in file_path or ".jpeg" in file_path or ".png" in file_path or ".tif" in file_path or ".tiff" in file_path: # version 0.1.1
          print ("test: ", file_path) ##d
          if ".jpeg" in file_path:
            file_path = file_path[:-5] + ".jpg"
          if ".tiff" in file_path:
            file_path = file_path[:-5] + ".tif"
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".bmp"
          else:
            img_path = file_path[:-4] + "_converted" + ".bmp"
          img.save(img_path)
          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1
        ##E if
      ##E for
    ##E for
  ##E def to_tiff

  def to_webp(self):
    for dir_path in self.path_list:
      dir_target_path = glob.glob(os.path.join(dir_path,"*"))
      print ("webp: ", dir_target_path) ##d
      for file_path in dir_target_path:
        if ".jpg" in file_path or ".jpeg" in file_path or ".png"  in file_path or ".tif" in file_path or ".tiff"  in file_path or ".bmp" in file_path: # version 0.1.1
          print ("test: ", file_path) ##d
          if ".jpeg" in file_path:
            file_path = file_path[:-5] + ".jpg"
          if ".tiff" in file_path:
            file_path = file_path[:-5] + ".tif"
          img = Image.open(file_path)
          if self.converted_path:
            file_name = file_path[file_path.rfind("\\"):file_path.rfind(".")]
            img_path = self.converted_path + file_name + ".webp"
          else:
            img_path = file_path[:-4] + "_converted" + ".webp"
          img.save(img_path)
          print ("webp converted: ", img_path) ##d

          if self.settings["delete_file"]:os.remove(file_path) # version 0.1.1
        ##E if
      ##E for
    ##E for
  ##E def to_webp


  def __del__(self):
    pass

if __name__=="__main__":
  con = CONVERTER()
  con.convert()

