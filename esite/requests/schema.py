from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import (
    login_required,
    permission_required,
    staff_member_required,
    superuser_required,
)

from esite.requests.models import Request

# Create your registration related graphql schemes here.


class RequestType(DjangoObjectType):
    class Meta:
        model = Request


class CreateRequest(graphene.Mutation):
    r = graphene.Field(graphene.String, token=graphene.String(required=False))

    class Arguments:
        title = graphene.String(required=True)
        link = graphene.String(required=True)
        name = graphene.String(required=True)
        _type = graphene.String(required=True)
        email = graphene.String(required=False)
        phone = graphene.String(required=False)
        note = graphene.String(required=False)
        token = graphene.String(required=False)

    @login_required
    def mutate(self, info, title, link, name, _type, **_kwargs):
        email = _kwargs.get('email', None)
        phone = _kwargs.get('phone', None)
        note = _kwargs.get('note', None)
        r = Request(title=title, link=link, name=name, _type=_type, email=email, phone=phone, note=note)
        r.save()

        return CreateRequest(r.title)


class Mutation(graphene.ObjectType):
    create_request = CreateRequest.Field()


class Query(graphene.ObjectType):
    requests = graphene.List(RequestType, token=graphene.String(required=False))

    @superuser_required
    def resolve_requests(self, info, **_kwargs):
        return Request.objects.all()