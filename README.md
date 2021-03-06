# GOIT3

For now - the Auth tokens for GitHub are blocked in security reasons. That's why no continuous deployment is available through GitHub.

So all the sources passed to Heroku using the HEROKU CLI

Model stored at Google Drive and could be rolled out to disk space at the time of first launch. Also there is an option to store it in PGDB


Sources of Vgg16 model you could find by link 

https://drive.google.com/file/d/1LJnhd4X4GIjoaBv40DtgxGryT33xQykT/view?usp=sharing

Heroku app -  web-based image recogniser available here: https://goit3.herokuapp.com/IR/

Docker Image stored at - https://hub.docker.com/r/mathteacher/project3_neural

To get it from docker hub run  <strong> docker pull mathteacher/project3_neural:demo </strong>

To run it use command <strong> docker compose up neural </strong> with <i>Docker-compose.yml</i> (due to containing sensitive info could be send by request omly). 


In this project, it was proposed to train a neural network to recognize pictures of 10 different classes

![image](https://user-images.githubusercontent.com/81954790/163984233-944fed53-a0f7-4bc9-8059-169bb3c1a74f.png)


A pre-trained convolutional neural network was used to train the model. 

As a convolutional basis, the VGG16 network trained on ImageNet data was used to extract useful features from the cifar10 dataset

![image](https://user-images.githubusercontent.com/81954790/163985420-43201cf1-0173-4a72-926d-7cf4576e4726.png)

To improve the accuracy of the model, the data extension technique was used

Thanks to this, it was possible to avoid retraining of the model and the accuracy of the model was achieved at the level of 92%

![image](https://user-images.githubusercontent.com/81954790/163985694-25eddf9e-e858-437b-b95c-c92a034b07a8.png)


Loss and accuracy graphs

![image](https://user-images.githubusercontent.com/81954790/163984002-cbc12b3f-ae4a-4b95-a21d-da22e3f243ca.png)


Results of our work

![image](https://user-images.githubusercontent.com/81954790/163985133-94975f79-1cba-460a-a564-e16aeaed9930.png)
