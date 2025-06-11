import sys

import joblib
import os

model = joblib.load(os.path.join(os.getcwd(), 'models', 'quotes_model.pkl'))
vectorizer = joblib.load(os.path.join(os.getcwd(), 'models', 'vectorizer.pkl'))
mlb = joblib.load(os.path.join(os.getcwd(), 'models', 'mlb.pkl'))

def predict_tags(text):
    text_new = vectorizer.transform([text])
    prediction_proba = model.predict_proba(text_new)
    threshold = 0.3
    prediction = (prediction_proba >= threshold).astype(int)
    return mlb.inverse_transform(prediction)

if __name__ == '__main__':
    print('Enter quote (or exit to quit): ')
    while True:
        quote = input('> ')
        predicted_tags = predict_tags(quote)[0]
        if len(predicted_tags) > 0:
            print(f'Predicted tags: {', '.join(x.capitalize() for x in predicted_tags)}')
        else:
            print(f'No tags predicted')
        if quote.lower() == 'exit':
            break
