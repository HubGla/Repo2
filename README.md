# Black-Scholes Sigma Predictor with Apache Kafka

## Opis
- `producer.py`: przesyła dane wejściowe z pliku CSV co 10 sekund do tematu `sigma_topic`.
- `consumer.py`: odbiera dane, przewiduje zmienność (σ), liczy wartość opcji BS i predyktuje wynik.

## Uruchomienie
1. Zainstaluj zależności:
```
pip install -r requirements.txt
```
2. Upewnij się, że Kafka działa na `localhost:9092`.
3. Uruchom producenta:
```
python producer.py
```
4. Uruchom konsumenta:
```
python consumer.py
```
