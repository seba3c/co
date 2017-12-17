import logging

from django.core.management.base import BaseCommand
from apps.stats.collector import IntranetStatsCollector


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Collect statistics from Intranet'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        logger.info("Running command: 'collect_stats'...")
        IntranetStatsCollector().collect_stats()
