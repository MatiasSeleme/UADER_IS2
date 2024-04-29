from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class NumeroPrimo(AbstractHandler):
    def handle(self, request: Any) -> float:
        c = 0
        for i in range(1, request + 1):
            if request % i == 0:
                c += 1

        if c == 2:
            return f"Numero Primo: {request} es un numero primo\n"
        else:
            return super().handle(request)


class NumerosPares(AbstractHandler):
    def handle(self, request: Any) -> float:
        if request % 2 == 0 :
            return f"Numero Par: {request} es un numero par\n"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for i in range(100):
        
        result = handler.handle(i)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {i}  No consumido\n", end="")


if __name__ == "__main__":
    primo = NumeroPrimo()
    par = NumerosPares()


    primo.set_next(par)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Primos > Par")
    client_code(primo)

    client_code(par)
