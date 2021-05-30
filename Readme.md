## Violence Recognition

#### Recognizing violence using deep learning and image processing

+ Downloaded violence videos from youtube and split in to small size and scaled all of their resolution to 240 x 320. 
+ I have used "moviepy" to do all these video processing and then saved them in to violence and nonviolence folders.

### Data set preperation:
+ `resize_video_dimension.py` script is used to resize the video in to the required dimension.
    + To be resized input video path and output video path should be set in the code to resize a video.
+ `split_video.py` script is used to split the video file in to small parts.
    + Input video path and output paths have to be set in the code to split the video and save in the directory..

You can find the dataset that I have used for this model in the below google drive link [Dataset](https://drive.google.com/drive/folders/1qinHCeXS97tO6wgxNm4BDh9T9hWnWmOH)

### Using Resnet50 model
Please look in to `violence_30th.ipynb` file for the complete approach of preprocessing and training methods.

You can download trained model file from this google drive link [Model file](https://drive.google.com/file/d/1A8A9Sbdi-g7zMJgWD9CRZzLJu48-OQh7/view?usp=sharing)

### Using VGG16 model
Please look in to `train-violence-vgg.ipynb` file for the complete approach of preprocessing and training methods.

You can download trained model file from this google drive link [Model file](https://drive.google.com/file/d/1-BEpyMBNDRb94xiymWIQuK-8e8dHTLAR/view?usp=sharing)
you can find detaild explaination in my [blog](https://saraswathimamidala30.medium.com/data-downloading-i-have-downloaded-violence-videos-from-youtube-and-split-in-to-small-size-and-91146b986162)
