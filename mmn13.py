import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import sys
import os


def local_histogram_enhancment(block_dimensions, image_name):
    # read the image in grayscale
    img = cv.imread(image_name, cv.IMREAD_GRAYSCALE)
    # show original image
    cv.imshow('Original Image', img)
    # extract image shape
    height, width = img.shape

    # we want to present multiple options of the local histogram enhacment
    # so we will show all of them together for comparison
    fig = plt.figure(figsize=(12, 12))
    columns = int(np.sqrt([len(block_dimensions)]))
    rows = int(len(block_dimensions) / columns)

    for i, dimensions in enumerate(block_dimensions, start=1):
        m, n = dimensions
        # use opencv2 builtin ContrastLimited Adaptive histogram equalization with different
        # block dimension
        clahe = cv.createCLAHE(clipLimit=0.0, tileGridSize=(m, n))
        eimg = clahe.apply(img)
        fig.add_subplot(rows, columns, i)
        # add the image with enhancment to the figure
        plt.imshow(eimg, cmap='gray')
        plt.title('Box size {}x{}'.format(m, n))
    
    # present the result
    fig.tight_layout(pad=2.0)
    plt.show()

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

    block_dimensions = [(3, 3), (9, 9), (15, 15), (31, 31), (63, 63), (127, 127)]

    local_histogram_enhancment(block_dimensions=block_dimensions, image_name=in_file_name)

