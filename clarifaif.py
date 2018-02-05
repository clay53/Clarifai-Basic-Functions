from conf import clarifai_key
from conf import model_id

from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key=clarifai_key)
model = app.models.get(model_id)

def add_images (images, concepts, not_concepts):
    imgs = []
    for img in images:
        print img
        imgs.append(ClImage(file_obj=open(img, 'rb'), concepts=concepts, not_concepts=not_concepts))
    return app.inputs.bulk_create_images(imgs)

def create_model (name, concepts):
    return app.models.create(name, concepts=concepts)

def train_model ():
    return model.train()

def predict (file):
    return model.predict([ClImage(file_obj=open(file, 'rb'))])