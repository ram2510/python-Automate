import os
path ='C:/Users/ram2510/Desktop/python/automation/motivational-quotes'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.png'))
    i = i+1
