from kafka import KafkaProducer
import json
import pandas as pd
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

df = pd.read_csv('data/test_row.csv')

for _, row in df.iterrows():
    data = row.to_dict()
    producer.send('sigma_topic', value=data)
    print(f"Sent row to Kafka: {data}")
    time.sleep(10)
