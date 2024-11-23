# MCAP Logger 🧢

## Project description

This python package to provide a standardised, easy to import and use logging method.

The package is...

- a logger module that leverages the existing MCAP and Foxglove packages
- provides a plugin for standard Python loging

Links:

- [Documentation](https://8-bit-hunters.github.io/mcap_logger/)
- [PyPI package](https://pypi.org/project/mcap-logger/)

## Example usage

### Installing the library

```shell
pip install mcap-logger
```

### Creating a simple log

```python
import logging
from pathlib import Path

from mcap_logger.mcap_handler import McapHandler


def main():  # noqa: ANN201
    log_file = Path("hello.mcap")

    mcap_handler = McapHandler(log_file)
    mcap_handler.setLevel("DEBUG")

    logger = logging.getLogger("mcap_logger")
    logger.addHandler(mcap_handler)
    logger.setLevel("DEBUG")

    logger.info("Hello from mcap-logger-tutorial!")
```

### Log Protobuf data

> ℹ️ Protocol buffers are Google's language-neutral mechanism for serializing structured data. More info about it and
> its syntax: [Protocol Buffers](https://protobuf.dev/)

```python
from sensor_data_pb2 import SensorData
from mcap_logger.topic_logger import TopicLogger

log_file = Path("hello.mcap")
mcap_handler = McapHandler(log_file)
mcap_handler.setLevel("DEBUG")

logger = logging.getLogger("mcap_logger")
logger.addHandler(mcap_handler)
logger.setLevel("DEBUG")

# Log Protobuf data
sensor_message = SensorData(temperature=25, humidity=65)
TopicLogger("mcap_logger").topic("/sensor_data").write(sensor_message)

```

![](docs/assets/demo_log_in_foxglove.png)

## Call for Contributions

The MCAP-Logger project welcomes your expertise and enthusiasm!
