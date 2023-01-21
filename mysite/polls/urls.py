#  Copyright (c) 2022 GigFinesse, Inc.
#  All Rights Reserved
#  Proprietary and confidential
#  Unauthorized copying of this file via any medium is strictly prohibited

from django.conf import settings
from django.urls import path
from strawberry.django.views import GraphQLView

from .graphql import schema

app_name = "venue_api"
urlpatterns = [
    path("graphql", GraphQLView.as_view(schema=schema.schema, graphiql=settings.DEBUG)),
]
