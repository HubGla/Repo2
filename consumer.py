from kafka import KafkaConsumer
import json
import joblib
import numpy as np
import pandas as pd
from utils import bs73

# Wczytaj wytrenowany model
model = joblib.load('model/xgb_model.pkl')

# Połącz z Kafką
consumer = KafkaConsumer(
    'sigma_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    row = msg.value
    row_df = pd.DataFrame([row])
    S0 = row_df['Zamkniecie'][0]
    sigma = (model.predict(row_df)[0] / S0) * np.sqrt(252)
    sigma = np.clip(sigma, 0.01, 0.8)
    K = round(S0 / 5) * 5
    r = row_df['wibor3m'][0] * 0.01
    T = 1 / 252
    price = bs73(S0, K, T, r, sigma)
    print(f"[Kafka] S0={S0}, sigma={sigma:.4f}, opcja (BS)={price:.2f}")
