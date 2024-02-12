from PIL import Image, ImageDraw
import pandas as pd

# 假设您的xy轴坐标和压力数据分别存储在以下三个列表中
x_coords = [10, 20, 30, 40, 50]  # x轴坐标
y_coords = [100, 200, 150, 300, 250]  # y轴坐标
pressure_data = [0.5, 0.8, 0.6, 0.9, 0.0]  # 压力数据



data = pd.read_csv(r'AML_IntelligentCoders/signature_xizhi/False_4.csv',sep=',',header='infer',usecols=[1,2,3])


x_coords=data.values[0::,0]
y_coords=data.values[0::,1]
pressure=data.values[0::,2]



# Create a white background for image
img = Image.new('RGB', (240, 320), color='white')
draw = ImageDraw.Draw(img)

# Draw data points on image, with pressure as data
for x, y, p in zip(x_coords, y_coords, pressure):
    print(p)
    if p > 0:  # 只绘制压力大于0的点
        color = (int(p * 255), 0, 0)  # 根据压力值生成颜色
        draw.point((x, y), fill=color)



# 保存图像
img = img.rotate(90)            
img.save('False4.png')
img.show()


