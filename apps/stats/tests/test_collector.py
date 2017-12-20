# -*- coding: utf-8 -*-
import os

from django.test import TestCase
from django.conf import settings

from stats.collector import ServerConfig, IntranetStatsCollector, ClientConfig, ClientAlert
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
    stats = {'mem_active': 6815825920.0,
             'mem_total': 16042115072.0,
             'mem_used': 2465234944.0,
             'mem_shared': 152330240.0,
             'mem_inactive': 1883254784.0,
             'mem_free': 6828122112.0,
             'mem_buffers': 297345024.0,
             'mem_percent': 0.30,
             'os_name': 'linux2',
             'mem_available': 13165068288.0,
             'host_name': 'fake_host',
             'cpu_percent': 0.50,
             'mem_cached': 6451412992.0,
             'total_uptime': 1250}
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

        self.assertEqual(stats.os_name, "linux2")
        self.assertEqual(stats.total_uptime, 1250)
        self.assertEqual(stats.mem_usage, 0.30)
        self.assertEqual(stats.cpu_usage, 0.50)

    def test_get_alerts(self):
        stats = {'mem_active': 6815825920.0,
                 'mem_total': 16042115072.0,
                 'mem_used': 2465234944.0,
                 'mem_shared': 152330240.0,
                 'mem_inactive': 1883254784.0,
                 'mem_free': 6828122112.0,
                 'mem_buffers': 297345024.0,
                 'mem_percent': 0.50,
                 'os_name': 'linux2',
                 'mem_available': 13165068288.0,
                 'host_name': 'fake_host',
                 'cpu_percent': 0.70,
                 'mem_cached': 6451412992.0}

        client_cfg = ClientConfig("127.0.0.1", 22, "username", "password", "email")
        client_cfg.alerts.append(ClientAlert("cpu", 0.60))
        client_cfg.alerts.append(ClientAlert("memory", 0.40))
        alerts = self.collector.get_alerts(client_cfg, stats)
        self.assertEqual(len(alerts), 2)

        client_cfg.alerts.clear()
        client_cfg.alerts.append(ClientAlert("cpu", 0.40))
        client_cfg.alerts.append(ClientAlert("memory", 0.55))
        alerts = self.collector.get_alerts(client_cfg, stats)
        self.assertEqual(len(alerts), 1)

        client_cfg.alerts.clear()
        client_cfg.alerts.append(ClientAlert("cpu", 0.80))
        client_cfg.alerts.append(ClientAlert("memory", 0.80))
        alerts = self.collector.get_alerts(client_cfg, stats)
        self.assertEqual(len(alerts), 0)
