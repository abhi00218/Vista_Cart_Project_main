from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals  # Replace 'yourapp' with the name of your app
