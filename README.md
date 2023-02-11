## Video Neural Network

This repository consists of the code used for carrying out classification of Autism Spectrum Disorder (ASD). The neural network's code was inspired from [VideoClassifier-CNNLSTM](https://github.com/jibinmathew69/VideoClassifier-CNNLSTM) and modified for training and prediction over our ADOS clinical examination recordings dataset. The neural network was originally used for classification of [UCF-101](https://www.crcv.ucf.edu/data/UCF101.php) video dataset.

### Usage with Anaconda3
The following instructions can be used to run the neural network:
- Create a new anaconda environment using `conda create -n env python=3.6 -y`
- Install the dependencies required using `conda install numpy pandas scikit-learn scipy matplotlib tensorflow-gpu==1.15.0 keras opencv -y`
- The code will generate classes based on the folders present inside `very_large_data/autism_data` folder.
- Add the video data in folders with their respective class names inside the `very_large_data/autism_data` folder.
- Carry out training by using `python vgg16_lstm_hi_dim_train.py` or using other `_train.py` scripts.
- Once training is finished, the history of the training can be seen in `reports/autism_data`.
- The trained models can be seen in `models/autism_data` folder.
- Replace the training dataset inside the `very_large_data/autism_data` folder with testing data in a similar folder structure (using dummy class labels if prediction is not known.)
- Predictions can be carried out using `python vgg16_lstm_hi_dim_predict.py` or using other `_predict.py` scripts.
- The output predictions can be seen on the terminal or either be stored in a `.csv` by using `python vgg16_lstm_hi_dim_predict.py > output.csv`.

In our project, we carried out prediction aggregation by splitting long videos into 5-second segments for optimal training and prediction. The output `.csv` file can be used to carry out prediction aggregation to obtain final prediction over the entire video. The videos were generated using [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) with blank background over which skeletal keypoints were plotted.

### Citation
If you use these tools in your research, please cite this project.

```
@article{Kojovic2021,
	title        = {Using 2D video-based pose estimation for automated prediction of autism spectrum disorders in young children},
	author       = {Kojovic, Nada and Natraj, Shreyasvi and Mohanty, Sharada Prasanna and Maillart, Thomas and Schaer, Marie},
	year         = 2021,
	month        = {Jul},
	day          = 23,
	journal      = {Scientific Reports},
	volume       = 11,
	number       = 1,
	pages        = 15069,
	doi          = {10.1038/s41598-021-94378-z},
	issn         = {2045-2322},
	url          = {https://doi.org/10.1038/s41598-021-94378-z}
}
```