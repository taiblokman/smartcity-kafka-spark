import os
from confluent_kafka import SerializingProducer
import simplejson as json
from datetime import datetime

LONDON_COORDINATE = { "latitude": 51.55074, "longitude": -0.1278 }
BIRMINGHAM_COORDINATE = { "latitude": 52.4862, "longitude": -1.8904 }

# calc movement increment
LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATE['latitude'] -
                      LONDON_COORDINATE['latitude']) / 100
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATE['longitude'] -
                      LONDON_COORDINATE['longitude']) / 100

# Env variables for configuration
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC', 'vehicle_data')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_data')
TRAFFIC_TOPIC = os.getenv('TRAFFIC_TOPIC', 'traffic_data')
WEATHER_TOPIC = os.getenv('WEATHER_TOPIC', 'weather_data')
EMERGENCY_TOPIC = os.getenv('EMERGENCY_TOPIC', 'emergency_data')

start_time = datetime.now()
start_location = LONDON_COORDINATE.copy()

if __name__ = "__main__":
    producer_config = {
        'bootstrap.servers':
    }