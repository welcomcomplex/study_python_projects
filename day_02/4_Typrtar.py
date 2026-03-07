from typing import List, Protocol, TypeVar, Generic, protocol

T = TypeVar('T')

def backwards(lst: List[T]) -> List[T]:
    return lst[:]

class Stack(Generic[T]):
    def __init__(self,value: T):
        self._items: List[T] = [value]
        def push(self,item: T) -> List[T]:
            self._items.append(item)
            return self._items
        def pop(self) -> T:
            return self._items.pop()
        def is_empty(self) -> bool:
            return not self._items
stack = Stack[int](5)


class Drawable(Protocol):
    def draw(self) -> None: ...
class Circle:
    def draw(self) -> None:
        print("Drawing a circle")
def render(d : Drawable) -> None:
    d.draw()
render(Circle())