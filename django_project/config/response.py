from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect, resolve_url


class Action_To_Serializer(serializers.Serializer):
    action = serializers.CharField()
    url = serializers.CharField()
    params = serializers.JSONField()


class Action:
    def __init__(self,  action: str, url: str, params={}):
        self.action = action
        self.url = url
        self.params = params

    def data(action, url, params={}):
        return Action_To_Serializer(Action(action, resolve_url(url), params)).data

    def data_dt(action, url, pk, params={}):
        return Action_To_Serializer(Action(action, resolve_url(url, pk), params)).data


def APIResponse(operations=None, data=None):
    response = {
    }
    response['operations'] = operations if operations else None
    response['data'] = data if data else None
    return response


def set_receive(request, content_type):
    receive = request.data if content_type == 'application/json' else request.POST
    return receive