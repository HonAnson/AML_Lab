import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

csv_df_true = pd.read_csv('C:/Users/steven/Desktop/AML/Lab/data_base/signature_che/False_10.csv')
csv_df_false = pd.read_csv('C:/Users/steven/Desktop/AML/Lab/data_base/signature_yichen/False_3.csv')

pressure_distribution_true = pd.DataFrame(0, index=range(240), columns=range(320))
pressure_distribution_false = pd.DataFrame(0, index=range(240), columns=range(320))
accelx_distribution = pd.DataFrame(0, index=range(240), columns=range(320))
accely_distribution = pd.DataFrame(0, index=range(1000), columns=range(1000))
accelz_distribution = pd.DataFrame(0, index=range(1000), columns=range(1000))
gyrox_distribution = pd.DataFrame(0, index=range(1000), columns=range(1000))
gyroy_distribution = pd.DataFrame(0, index=range(1000), columns=range(1000))
gyroz_distribution = pd.DataFrame(0, index=range(1000), columns=range(1000))


x_coord = csv_df_true.y
y_coord = csv_df_true.x

centralized_true_x = x_coord - (sum(x_coord)/len(x_coord))
centralized_true_y = x_coord - (sum(y_coord)/len(y_coord))

print(csv_df_true.accel_x)
for index in range(len(csv_df_true.pressure)):
    if csv_df_true.pressure[index] != 0:
        pressure_distribution_true[x_coord[index]][250-y_coord[index]] = csv_df_true.pressure[index]
        # accelx_distribution[csv_df.x[index]][csv_df.y[index]] = csv_df.accel_x[index]
        #accely_distribution[csv_df.x[index]][csv_df.y[index]] = csv_df.accel_y[index]
        #accelz_distribution[csv_df.x[index]][csv_df.y[index]] = csv_df.accel_z[index]
        #gyrox_distribution[csv_df.x[index]][csv_df.y[index]] = csv_df.gyro_x[index]
        #gyroy_distribution[csv_df.x[index]][csv_df.y[index]] = csv_df.gyro_y[index]
        #gyroz_distribution[csv_df.x[index]][csv_df.y[index]] = csv_df.gyro_z[index]

for index in range(len(csv_df_false.pressure)):
    if csv_df_false.pressure[index] != 0:
        pressure_distribution_false[csv_df_false.y[index]][250-csv_df_false.x[index]] = csv_df_false.pressure[index]

plt.figure()
sns.heatmap(pressure_distribution_true)
plt.figure()
sns.heatmap(pressure_distribution_false)
plt.show()