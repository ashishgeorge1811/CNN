#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Data_Augmentation using single image


# In[ ]:


from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')  #fill_mode can be [constant,reflect,wrap instead of nearest]
 

img = load_img('C:\\Users\\AshishGeorge\\Desktop\\advanced_poles\\ireland\\z490.PNG')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
 

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='C:\\Users\\AshishGeorge\\Desktop\\New folder', save_prefix='bird', save_format='PNG'):
    i += 1
    if i > 50:
        break  # otherwise the generator would loop indefinitely


# In[ ]:


#Data_Augumentation using images in a folder


# In[ ]:


from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

 
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

 

import pathlib


PATH_TO_TEST_IMAGES_DIR = pathlib.Path(r'C:\\Users\\AshishGeorge\\Desktop\\augmentation')
# extensions = ("*.jpg","*.JPG","*.jpeg")
# TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob(extensions)))
# TEST_IMAGE_PATHS
extensions = ("*.jpg","*.jpeg","*.png")
testimage = []
for extension in extensions:
    
    testimage.extend(PATH_TO_TEST_IMAGES_DIR.glob(extension))
  
for image in testimage:
    print(image)
    img = load_img(image)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)# this is a Numpy array with shape (1, 3, 150, 150)
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=r'C:\\Users\\AshishGeorge\\Desktop\\augmentation', save_prefix='bird', save_format='PNG'):
        i += 1
        if i > 2:
            break 


# In[ ]:




