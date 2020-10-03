import numpy as np
import os
import sys
import cv2

def apply_kernel(kernel, image_name):
    img_src = cv2.imread(image_name, cv.IMREAD_GRAYSCALE)

    # -1 is to keep images with same depth
    img = cv2.filter2D(img_src, -1, kernel)

    cv2.imshow('new', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    # check that user supplied an image as argument
    if len(sys.argv) != 2:
        print('Usage: {} <picture file name>'.format(sys.argv[0]))
        sys.exit(1)

    in_file_name = sys.argv[1]

    # make sure this image exists
    if not os.path.isfile(in_file_name):
        print('{} doesn\'t exist'.format(in_file_name))
        sys.exit(1)

    kernel = np.array([[1.0, 1.0, 1.0], 
                       [1.0, -8.0, 1.0],
                       [1.0, 1.0, 1.0]])

    apply_kernel(kernel=kernel, image_name=in_file_name)
