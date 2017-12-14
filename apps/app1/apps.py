from django.apps import AppConfig


class AConfig(AppConfig):
    name = 'app1'
    verbose_name = u'1 App'

    def ready(self):
        import app1.signals
