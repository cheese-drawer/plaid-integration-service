# standard library imports
import logging
import os
from typing import Any, List, Dict, TypedDict

# third party imports
import amqp_worker as worker
import db_wrapper as db

# internal dependencies
from start_server import Runner

# application logic
from models import ExampleItem, ExampleItemData, SimpleData
import lib


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
# DATABASE SETUP
#

db_connection_params = db.ConnectionParameters(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'postgres'),
    password=os.getenv('DB_PASS', 'postgres'),
    database=os.getenv('DB_NAME', 'postgres'))

# init db & connect
database = db.Client(db_connection_params)


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
response_and_request = worker.RPCWorker(broker_connection_params)
service_to_service = worker.QueueWorker(broker_connection_params)

@response_and_request.route('balance_service-balance')
async def model_route(query: str)-> str:
    pass

@response_and_request.route('balance_service-transactions_all')
async def model_route(query: str)-> List:
    pass

@response_and_request.route('transaction_service-transaction_details')
async def model_route(query: str)-> str:
    pass
    
@response_and_request.route('transaction_service-transaction_details')
async def model_route(query: str)-> str:
    pass

@response_and_request.route('budget_service-goal_all')
async def model_route(query: str)-> str:
    pass

@response_and_request.route('budget_service-goal')
async def model_route(query: str)-> str:
    pass

@response_and_request.route('budget_service-goal_details')
async def model_route(query: str)-> str:
    pass

@response_and_request.route('budget_service-bucket_all')
async def model_route(query: str)-> str:
    pass

@response_and_request.route('budget_service-bucket')
async def model_route(query: str)-> str:
    pass

@response_and_request.route('budget_service-expense_all')
async def model_route(query: str)-> str:
    pass

@response_and_request.route('budget_service-expense')
async def model_route(query: str)-> str:
    pass