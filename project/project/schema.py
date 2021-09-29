import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from notes.models import Note, UserPreferences, UserInfo, User

class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        fields = ('id', 'note_text', 'note_name', 'note_created')
        filter_fields = ['id', 'note_name']
        interfaces = (relay.Node, )

class UserPreferencesType(DjangoObjectType):
    class Meta:
        model = UserPreferences
        fields = ('id', 'note_color_preference', 'note_name_preference', 'user_info')
        filter_fields = ['id', 'note_color_preference', 'note_name_preference']
        interfaces = (relay.Node, )

class UserInfoType(DjangoObjectType):
    class Meta:
        model = UserInfo
        fields = ('id', 'user_preferences', 'user_mail', 'user_chosen_name', 'user')
        filter_fields = ['id', 'user_mail', 'user_chosen_name']
        interfaces = (relay.Node, )

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'user_info')
        filter_fields = ['id']
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    note = relay.Node.Field(NoteType)
    all_notes = DjangoFilterConnectionField(NoteType)

    user_preferences = relay.Node.Field(UserPreferencesType)
    all_user_preferences = DjangoFilterConnectionField(UserPreferencesType)

    user_info = relay.Node.Field(UserInfoType)
    all_user_info = DjangoFilterConnectionField(UserInfoType)

    user = relay.Node.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)

schema = graphene.Schema(query=Query)