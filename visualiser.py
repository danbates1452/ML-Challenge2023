import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("./data/movementSensorData.csv")

print(df.keys())
x=df.loc[df['activity'] == 1, 'lw_x']
y=df.loc[df['activity'] == 4, 'lw_x']
plt.plot(x,label="Walking x-axis")
plt.plot(y,label="Driving x-axis")
plt.legend(loc="upper right")
plt.xlabel("Time step")
plt.ylabel("Value")
plt.show()

x=df.loc[df['activity'] == 1, 'lw_y']
y=df.loc[df['activity'] == 4, 'lw_y']
plt.plot(x,label="Walking y-axis")
plt.plot(y,label="Driving y-axis")
plt.legend(loc="upper right")
plt.xlabel("Time step")
plt.ylabel("Value")
plt.show()

x=df.loc[df['activity'] == 1, 'lw_z']
y=df.loc[df['activity'] == 4, 'lw_z']
plt.plot(x,label="Walking z-axis")
plt.plot(y,label="Driving z-axis")
plt.legend(loc="upper right")
plt.xlabel("Time step")
plt.ylabel("Value")
plt.show()

#import seaborn
#seaborn.set_style('darkgrid')

#plt.figure(figsize=(5,4))
#plot_axes = plt.axes(projection = '3d')
#walkingx = df.loc[df['activity'] == 1, 'lw_x']
#walkingy = df.loc[df['activity'] == 1, 'lw_y']
#walkingz = df.loc[df['activity'] == 1, 'lw_z']

#drivingx = df.loc[df['activity'] == 4, 'lw_x']
#drivingy = df.loc[df['activity'] == 4, 'lw_y']
#drivingz = df.loc[df['activity'] == 4, 'lw_z']

#plot_axes.scatter3D(walkingx, walkingy, walkingz)
#plot_axes.scatter3D(drivingx, drivingy, drivingz)

#plot_axes.set_xlabel('x')
#plot_axes.set_ylabel('y')
#plot_axes.set_zlabel('z')
#plt.show()