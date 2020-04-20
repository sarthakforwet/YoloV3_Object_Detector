import os
import sort_dict
import argparse

# CLI arguments.
parser = argparse.ArgumentParser(description="Execution program for yolo.py")
parser.add_argument("--dir_path")
parser.add_argument("--labels",default="Data_for_colab/obj.names")
parser.add_argument("--image")
parser.add_argument("--weights",default="Data_for_colab/yolov3-tiny-obj_4000.weights")
parser.add_argument("--configs",default="Data_for_colab/yolov3-tiny-obj.cfg")

args = vars(parser.parse_args())

if args["dir_path"] and args["image"]:
    raise ValueError("Directory path and image cannot be given simultaneously.")

if args["dir_path"]:
    if args["dir_path"][-1] == "/":
        args["dir_path"] = args["dir_path"][:-1]

    sorted_img_dict,frames = sort_dict.sort(args["dir_path"])

    '''
        Note that your directory must have following structure - dirname/framex.jpg where len(x) can be 1 or 2 or 3 after that you have to
        tweak some code in sort_dict.py .
        Examples of structure ->
            - test/frame0.jpg
            - dirname/frame32.jpg
    '''

    for frame in frames:
        image_path = frame
        try:
            os.system("python yolo.py --image {} --weights {} --configs {} --labels {}".format(image_path,args["weights"],args["configs"],args["labels"]))
        except Exception as e:
            print(e)

if args["image"]:
    os.system("python yolo.py --image {} --weights {} --configs {} --labels {}".format(args["image"],args["weights"],args["configs"],args["labels"]))

else:
    raise ValueError("Please Specify either Image or Directory!")