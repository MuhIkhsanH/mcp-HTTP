from abc import ABC, abstractmethod


class TestPlugin(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    async def run(self, session):
        pass