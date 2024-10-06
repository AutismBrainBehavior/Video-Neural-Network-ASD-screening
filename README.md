[![CC BY-NC-ND 4.0][cc-by-nc-nd-shield]][cc-by-nc-nd]

[cc-by-nc-nd]: http://creativecommons.org/licenses/by-nc-nd/4.0/
[cc-by-nc-nd-image]: https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png
[cc-by-nc-nd-shield]: https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg

## ADOS OpenPose Video Neural Network

This repository consists of the code used for carrying out classification of Autism Spectrum Disorder (ASD) using [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) normalised ADOS clinical examination video recordings ([Paper 1](https://www.nature.com/articles/s41598-021-94378-z) & [Paper 2](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0308388)). The neural network's code was inspired from [VideoClassifier-CNNLSTM](https://github.com/jibinmathew69/VideoClassifier-CNNLSTM) and modified for training and prediction over our ADOS clinical examination recordings dataset. The videos were generated using [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) with blank background over which skeletal keypoints were plotted. The neural network was tested on University of Geneva's high-performance computing cluster, Baobab. The slurm scripts for the same are `run_nn.sh` for training and `run_predict.sh` for testing. The neural network was originally used for classification of [UCF-101](https://www.crcv.ucf.edu/data/UCF101.php) video dataset.

An illustration of OpenPose Normalized videos videos after carrying out pre-processing can be observed as follows:

<p align="center">
<img src=https://github.com/nshreyasvi/Video-Neural-Network-ASD-screening/blob/main/illustrations/openpose.jpg>
</p>

### Usage with Anaconda3
The following instructions can be used to run the neural network using [Anaconda](https://www.anaconda.com/):
- Create a new anaconda environment using `conda create -n env python=3.6 -y`
- Install conda dependencies using `conda install ffmpeg numpy pandas scikit-learn scipy matplotlib tensorflow-gpu==1.15.0 keras opencv -y`
- Install pip dependencies using `pip install opencv-contrib-python==4.1.2.30 imutils`
- The code will generate classes based on the folders present inside `very_large_data/autism_data` folder.
- Add the video data in folders with their respective class names inside the `very_large_data/autism_data` folder.
- Carry out training by using `python vgg16_lstm_hi_dim_train.py` or using other `_train.py` scripts.
- Once training is finished, the history of the training can be seen in `reports/autism_data`.
- The trained models can be seen in `models/autism_data` folder.
- Replace the training dataset inside the `very_large_data/autism_data` folder with testing data in a similar folder structure (using dummy class labels if prediction is not known.)
- Predictions can be carried out using `python vgg16_lstm_hi_dim_predict.py` or using other `_predict.py` scripts.
- The output predictions can be seen on the terminal or either be stored in a `.csv` by using `python vgg16_lstm_hi_dim_predict.py > output.csv`.

In our first research studies, we carried out prediction aggregation by splitting long videos into 5-second segments for optimal training and prediction. The output `.csv` file can be used to carry out prediction aggregation to obtain final prediction over the entire video. In our second study (video-audio neural network ensemble), we also implemented a prediction aggregation condition where we only used clips which were predicted with more than 90% confidence for aggregated final prediction over the entire video. In that approach, we used the same output `.csv` file for tinkering around. 

An example of the training log for the neural network can be observed as follows:

<p align="center">
<img src=https://github.com/nshreyasvi/Video-Neural-Network-ASD-screening/blob/main/reports/autism_data/vgg16-lstm-hi-dim-history.png>
</p>

### Citation
```
@article{10.1371/journal.pone.0308388,
    doi = {10.1371/journal.pone.0308388},
    author = {Natraj, Shreyasvi AND Kojovic, Nada AND Maillart, Thomas AND Schaer, Marie},
    journal = {PLOS ONE},
    publisher = {Public Library of Science},
    title = {Video-audio neural network ensemble for comprehensive screening of autism spectrum disorder in young children},
    year = {2024},
    month = {10},
    volume = {19},
    url = {https://doi.org/10.1371/journal.pone.0308388},
    pages = {1-20},
    abstract = {A timely diagnosis of autism is paramount to allow early therapeutic intervention in preschoolers. Deep Learning tools have been increasingly used to identify specific autistic symptoms. But they also offer opportunities for broad automated detection of autism at an early age. Here, we leverage a multi-modal approach by combining two neural networks trained on video and audio features of semi-standardized social interactions in a sample of 160 children aged 1 to 5 years old. Our ensemble model performs with an accuracy of 82.5% (F1 score: 0.816, Precision: 0.775, Recall: 0.861) for screening Autism Spectrum Disorders (ASD). Additional combinations of our model were developed to achieve higher specificity (92.5%, i.e., few false negatives) or sensitivity (90%, i.e. few false positives). Finally, we found a relationship between the neural network modalities and specific audio versus video ASD characteristics, bringing evidence that our neural network implementation was effective in taking into account different features that are currently standardized under the gold standard ASD assessment.},
    number = {10},
}
```
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
