from skimage import io
from skimage.color import rgb2gray
import os
import pickle


def main():
    folder = '.\\images\\'
    files = os.listdir(folder)
    learning_file = open('learning_data.bin', 'wb')
    index = 1
    for f in files:
        if '.png' in f:
            image_data = io.imread(folder + f, True)
            pixels = []
            for i in range(image_data.shape[0]):
                for j in range(image_data.shape[1]):
                    pixels.append(image_data[i][j])
            is_smile = False
            if index <= 10:
                is_smile = True
            pickle.dump(is_smile, learning_file)
            pickle.dump(pixels, learning_file)
            index += 1
    learning_file.close()

def store_to_file(folder, is_happy, num_files = None):
    files = os.listdir(folder)
    mode = 'wb' if is_happy else 'ab'
    learning_file = open('learning_data3.bin', mode)
    if num_files:
        pickle.dump(num_files, learning_file)

    for f in files:
        if '.png' in f:
            image_data = io.imread(folder + f)
            image_data = rgb2gray(image_data)
            pickle.dump(is_happy, learning_file)
            pickle.dump(image_data, learning_file)
    learning_file.close()

def main2():
    num_files = len(os.listdir('.\\images\\happy\\')) + len(os.listdir('.\\images\\sad\\'))
    store_to_file('.\\images\\happy\\', True, num_files)
    store_to_file('.\\images\\sad\\', False)

main2()
