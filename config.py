# All paths are relative to train_val.py file
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
config = {
	'images_path': os.path.join(base_dir, 'train_val_data', 'Flicker8k_Dataset') + os.sep,  # Make sure you put that last slash (/)
	'train_data_path': os.path.join(base_dir, 'train_val_data', 'Flickr_8k.trainImages.txt'),
	'val_data_path': os.path.join(base_dir, 'train_val_data', 'Flickr_8k.devImages.txt'),
	'captions_path': os.path.join(base_dir, 'train_val_data', 'Flickr8k.token.txt'),
	'tokenizer_path': os.path.join(base_dir, 'model_data', 'tokenizer.pkl'),
	'model_data_path': os.path.join(base_dir, 'model_data') + os.sep,  # Make sure you put that last slash (/)
	'model_load_path': os.path.join(base_dir, 'model_data', 'model_inceptionv3_epoch-20_train_loss-2.4050_val_loss-3.0527.hdf5'),
	'num_of_epochs': 20,
	'max_length': 40,  # This is set manually after training of model and required for test.py
	'batch_size': 64,
	'beam_search_k': 3,
	'test_data_path': os.path.join(base_dir, 'train_val_data', 'Flickr_8k.testImages.txt'),  # Correct test data path
	'model_type': 'inceptionv3',  # inceptionv3 or vgg16
	'random_seed': 1035
}

rnnConfig = {
	'embedding_size': 300,
	'LSTM_units': 256,
	'dense_units': 256,
	'dropout': 0.3
}
