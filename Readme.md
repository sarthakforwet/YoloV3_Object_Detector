<b>About Repository:</b><br>
   - Basically this Repository is an attempt by me to make it easy for other developers to perform Object dection and Recognition.<br> 
	 
   - This Repository also provides users with weights and configuration files that I have generated for my particular task of 
        detecting the emotions of Tom and Jerry.
   
   - I am also providing images (`test_images`) to test this model without actually training it.<br> 
	 
   - This Repository has a mechanism for users to test it before they train it so that they can get insights of how the 
    flow of code going on.<br> 
	 
   - Note that the main Aim of this Model is combine at one place the training and testing of the model .<br>
   
   - Training of the model is not the motto of this Repo.<br>
	 
   - Refer to the links Given in <i>below section</i> to train the model.<br> 

<b><u>Custom Training:</u></b>
	
-	Obtain the dataset for the that you wanna detect.

-	For training the Model on Colab : Refer <a href="https://medium.com/@today.rafi/train-your-own-tiny-yolo-v3-on-google-colaboratory-with-the-custom-dataset-2e35db02bf8f">this</a>.
	
-	For training the Model on Local Machine either Linux , Windows or MacOS : Refer <a href="https://github.com/AlexeyAB/darknet">this</a>.
		
-	After training you should have a weights and configration file with you to proceed with the predictions.


<b>Testing:</b><br> 

- A folder should be present having files similar to obj.data , obj.names , yolov3-tiny-obj.cfg , yolov3-tiny-obj_4000.weights  as  present  under  Data_for_colab  folder.
  These files will be with you if you have training of the model.
  
-  run `yolorun.py` file . 
	
Information about `yolorun.py`
		
arguments :

- --image : path to the image file.<br>
		      
- --dir_path : path to the directory in which images are kept.
		      
- --weights : path to the .weights file generated from training.
		      
- --configs : path to the .cfg file.
		
- --labels :  path to the .names file.
		
    Remember that at a time only one of the argument either `--image` or `--dir_path` can be used else error will be thrown.
		
    Examples: 
    
- `python yolorun.py --image image.jpg` <br>
- `python yolorun.py --dir_path dirname`
	
  Note : `yolo.py` (called by yolorun.py) saves the output of the prediction by the model in a text file named `submission.txt` . If you want you can remove this
		functionality by following the instructions in `yolo.py` , line - 23     

<b>Conclusions:</b>
- This Repo is my best attempt to make object detection and recognition easier and will definitely in the future be introducing 
easier methods than this also .

- However if you any doubt regarding how the code is working in this Repo or One of the Repo's that i referred for training ,
you can whatsapp me - +916265188633 .

- Also do follow <a href="https://www.instagram.com/the_ai_works/">this</a> insta page for seeing the predictions from this model
and also for some good Deep Learning and Data Science Stuffs.
