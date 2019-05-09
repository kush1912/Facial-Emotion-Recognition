import os
import sys
import cv2
import numpy as np
import pandas as pd

def main():

    output_path = sys.argv[1]                       # directory name is defined

    if os.path.exists(output_path):

        os.system('rm -rf {}'.format(output_path))  #remove the ouput path if it already exists

    os.system('mkdir {}'.format(output_path))       #make the directory with output_path

    label_names = ['0_Angry', '1_Disgust', '2_Fear', '3_Happy', '4_Sad', '5_Surprise', '6_Neutral']
    data = pd.read_csv('Testing.csv', delimiter=',')
    
    labels = data.iloc[1:,0].astype(np.int32)       # emotion column
    image_buffer = data.iloc[1:,1]                  # image column
    images = np.array([np.fromstring(image, np.uint8, sep=' ') for image in image_buffer])
    usage = data.iloc[1:,2]                         #type of data-(training or testing)
    dataset = zip(labels, images, usage)
    for i, d in enumerate(dataset):
        usage_path = os.path.join(output_path, d[-1])
        label_path = os.path.join(usage_path, label_names[d[0]])
        img = d[1].reshape((48,48))
        img_name = '%08d.jpg' % i                    # image name
        img_path = os.path.join(label_path, img_name)
        if not os.path.exists(usage_path):              # if directory not existed then created 
            os.system('mkdir {}'.format(usage_path))    
        if not os.path.exists(label_path):
            os.system('mkdir {}'.format(label_path))
        cv2.imwrite(img_path, img)                  #creating image from values 
        print ('Write {}'.format(img_path))

if __name__ == '__main__':
    main()
