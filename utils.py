# ------------------------------------------------------------
# Real-Time Style Transfer Implementation
# Licensed under The MIT License [see LICENSE for details]
# Written by Cheng-Bin Jin
# Email: sbkim0407@gmail.com
# ------------------------------------------------------------
import os
import sys
import scipy.misc
import numpy as np
import imageio
import skimage


def imread(path, is_gray_scale=False, img_size=None):
    if is_gray_scale:
        img = imageio.imread(path, as_gray=True)

    else:
        # img = imageio.imread(path, pilmode='RGB')
        img = imageio.imread(path)

        if not (img.ndim == 3 and img.shape[2] == 3):
            img = np.dstack((img, img, img))

    if img_size is not None:
        img = skimage.transform.resize(img, img_size)

    return img


def imsave(path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    imageio.imwrite(path, img)


def all_files_under(path, extension=None, append_path=True, sort=True):
    if append_path:
        if extension is None:
            filenames = [os.path.join(path, fname) for fname in os.listdir(path)]
        else:
            filenames = [os.path.join(path, fname)
                         for fname in os.listdir(path) if fname.endswith(extension)]
    else:
        if extension is None:
            filenames = [os.path.basename(fname) for fname in os.listdir(path)]
        else:
            filenames = [os.path.basename(fname)
                         for fname in os.listdir(path) if fname.endswith(extension)]

    if sort:
        filenames = sorted(filenames)

    return filenames


def exists(p, msg):
    assert os.path.exists(p), msg


def print_metrics(itr, kargs):
    print("*** Iteration {}  ====> ".format(itr))
    for name, value in kargs.items():
        print("{} : {}, ".format(name, value))
    print("")
    sys.stdout.flush()

