from WirelessSensorNetwork.forms import SearchForm


def global_vars(request):
    context = dict()
    search_form = SearchForm(request.GET or None)
    context['search_form'] = search_form
    context['user'] = request.session.get('user', None)
    return context