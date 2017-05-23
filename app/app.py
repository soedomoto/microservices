from flask import Flask
from flask_consulate import Consul

def get_ip_address(ifname):
    import socket
    import fcntl
    import struct

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


ip = get_ip_address('eth0')
app = Flask(__name__)


@app.route('/healthcheck')
def health_check():
    """
    This function is used to say current status to the Consul.
    Format: https://www.consul.io/docs/agent/checks.html

    :return: Empty response with status 200, 429 or 500
    """
    # TODO: implement any other checking logic.
    return '', 200


@app.route('/')
def home():
    """
    This function is used to say current status to the Consul.
    Format: https://www.consul.io/docs/agent/checks.html

    :return: Empty response with status 200, 429 or 500
    """
    # TODO: implement any other checking logic.
    return 'Works', 200


# Consul
# This extension should be the first one if enabled:
consul = Consul(app=app, consul_host='consul', consul_port=8500)
# Fetch the conviguration:
# consul.apply_remote_config(namespace='mynamespace/')
# Register Consul service:
consul.register_service(
    name='account',
    interval='10s',
    tags=['webserver', ],
    address=ip,
    port=80,
    httpcheck='http://{}/healthcheck'.format(ip)
)

app.run(host='0.0.0.0', port=80)
