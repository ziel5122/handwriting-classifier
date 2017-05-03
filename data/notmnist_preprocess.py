import idx2numpy
from numpy import array, asmatrix
import os
from PIL import Image
from sklearn.preprocessing import scale
from six.moves.urllib.request import urlretrieve
import tarfile

notmnist_path = './notMNIST'
url = 'http://commondatastorage.googleapis.com/books1000/'

def download(filename):
    print('downloading', filename)
    dest_path = os.path.join(notmnist_path, filename)
    dest_path, _ = urlretrieve(url + filename, dest_path)
    print('finished downloading', filename)
    print()
    return dest_path

def extract(path):
    print('extracting', path)
    tar = tarfile.open(path)
    tar.extractall(notmnist_path)
    tar.close()

#extract(download('notMNIST_large.tar.gz'))
#extract(download('notMNIST_small.tar.gz'))

vectors = []
i = 0
small = './notMNIST/notMNIST_small'
for letter_folder in os.listdir(small):
    for image in os.listdir(os.path.join(small, letter_folder)):
        png = Image.open(os.path.join(small, letter_folder, image))
        width, height = png.size
        img = png.load()
        print(i)
        i += 1
        values = []
        for h in range(0, height):
            for w in range(0, width):
                values.append(img[w, h])

        vectors.append(array(values))

small = './notMNIST/notMNIST_large'
for letter_folder in os.listdir(small):
    for image in os.listdir(os.path.join(small, letter_folder)):
        try:
            png = Image.open(os.path.join(small, letter_folder, image))
            width, height = png.size
            img = png.load()
            print(i)
            i += 1
            values = []
            for h in range(0, height):
                for w in range(0, width):
                    values.append(img[w, h])

            vectors.append(array(values))
        except IOError:
            os.remove(os.path.join(small, letter_folder, image))
            print('removed')

print(len(vectors))

features = array(vectors)
print(len(features))
print(features.shape)
scaled_features = scale(features)
idx2numpy.convert_to_file('./notMNIST/notmnist-features.idx', scaled_features)
'''
png = Image.open('./notMNIST/notMNIST_small/A/MDEtMDEtMDAudHRm.png')
width, height = png.size
img = png.load()

images
values = []
for h in range(0, height):
    for w in range(0, width):
        values.append(img[w, h])

arr = array(values)
print(arr)
'''
