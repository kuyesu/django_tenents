from django.shortcuts import render
from .models import Tenant, Members
from .utitilities import get_host_name, get_tenant
# Create your views here.


def our_team(request):
    tenant = get_tenant(request)
    member = Members.object.filter(tenant=tenant)

    return (request, "our_team.html", {'tenant': tenant, 'member': member})