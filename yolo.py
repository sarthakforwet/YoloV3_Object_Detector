import numpy as np
import argparse
import cv2
import os
import time
import random

parser = argparse.ArgumentParser(description="This is Yolov3 Detection Camp")
parser.add_argument("--image",required=True)
parser.add_argument("--confidence",default=0.3)
parser.add_argument("--threshold",default=0.3)

parser.add_argument("--weights")
parser.add_argument("--configs")

parser.add_argument("--labels",required=True)

args = vars(parser.parse_args())


# Opening the output file
# If not needed comment lines 16,71,72,86,second and third part of line 74.
submission = open("submission.txt","a")

# Getting image.
image = cv2.imread(args["image"])
(H,W) = image.shape[:2]

# Change the path to you .names file.
labelspath = os.path.join(args["labels"])

Labels = open(labelspath).read().strip().split("\n")
Colors = np.random.randint(0,255,size=(len(Labels),3),dtype="uint8")

# Change the paths to your .cfg and .weights file.
weightsfile = os.path.join(args["weights"])
configfile  = os.path.join(args["configs"])

net = cv2.dnn.readNetFromDarknet(configfile,weightsfile)

ln = net.getLayerNames()
ln = [ln[i[0]-1] for i in net.getUnconnectedOutLayers()]

blob = cv2.dnn.blobFromImage(image,1/255.,(416,416),swapRB=True,crop=False)
net.setInput(blob)
start = time.time()
layeroutputs = net.forward(ln)
end = time.time()

print(f"Model took {round(end-start,4)} secs")

boxes = []
confidences = []
classids = []

for output in layeroutputs:
	for detection in output:
		scores = detection[5:]
		classid = np.argmax(scores)
		confidence = scores[classid]

		if confidence > args["confidence"]:
			box = detection[0:4]*np.array([W,H,W,H])
			(centerX,centerY,width,height) = box.astype("int")

			x = int(centerX-(width/2))
			y = int(centerY-(height/2))

			boxes.append([x,y,int(width),int(height)])
			confidences.append(float(confidence))
			classids.append(classid)

nms_idxs = cv2.dnn.NMSBoxes(boxes,confidences,args["confidence"],args["threshold"])

# Random index for Unkown Image or cam say when nothing in the prediction output.
color_idx = random.randrange(len(Colors))

if len(nms_idxs)>0:
	for i in nms_idxs.flatten():
		(x,y) = boxes[i][0] , boxes[i][1]
		(w,h) = boxes[i][2] , boxes[i][3]
		color = [int(c) for c in Colors[classids[i]]]
		cv2.putText(image,"{} : {:.2f}%".format(Labels[classids[i]],confidences[i]*100),(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,color,2)
		cv2.rectangle(image,(x,y),(x+w,y+h),color,2)
		submission.write("{} {} ".format(Labels[classids[i]],confidences[i]))
	submission.write("\n")
else:
    cv2.putText(image,"Unknown",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,[int(c) for c in Colors[color_idx]],2) , submission.write("Unknown") , submission.write("\n")

cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
submission.close()