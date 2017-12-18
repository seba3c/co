# -*- coding: utf-8 -*-
import os

from django.test import TestCase
from django.conf import settings

from stats.collector import ServerConfig, IntranetStatsCollector
from unittest import mock
from stats.models import IntranetMachine


TEST_SERVER_CONFIG = os.path.join(settings.APPS_DIR, "stats", "tests", "test_clients_config.xml")


class ServerConfigLoaderTestCase(TestCase):

    def setUp(self):
        self.server_cfg1 = ServerConfig()
        self.server_cfg2 = ServerConfig(TEST_SERVER_CONFIG)

    def test_server_config_loader(self):
        self.assertEqual(self.server_cfg1.get_clients(), [])

        clients = self.server_cfg2.get_clients()
        self.assertEqual(len(clients), 2)

        client_cfg = clients[0]
        self.assertEqual(client_cfg.ip, "127.0.0.1")
        self.assertEqual(client_cfg.port, 22)
        self.assertEqual(client_cfg.username, "user")
        self.assertEqual(client_cfg.password, "password")
        self.assertEqual(client_cfg.email, "castanedacs@gmail.com")

        alerts = client_cfg.alerts

        self.assertEqual(len(alerts), 2)
        self.assertEqual(alerts[1].type, "cpu")
        self.assertEqual(alerts[1].limit, 0.20)


def get_fake_stats(instance, client):
    stats = {"os_name": "Linux",
             "total_uptime": 1250,
             "cpu": {"percent": 0.50},
             "mem": {"percent": 0.30}
             }
    return stats


class IntranetStatsCollectorTestCase(TestCase):

    def setUp(self):
        self.collector = IntranetStatsCollector(TEST_SERVER_CONFIG)

    @mock.patch('stats.collector.IntranetStatsCollector.get_stats', new=get_fake_stats)
    def test_save_stats(self):
        self.assertEqual(IntranetMachine.objects.count(), 0)
        self.collector.collect_stats()
        self.assertEqual(IntranetMachine.objects.count(), 2)

        i_machine = IntranetMachine.objects.get(ip="127.0.0.2", port=22)
        stats = i_machine.stats.first()

        self.assertEqual(stats.os_name, "Linux")
        self.assertEqual(stats.total_uptime, 1250)
        self.assertEqual(stats.mem_usage, 0.30)
        self.assertEqual(stats.cpu_usage, 0.50)
