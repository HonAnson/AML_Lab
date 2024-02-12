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
    
    ### Prepare label 
    all_labels = []
    # Create label base on path name
    for path_name in all_imgs_path:
        if "false" in path_name:
            all_labels.append(0)
        elif "true" in path_name:
            all_labels.append(1)

    signature_dataset = Mydatasetpro(all_imgs_path, label = all_labels)
    


    data.DataLoader(
                            signature_dataset,
                            batch_size=10,
                            shuffle=True
    )
    return 

def process_data():

    return




def main():
    
    return








if __name__ == "__main__":
    main()
