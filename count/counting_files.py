import os

root_dir = "D:/"

count = 0
for (root, dirs, files) in os.walk(root_dir):

    if len(files) > 0:
        for file_name in files:
            if(len(file_name) > 20) : 
                count += 1
            if count % 10000 == 0 :
                print(count)
                
print(count)