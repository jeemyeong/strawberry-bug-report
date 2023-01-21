from typing import Annotated

import strawberry

from ..models import Slot as SlotModel
from ..models import Show as ShowModel

Show = Annotated["Show", strawberry.lazy(".types.show")]
Slot = Annotated["Slot", strawberry.lazy(".types.slot")]


@strawberry.type
class Query:
    @strawberry.field
    def slot(self) -> Slot:
        return SlotModel.objects.get(id=1)

    @strawberry.field
    def show(self) -> Show:
        return ShowModel.objects.get(id=1)

schema = strawberry.Schema(query=Query)
