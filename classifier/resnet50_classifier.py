import numpy as np
import pandas as pd
import tensorflow as tf
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image

model = ResNet50(weights="imagenet")

def classify_image(path_to_image: str):
    img = image.load_img(path_to_image, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)

    return create_html_table_from_preds(preds)


def create_html_table_from_preds(preds):
    predictions = decode_predictions(preds, top=10)[0]
    result = pd.DataFrame(columns=['Label', 'Probability'])
    result['Label'] = [p[1] for p in predictions]
    result['Probability'] = [str(round(p[2] * 100, 1)) + '%' for p in predictions]

    return result.to_html(escape=False, index=False, classes='display" id = "classifications')
