from .models import Tenant


def get_host_name(request):
    return request.get_host().split(':')[0].lower()

def get_tenant(request):
    host_name = get_host_name(request)
    subdomain = host_name.split('.')[0]

    return Tenant.objects.filter(subdomain=subdomain).first()
    

