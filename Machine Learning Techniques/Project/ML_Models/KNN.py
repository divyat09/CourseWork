from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import datasets
import scipy.io as sio
import numpy as np 
import math


Angry_train=sio.loadmat('/home/divyat/Desktop/Project/Merged_train/Angry.mat')['X']
Disgust_train=sio.loadmat('/home/divyat/Desktop/Project/Merged_train/Disgust.mat')['X']
Fear_train=sio.loadmat('/home/divyat/Desktop/Project/Merged_train/Fear.mat')['X']
Happy_train=sio.loadmat('/home/divyat/Desktop/Project/Merged_train/Happy.mat')['X']
Neutral_train=sio.loadmat('/home/divyat/Desktop/Project/Merged_train/Neutral.mat')['X']
Sad_train=sio.loadmat('/home/divyat/Desktop/Project/Merged_train/Sad.mat')['X']
Surprise_train=sio.loadmat('/home/divyat/Desktop/Project/Merged_train/Surprise.mat')['X']


Angry_test=sio.loadmat('/home/divyat/Desktop/Project/Merged_test/Angry.mat')['X']
Disgust_test=sio.loadmat('/home/divyat/Desktop/Project/Merged_test/Disgust.mat')['X']
Fear_test=sio.loadmat('/home/divyat/Desktop/Project/Merged_test/Fear.mat')['X']
Happy_test=sio.loadmat('/home/divyat/Desktop/Project/Merged_test/Happy.mat')['X']
Neutral_test=sio.loadmat('/home/divyat/Desktop/Project/Merged_test/Neutral.mat')['X']
Sad_test=sio.loadmat('/home/divyat/Desktop/Project/Merged_test/Sad.mat')['X']
Surprise_test=sio.loadmat('/home/divyat/Desktop/Project/Merged_test/Surprise.mat')['X']


Emotion_train=[Happy_train, Angry_train , Disgust_train, Fear_train, Neutral_train , Sad_train, Surprise_train]
Emotion_test=[ Happy_test, Angry_test, Disgust_test, Fear_test, Neutral_test , Sad_test, Surprise_test]


Train_Data=Emotion_train[0] #Test data MxD form....D=number of features
[M,N]=Train_Data.shape
y=np.zeros(M)		#True labels of the training data


i=1
while(i<7):
	Train_Data_temp=Emotion_train[i]
	[M,N]=Train_Data_temp.shape
	y_temp=i*np.ones(M)
	y=np.concatenate((y, y_temp), axis=0)	
	Train_Data=np.concatenate((Train_Data, Train_Data_temp), axis=0)
	i=i+1


i=1
accuracy=[]
while(i<15):
	knn = KNeighborsClassifier(n_neighbors=i,weights='distance')
	knn.fit(Train_Data,y)
	[N_test,count,j]=[0,0,0]
	
	while(j<7):
		
		[M,N]=Emotion_test[j].shape
		N_test=N_test+M
		y_predicted=knn.predict(Emotion_test[j])
		print(y_predicted)
		count=count+(y_predicted==j*np.ones(M)).sum()
		j=j+1

	accuracy.append(count*100.0/N_test)
	i=i+1

K=np.linspace(1,14,14)
plt.plot(K,accuracy)
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.show()



















	