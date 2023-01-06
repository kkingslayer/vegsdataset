import os
import shutil

os.system("git clone https://github.com/ultralytics/yolov5")

os.chdir("yolov5/")
os.system("pip install -r requirements.txt")

shutil.rmtree("vegsdataset")
os.system("git clone https://github.com/kkingslayer/vegsdataset")

#os.system("python3 train.py --epochs 1 --data inf.yaml --weights yolov5s.pt")

