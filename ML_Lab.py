import glob
import torch
from torch.utils import data
from PIL import Image
import numpy as np
from torchvision import transforms
import matplotlib.pyplot as plt


class Mydatasetpro(data.Dataset):
# 类初始化
    def __init__(self, img_paths = None, labels = None, transform = None):
        self.imgs = img_paths
        self.labels = labels
        self.transforms = transform
# 进行切片
    def __getitem__(self, index):                #根据给出的索引进行切片，并对其进行数据处理转换成Tensor，返回成Tensor
        img = self.imgs[index]
        label = self.labels[index]
        pil_img = Image.open(img)                 #pip install pillow
        data = self.transforms(pil_img)
        return data, label
# 返回长度
    def __len__(self):
        return len(self.imgs)



def load_data(path = None):
    """
    This function load input data from 
    """
    if path is None:
        print("No path given")
        return

    #使用glob方法来获取数据图片的所有路径
    all_imgs_path = glob.glob(r'/home/lyc/doc/AML_LAB/dataset(png)/*/*.png')#数据文件夹路径，根据实际情况更改！
    
    # #循环遍历输出列表中的每个元素，显示出每个图片的路径
    # for var in all_imgs_path:
    #     print("Image loaded:", var)
    
    ### Prepare label 
    all_labels = []
    #对所有图片路径进行迭代
    for path_name in all_imgs_path:
        if "false" in path_name:
            all_labels.append(0)
        elif "true" in path_name:
            all_labels.append(1)

    signature_dataset = Mydatasetpro(all_imgs_path, label = all_labels)
    print("A total of ", len(signature_dataset), "loaded.") #返回文件夹中图片总个数

def process_data():



    


def main():
    









if __name__ == "__main__":
    main()
