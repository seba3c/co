# -*- coding: utf-8 -*-
import os
import logging
import xmltodict

from django.conf import settings
from stats.models import IntranetMachine, IntranetMachineStats


logger = logging.getLogger(__name__)


class ClientAlert():

    def __init__(self, ttype, limit):
        self.type = ttype
        self.limit = float(limit)


class ClientConfig():
    """
    Object representation of each client config from xml file
    """

    def __init__(self, ip, port, username, password, email):
        self.ip = ip
        self.port = int(port)
        self.username = username
        self.password = password
        self.email = email
        self.alerts = []

    def __repr__(self):
        return "ClientConfig(IP: %s PORT: %d email: %s alerts: %d)" % (self.ip, self.port,
                                                                       self.email,
                                                                       len(self.alerts))


class ServerConfig():
    """
    Server Config Object representation. Load a list of clients from a given XML file.
    """

    def __init__(self, filename=None):
        self.filename = filename
        self.doc = {"clients": {"client": []}}

    def _parse_file(self):
        if self.filename is not None:
            with open(self.filename) as fd:
                self.doc = xmltodict.parse(fd.read())

    def get_clients(self):
        clients = []
        self._parse_file()
        client_data = self.doc["clients"]['client']
        for c in client_data:
            cfg = ClientConfig(c['@ip'], c['@port'],
                               c['@username'], c['@password'],
                               c['@mail'])
            alerts = c["alert"]
            for a in alerts:
                cfg_alert = ClientAlert(a["@type"], a["@limit"])
                cfg.alerts.append(cfg_alert)
            clients.append(cfg)
        return clients


class IntranetStatsCollector():
    """
    This class performs the following actions:
    * Loads Intranet clients configuration from XML file.
    * Gets remote stats from each client in the Intranet
    * Save remote stats locally
    * Send alerts by email to each client email if necessary
    """

    default_filename = os.path.join(settings.PROJECT_ROOT_DIR, "config", "clients_config.xml")

    def __init__(self, filename=None):
        self.filename = self.default_filename if filename is None else filename
        self.config_loader = ServerConfig(self.filename)

    def get_stats(self, client):
        logger.info("Getting remote stats from %s..." % client.ip)
        return {"cpu": {}, "mem": {}}

    def save_stats(self, client, stats):
        logger.info("Saving remote stats of %s host..." % client.ip)
        i_machine, _ = IntranetMachine.objects.get_or_create(ip=client.ip, port=client.port)
        stats_data = {"intranet_machine": i_machine,
                      "os_name": stats.get("os_name", "Unknown"),
                      "mem_usage": stats["mem"].get("percent", 0.0),
                      "cpu_usage": stats["cpu"].get("percent", 0.0),
                      "total_uptime": stats.get("total_uptime", 0.0),
                      }
        IntranetMachineStats.objects.create(**stats_data)

    def send_alerts(self, client, stats):
        logger.info("Sending alerts stats of %s host..." % client.ip)
        pass

    def collect_stats(self):
        logger.info("Collecting stats from Intranet...")
        clients = self.config_loader.get_clients()
        # TODO: this can be parallelized to improve performance
        for client in clients:
            stats = self.get_stats(client)
            self.save_stats(client, stats)
            self.send_alerts(client, stats)
