from typing import Annotated, List

import strawberry

from ...models import Slot as SlotModel

Show = Annotated["Show", strawberry.lazy(".show")]


@strawberry.input
class Param:
    id: int


@strawberry.django.type(SlotModel)
class Slot:
    id: int

    @strawberry.field
    def show(self) -> List[Show]:
        return self.show
