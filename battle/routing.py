from django.urls import re_path

from battle.consumers import BattleConsumer

websocket_urlpatterns = [
    re_path(r'api/one-to-one/(?P<code>\w+)', BattleConsumer.as_asgi())
]
