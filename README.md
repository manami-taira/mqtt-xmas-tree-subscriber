# mqtt-xmas-tree-subscriber
Blink your Xmas tree via MQTT (Subscriber)

## Setup
- for Fedora ARM or Fedora

    $ sudo yum install python-rpi-gpio

    $ sudo yum install python-paho-mqtt

- for RaspbianOS

    $ sudo apt-get install python-rpi.gpio

    $ sudo pip install paho-mqtt

## Usage
1. Build your MQTT broker.
 - If you want to build by ansible. see also build_activemq_broker.yml
2. Modify mqtt_broker value in source code.
3. Connect LED with PIN#11(GPIO#17) and GND on your Raspberry Pi.
4. Execute tree_subscriber.py on your Raspberry Pi.

    $ python ./tree_subscriber.py

## for testing
tree_subscriber_stub.py didn't require GPIO
If you want to test about MQTT protocol. Please execute following command.

    $ python ./tree_subscriber_stub.py

And so if you want to test about MQTT publisher. Please execute following command on another terminal.

    $ python ./tree_publisher.py
