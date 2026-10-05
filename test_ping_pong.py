import unittest
import importlib
import sys


import ping_pong


self.ping_pong = importlib.import_module('ping_pong')

#######################################################################


class TestPingPong(unittest.TestCase):
    def setUp(self):
        # Dynamically import the ping_pong module
        self.ping_pong = importlib.import_module('ping_pong')

    def test_ping(self):
        result = self.ping_pong.ping()
        self.assertEqual(result, "pong")

    def test_pong(self):
        result = self.ping_pong.pong()
        self.assertEqual(result, "ping")


#######################################################################

"""
Módulo ping_pong.py
Implementação das funções finalizadas após a fase de refatoração no TDD Ping-Pong.
"""


def ping() -> str:
    """Retorna 'pong' ao receber o estímulo de ping."""
    return "pong"


def pong() -> str:
    """Retorna 'ping' ao receber o estímulo de pong."""
    return "ping"