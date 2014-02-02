import os,time,json

def get_files(directory):
    file_list = []
    for name in os.listdir(directory):
        file_stat = os.stat(os.path.join(directory,name))
        #file_list.append({"name":name,"modifiedTime":time.ctime(a.st_mtime)})
        file_list.append({"name":name,"modifiedTime":file_stat.st_mtime})
    return file_list

file_list = get_files("/var/www/motion/*.jpg")
sorted_file_list = sorted(file_list, key=lambda k: k['modifiedTime'],reverse=True) 

formatted_file_list = []
for file in sorted_file_list:
    formatted_file_list.append({"name":file["name"],"modifiedTime":time.ctime(file["modifiedTime"])})
    
print json.dumps(formatted_file_list)