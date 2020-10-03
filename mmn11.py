import sys
import os
import cv2

def swap_red_and_green(in_file_name, out_file_name):
    # read file
    img = cv2.imread(in_file_name)
    # open window to show it
    cv2.imshow('orig', img)

    _,g,r = cv2.split(img)
    img[:,:,2] = g
    img[:,:,1] = r

    # show new pic
    cv2.imshow('new', img)
    cv2.waitKey(0)

    # write new picture to file
    cv2.imwrite(out_file_name, img)

if __name__ == '__main__':
    out_file_name = 'OutPicture.png'

    # check that user supplied an image as argument
    if len(sys.argv) != 2:
        print('Usage: {} <picture file name>'.format(sys.argv[0]))
        sys.exit(1)

    in_file_name = sys.argv[1]

    # make sure this image exists
    if not os.path.isfile(in_file_name): 
        print('{} doesn\'t exist'.format(in_file_name))
        sys.exit(1)

    # call swap function
    swap_red_and_green(in_file_name, out_file_name)
