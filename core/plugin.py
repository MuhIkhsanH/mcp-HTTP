from abc import ABC, abstractmethod


class Plugin(ABC):

    @abstractmethod
    def register_tools(self, mcp):
        pass