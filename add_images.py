import glob

from clarifaif import add_images

input1 = raw_input('Enter images directory (./ works) \n')
images = []
for img in glob.glob(input1 + '/*.jpg'):
    print img
    images.append(img)

input2 = raw_input('Enter concepts (seperated by comma NO spaces) \n')
concepts = input2.split(',')
for concept in concepts:
    print concept

input3 = raw_input('Enter not_concepts (seperated by comma NO spaces) \n')
not_concepts = input3.split(',')
for not_concept in not_concepts:
    print not_concept

add_images(images, concepts, not_concepts)