"""Tests for endpoints on the Request & Response API."""
# pylint: disable=missing-function-docstring

import unittest

# pylint thinks `test. ...` is a standard import for some reason
# pylint: disable=wrong-import-order
from test.integration.helpers.connection import connect, Connection
from test.integration.helpers.queue_client import Client
# use TimeLimitedTestCase instead of unittest.TestCase
# it adds a time limit for a test (5 seconds by default), so
# the test will fail for timing out instead of hanging forever
# if you try to test a route that doesn't exist
from test.integration.helpers.timeout import TimeLimitedTestCase


connection: Connection
client: Client


def setUpModule() -> None:
    """Establish connection & create AMQP client."""
    # pylint: disable=global-statement
    # pylint: disable=invalid-name
    global connection
    global client

    connection, channel = connect(
        host='localhost',
        port=8672,
        user='test',
        password='pass'
    )
    client = Client(channel)


def tearDownModule() -> None:
    """Close connection."""
    # pylint: disable=global-statement
    # pylint: disable=invalid-name
    global connection
    connection.close()


# You'll probably want to rename this to something that names the route
# under test. For example, if the route under test is plaid.request_token,
# maybe the test case class should be TestRoutePlaidRequestToken.
class TestRouteName(TimeLimitedTestCase):
    pass


if __name__ == '__main__':
    unittest.main()
