import asyncio
from typing import Dict, List, Callable


class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event: str, callback: Callable):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    async def publish(self, event: str, **kwargs):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                if asyncio.iscoroutinefunction(callback):
                    await callback(**kwargs)
                else:
                    callback(**kwargs)


event_bus = EventBus()
