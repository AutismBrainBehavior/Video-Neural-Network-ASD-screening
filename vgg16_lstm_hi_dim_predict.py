import numpy as np
from keras import backend as K
import sys
import os
import gc

def main():
    K.common.set_image_dim_ordering('tf')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from recurrent_networks import vgg16LSTMVideoClassifier
    from UCF101_loader import load_ucf, scan_ucf_with_labels

    vgg16_include_top = False
    data_dir_path = os.path.join(os.path.dirname(__file__), 'very_large_data')
    model_dir_path = os.path.join(os.path.dirname(__file__), 'models', 'autism_data')
    config_file_path = vgg16LSTMVideoClassifier.get_config_file_path(model_dir_path,
                                                                     vgg16_include_top=vgg16_include_top)
    weight_file_path = vgg16LSTMVideoClassifier.get_weight_file_path(model_dir_path,
                                                                     vgg16_include_top=vgg16_include_top)

    np.random.seed(42)

    load_ucf(data_dir_path)

    predictor = vgg16LSTMVideoClassifier()
    predictor.load_model(config_file_path, weight_file_path)

    videos = scan_ucf_with_labels(data_dir_path, [label for (label, label_index) in predictor.labels.items()])

    video_file_path_list = np.array([file_path for file_path in videos.keys()])
    np.random.shuffle(video_file_path_list)

    correct_count = 0
    count = 0

    for video_file_path in video_file_path_list:
        label = videos[video_file_path]
        predicted_label = predictor.predict(video_file_path)
        print('predicted: ' + predicted_label + ' actual: ' + label)
        correct_count = correct_count + 1 if label == predicted_label else correct_count
        count += 1
        accuracy = correct_count / count
        #print('accuracy: ', accuracy)
        gc.collect()


if __name__ == '__main__':
    main()
