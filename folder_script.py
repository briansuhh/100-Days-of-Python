import os

for i in range(15, 101):
    directory_name = f"Day {i}"
    
    if os.path.exists(directory_name):
        os.rmdir(directory_name)  
        
    os.mkdir(directory_name) 
    os.chdir(directory_name)
    os.system("touch main.py")
    os.chdir("..")