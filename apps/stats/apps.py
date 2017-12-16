from django.apps import AppConfig


class StatsConfig(AppConfig):
    name = 'stats'
    verbose_name = u'Machine Stats'

    def ready(self):
        import stats.signals
