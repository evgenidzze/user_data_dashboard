from channels.generic.websocket import AsyncWebsocketConsumer
from .models import UserActions
from .serializers import UserActionsSerializer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions


class UsersConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = UserActions.objects.all()
    serializer_class = UserActionsSerializer
    permission_classes = (permissions.AllowAny,)

    async def connect(self, **kwargs):
        await self.model_change.subscribe()
        await super().connect()

    @model_observer(UserActions)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serializer(self, instance, action, **kwargs):
        return dict(data=UserActionsSerializer(instance=instance).data, action=action.value)
