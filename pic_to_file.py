from skimage import io
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

def main2():
    folder = '.\\images\\'
    files = os.listdir(folder)
    learning_file = open('learning_data2.bin', 'wb')
    index = 1
    for f in files:
        if '.png' in f:
            image_data = io.imread(folder + f, True)
            is_smile = False
            if index <= 10:
                is_smile = True
            pickle.dump(is_smile, learning_file)
            pickle.dump(image_data, learning_file)
            index += 1
    learning_file.close()

main2()
