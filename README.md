# GMC Prometheus exporter

A basic prometheus exporter for GMC device.
Values are exported as CPM - a [radioactivity measurement](https://en.wikipedia.org/wiki/Counts_per_minute).


# Usage

```
usage: gqgmc-prometheus-exporter [-h] [-p PORT] [-b BAUDRATE] [-l ADDR]
                                 [-d DELAY] [-P SERIAL_PORT]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port for prometheus exporter to listen on
                        (HTTP)default to 9012
  -b BAUDRATE, --baudrate BAUDRATE
                        baudrate for GMC device. Default value is 57600
  -l ADDR, --addr ADDR  IP for prometheus exporter to listen on (HTTP) Default
                        value is 'localhost'
  -d DELAY, --delay DELAY
                        wait this amount of seconds before polling device for
                        cpm value Default value is 5
  -P SERIAL_PORT, --serial-port SERIAL_PORT
                        Serial PortDefault value is '/dev/ttyUSB0'
```

see [GQ-RFC1201](https://www.gqelectronicsllc.com/download/GQ-RFC1201.txt) for more information about GQ's serial protocol

Tested with GMC300EPLUS (v4).
