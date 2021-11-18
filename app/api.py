from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model

import numpy as np

IMAGE_SIZE = (224, 224, 3)
LABELS = ('chili-dog', 'food', 'frankfurter', 'furniture', 'hotdog', 'people', 'pets')

app = FastAPI()
model_loaded = load_model('./app/models/')

# Response for endpoint prediction
class Response(BaseModel):
    prediction: str

def read_image(file: bytes):
    with open('image.png', 'wb') as img:
        img.write(file)
    img = load_img('image.png', target_size=IMAGE_SIZE)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

@app.post("/predict/", response_model=Response)
async def predict(myfile: UploadFile = File(...)):
    image = read_image(await myfile.read())

    results = model_loaded.predict_on_batch(image)[0]

    label_prediction = LABELS[np.argmax(results, axis=-1)]
    predictions = { 'prediction': label_prediction }

    return predictions
