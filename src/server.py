"""Service API definition."""

# standard library imports
import logging
import os

# third party imports
import amqp_worker as worker

# internal dependencies
from encoder import (
    json_gzip_rpc_factory,
    # json_gzip_queue_factory,
)
from start_server import Runner

#
# ENVIRONMENT
#


def get_mode() -> str:
    """Determine if running application in 'production' or 'development'.

    Uses `MODE` environment variable & falls back to 'development' if no
    variable exists. Requires mode to be set to either 'development' OR
    'production', raises an error if anything else is specified.
    """
    env = os.getenv('MODE', 'development')  # default to 'development'

    if env in ('development', 'production'):
        return env

    raise TypeError(
        'MODE must be either `production`, `development`, or unset '
        '(defaults to `development`)')


MODE = get_mode()


#
# LOGGING
#

LOGGER = logging.getLogger(__name__)
# NOTE: use this one for debugging, very verbose output
# logging.basicConfig(level=logging.DEBUG)
# NOTE: or use this one for production or development
# sets development logging based on MODE
logging.basicConfig(
    level=logging.INFO
    if MODE == 'development'
    else logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#
# WORKER SETUP
#

# get connection parameters from dotenv, or use defaults
broker_connection_params = worker.ConnectionParameters(
    host=os.getenv('BROKER_HOST', 'localhost'),
    port=int(os.getenv('BROKER_PORT', '5672')),
    user=os.getenv('BROKER_USER', 'guest'),
    password=os.getenv('BROKER_PASS', 'guest'))

# initialize Worker & assign to global variable
response_and_request = worker.RPCWorker(
    broker_connection_params,
    pattern_factory=json_gzip_rpc_factory)
# service_to_service = worker.QueueWorker(
#     broker_connection_params,
#     pattern_factory=json_gzip_queue_factory)


#
# WORKER ROUTES
#

# define routes here...


#
# RUN SERVICE
#

runner = Runner()

# register workers
runner.register_worker(response_and_request)
# runner.register_worker(service_to_service)

# Run all registered workers & database client
runner.run()
