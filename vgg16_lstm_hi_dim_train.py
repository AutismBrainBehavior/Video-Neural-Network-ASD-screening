import numpy as np
from keras import backend as K
import os
import sys


def main():
    K.common.set_image_dim_ordering('tf')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from plot_utils import plot_and_save_history
    from recurrent_networks import vgg16LSTMVideoClassifier
    from UCF101_loader import load_ucf

    data_set_name = 'autism_data'
    input_dir_path = os.path.join(os.path.dirname(__file__), 'very_large_data')
    output_dir_path = os.path.join(os.path.dirname(__file__), 'models', data_set_name)
    report_dir_path = os.path.join(os.path.dirname(__file__), 'reports', data_set_name)

    np.random.seed(42)

    # this line downloads the video files of UCF-101 dataset if they are not available in the very_large_data folder
    load_ucf(input_dir_path)

    classifier = vgg16LSTMVideoClassifier()

    history = classifier.fit(data_dir_path=input_dir_path, model_dir_path=output_dir_path, vgg16_include_top=False,
                             data_set_name=data_set_name)

    plot_and_save_history(history, vgg16LSTMVideoClassifier.model_name,
                          report_dir_path + '/' + vgg16LSTMVideoClassifier.model_name + '-hi-dim-history.png')


if __name__ == '__main__':
    main()
