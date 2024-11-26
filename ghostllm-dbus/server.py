from dbus_fast.aio import MessageBus
from dbus_fast.constants import BusType
from dbus_fast.service import (ServiceInterface,
                               method, dbus_property, signal)
from dbus_fast import Variant, DBusError

from .constants import *
from .ollama import OllamaController

import asyncio

class _GhostLLMDBusInterface(ServiceInterface):

    def __init__(self):
        super().__init__(DBUS_ADDRESS_NAME)
        self.ollama = OllamaController()
    
    @method()
    def RewriteText(self, input_text: 's') -> 's':
        return self.ollama.chat(input_text)


class GhostLLMDBus():

    async def init(self):
        bus = await MessageBus(bus_type=BusType.SESSION).connect()
        interface = _GhostLLMDBusInterface()
        bus.export(DBUS_INTERFACE_NAME, interface)
        await bus.request_name(DBUS_ADDRESS_NAME)

        print(f"DBUS Service initialized at {DBUS_INTERFACE_NAME}")

        await bus.wait_for_disconnect()

    def listen(self):
        asyncio.run(self.init())
