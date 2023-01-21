from typing import Annotated, List, Optional

import strawberry

from ...models import Show as ShowModel

Slot = Annotated["Slot", strawberry.lazy(".slot")]

# maximum recursion depth exceeded while calling a Python object
Param = Annotated["Param", strawberry.lazy(".slot")]
# it was not raised when I used the following line instead of the above line
# Param = strawberry.LazyType["Param", ".slot"]

@strawberry.django.type(ShowModel)
class Show:
    id: int

    @strawberry.field
    def slots(self: ShowModel, param: Optional[Param]) -> List[Slot]:
        queryset = self.slots.all()
        return queryset
