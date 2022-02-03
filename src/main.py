import argparse
import serial
from time import sleep
from prometheus_client import start_http_server, Gauge


def probe(port: str, baudrate: int):
    try:
        with serial.Serial(port, baudrate) as ser:
            ser.write(b'<GETCPM>>')
            m, l = ser.read(2)
            cpm_value = (m << 8) | l
            return cpm_value
    except serial.serialutil.SerialException as e:
        print(e)
        exit(1)

def main(args):
    g = Gauge('cpm_value', 'Counts per minute')
    start_http_server(args.port, addr=args.addr)
    print(f"HTTP server started on http://{args.addr}:{args.port}")
    while True:
        cpm_value = probe(args.serial_port, args.baudrate)
        g.set(cpm_value)
        print(cpm_value)
        sleep(args.delay)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument(
        '-p', '--port', required=False,
        help="port for prometheus exporter to listen on (HTTP)"
            "default to 9012",
        type=int, default=9012
    )
    p.add_argument(
        '-b', '--baudrate',
        help="baudrate for GMC device."
            " Default value is 57600",
        type=int, default=57600
    )
    p.add_argument(
        '-l', '--addr',
        help="IP for prometheus exporter to listen on (HTTP)"
            " Default value is 'localhost'",
        type=str, default="localhost"
    )
    p.add_argument(
        '-d', '--delay',
        help="wait this amount of seconds before"
             " polling device for cpm value "
             "Default value is 5",
        type=int, default=5
    )    
    p.add_argument(
        '-P', '--serial-port',
        help="Serial Port"
             "Default value is '/dev/ttyUSB0'",
        type=str, default="/dev/ttyUSB0"
    )    
    args = p.parse_args()
    main(args)
