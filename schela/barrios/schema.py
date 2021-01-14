import graphene
from graphene_django import DjangoObjectType
from barrios.models import Cervecera
from django.contrib.auth.models import User


class CerveceraType(DjangoObjectType):
    class Meta:
        model = Cervecera


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    cervecera = graphene.List(CerveceraType)
    user = graphene.List(UserType)

    def resolve_cervecera(self, info, **kwargs):
        return Cervecera.objects.all()

    def resolve_user(self, info, **kwargs):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    def mutate(self, info, username, password):
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class CreateCervecera(graphene.Mutation):
    cervecera = graphene.Field(CerveceraType)

    class Arguments:
        cerveceraname = graphene.String()

    def mutate(self, info,  cerveceraname):
        cervecera = Cervecera.objects.create(cerveceraname=cerveceraname)
        return CreateCervecera(cerveceraname=cervecera)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_cervecera = CreateCervecera.Field()
