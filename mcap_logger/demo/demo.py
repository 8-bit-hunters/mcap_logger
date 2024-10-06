import time

from mcap_logger.demo.sensor_data_pb2 import SensorData

from mcap_logger.mcap_logger import get_logger

SENSOR_DATA = [
    {"temp": 10, "humid": 70},
    {"temp": 5, "humid": 75},
    {"temp": 2, "humid": 78},
    {"temp": -1, "humid": 80},
    {"temp": 3, "humid": 79},
]

logger = get_logger(__name__)

def demo_logging():
    print("Running logging demo...")
    logger.info("Fetching sensor data")
    for i, sensor_data in enumerate(SENSOR_DATA):
        logger.debug(f"reading sensor... {i}")
        time.sleep(0.5)
        temperature = sensor_data["temp"]
        humidity = sensor_data["humid"]

        sensor_message = SensorData(temperature=temperature, humidity=humidity)
        logger.topic("/sensor_data").write(sensor_message)

        if temperature < 0:
            logger.warning("Temperature is below zero!")

    logger.error("This is an error")
    logger.fatal("And this is a fatal error")
    logger.info("Finished")
    print("Logging finished")

if __name__ == "__main__":
    demo_logging()
