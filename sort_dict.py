import os

def sort(dir_path):
    img_path = os.listdir(dir_path)
    d = {}
    sorted_frames = []
    for i in range(len(img_path)):
        key  = img_path[i][5:8]
        if ".j" in key:
            key = img_path[i][5]
        if "." in key:
            key = img_path[i][5:7]
        key = int(key)
        d[key] = img_path[i]

    sorted_d = sorted(d.items(),key=lambda x:(x[0],x[1]))

    for e in sorted_d:
        sorted_frames.append(dir_path+"/"+e[1])

    return sorted_d , sorted_frames