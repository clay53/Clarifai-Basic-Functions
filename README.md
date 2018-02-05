# Dependencies
```
pip
python 2.7.x
sudo pip install Clarifai
```

# Setup

Example conf.py
``
# From https://clarifai.com/developer/account/applications

clarifai_key = '<~32 characters>'
model_id = 'dog-or-cat'
```

# Usage 

```
Notes:
This assumes you're cd'd into the project directory
```

Add images to model from directory (only .jpg files will be recongnized)
```
python add_images.py
Enter images directory (./ works)
./dogs
Enter concepts (seperated by comma NO spaces)
dog
Enter not_concepts (seperated by comma NO spaces)
cat
```

Create model (can be done from the website easily)
```
python ceate_model.py
Enter model name
dog-or-cat
Enter concepts (seperated by commas NO spaces)
cat,dog
```

Train model (takes model ID from conf.py)
```
python train_model.py
Training...
Training complete
```

Predict with model
```
Enter file path (./ works)
./dog.jpg
```