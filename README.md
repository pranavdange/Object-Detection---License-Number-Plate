# Object-Detection-License-Number-Plate


I intend to detect the License Plate of any vehicle – though be in Car, Bus, Truck from images or Video.
Once developed can be used in multivariate applications like Traffic monitoring, criminal activity identification, etc.
Dataset link –
https://storage.googleapis.com/openimages/web/visualizer/index.html?set=train&type=detection&c=%2Fm%2F01jfm_

Drive Link for Trained Model –
https://drive.google.com/drive/folders/1Diy9gLYAlwk4q3XR5YUVp-xW88Tgurhb?usp=sharing
![image](https://user-images.githubusercontent.com/75486718/126176199-d41bbca8-7b1c-48aa-93e9-f67c8c95a34a.png)

Workflow
![image](https://user-images.githubusercontent.com/75486718/126176277-324a7eaa-2c90-4642-b196-3f7c32ca66b4.png)

![image](https://user-images.githubusercontent.com/75486718/126176304-d15e59bf-e4e1-4afe-8b39-48df0eb49b49.png)

Custom Training 

This step involves properly configuring your custom .cfg, obj.data, obj.names, train.txt and test.txt files.
It is important to configure all these files with extreme caution as typos or small errors can cause major problems with your custom training
Configuring Variables:

width = 416
height = 416 (these can be any multiple of 32, 416 is standard, we can sometimes improve results by making value larger like 608 but will slow down training)
max_batches = (# of classes) * 2000 (but no less than 6000 so if you are training for 1, 2, or 3 classes it will be 6000
steps = (80% of max_batches), (90% of max_batches) (so if your max_batches = 10000, then steps = 8000, 9000)
filters = (# of classes + 5) * 3 (so if you are training for one class then your filters = 18
The last configuration files needed before we can begin to train our custom detector are the train.txt and test.txt files which hold the relative paths to all our training images and validation images.

Darknet and Tensorflow Use -

![image](https://user-images.githubusercontent.com/75486718/126176777-13b490bd-179d-4fa6-8e02-eeaafc149ff8.png)


Deployment on Local
![image](https://user-images.githubusercontent.com/75486718/126176694-b068eb4f-c4a4-4277-997f-f594664a8f09.png)
![image](https://user-images.githubusercontent.com/75486718/126176717-65ca047f-9497-4bbe-bf72-ae77fbfd4db8.png)

Summary 

Finally, using Yolo, Darknet and TensorFlow, an end to end model is created which can detect license plate from any of the images and Videos provided. Future scope of the Project includes using the same as Webcam!

Note -

Please note that the Model uses Yolo V4 Model and Custom Training is done. I have tried making it simple and easy to follow. To make it run directly by git cloning on your local machine you need data files, etc. Please contact and make a request for the same by dropping a message. Always happy to help :)
