from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_PATH = "/app/model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

app = FastAPI()

class Input(BaseModel):
    text: str

@app.post("/predict")
def predict(payload: Input):
    inputs = tokenizer(payload.text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = model(**inputs).logits

    pred = int(torch.argmax(logits, dim=1))

    return {
        "prediction": pred
    }
