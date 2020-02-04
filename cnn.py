from skimage import io
from skimage import util
import numpy as np
import math

def maxpul(image, shape):
    image_shape = np.shape(image)
    res = [] #np.zeros([(image_shape[0])//shape[0], image_shape[1]//shape[1]])
    for y in range(0, image_shape[0], shape[0]):
        for x in range(0, image_shape[1], shape[1]):
            max_val = -math.inf
            for c_y in range(shape[0]):
                if y+c_y < image_shape[0]:
                    for c_x in range(shape[1]):
                        if x + c_x < image_shape[1]:
                            val = image[y+c_y][x+c_x]
                            if (val > max_val):
                                max_val = val
            res.append(max_val)
    newshape = [(image_shape[0] + shape[0] - 1) // shape[0], (image_shape[1] + shape[1] - 1) // shape[1]]
    return np.reshape(res,newshape)



def convolute(image, ceed):
    ceed_shape = np.shape(ceed)
    ceed_center_y = ceed_shape[0] // 2
    ceed_center_x = ceed_shape[1] // 2
    image_shape = np.shape(image)
    res = np.zeros(image_shape)
    for im_y in range(image_shape[0]):
        for im_x in range(image_shape[1]):
            pix = 0
            for c_y in range(ceed_shape[0]):
                delta_y = c_y-ceed_center_y
                if 0 <= im_y + delta_y < image_shape[0]:
                    for c_x in range(ceed_shape[1]):
                        delta_x = c_x - ceed_center_x
                        if 0 <= im_x + delta_x < image_shape[1]:
                            pix += image[im_y+delta_y][im_x+delta_x]*ceed[c_y][c_x]
            res[im_y][im_x] = pix/len(ceed)
    return res


def main():
    image_data = io.imread("test.png", True)
    image_data = util.invert(image_data)
    ceed = [[1, 1, 1],
            [0, 0, 0],
            [0, 0, 0]]
    new_data = convolute(image_data, ceed)
    max_data = maxpul(new_data, [3,3])
#    new_data = convolute(max_data, ceed)
#    max_data = maxpul(new_data, [2,2])
    io.imshow_collection([image_data,new_data, max_data])
    io.show()
    print(new_data)


main()
