from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from WirelessSensorNetwork.blockchain import Blockchain
from .forms import SearchForm, LoginForm, TransactionForm


# -------------------------- Home View --------------------------
class Home(View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        if not request.session.get('user', False):
            return redirect('wsn:login')

        context = dict()
        search_form = SearchForm(request.GET or None)
        if search_form.is_valid():
            search_keyword = search_form.cleaned_data['search']
            context['search'] = search_keyword
            try:
                context['details'] = Blockchain.get_node_details(search_keyword)
            except:
                pass
        else:
            context['search'] = ''
        context['transactions'] = Blockchain.get_all_transaction()
        context['transaction_form'] = TransactionForm()
        return render(request, 'WirelessSensorNetwork/index.html', context)

    def post(self, request):
        if not request.session.get('user', False):
            return redirect('wsn:login')
        form = TransactionForm(request.POST or None)
        node_cluster = request.session.get('user').get('cluster')
        if form.is_valid():
            Blockchain.get_cluster_header(node_cluster)


# -------------------------- Login View --------------------------
class Login(View):

    def get(self, request, *args, **kwargs):
        if request.session.get('user', False):
            return redirect('wsn:home')

        context = dict()
        context["login_form"] = LoginForm()
        return render(request, "WirelessSensorNetwork/login.html", context)

    def post(self, request, *args, **kwargs):
        if request.session.get('user', False):
            return redirect('wsn:home')

        context = dict()
        form = LoginForm(request.POST or None)
        if form.is_valid():
            try:
                # Check if connecting user is the sink node
                is_sink_node = Blockchain.check_sink_node(form.cleaned_data['address'])
                print(f'is sink node: {is_sink_node}')
                if is_sink_node:
                    request.session['user'] = Blockchain.get_sink_node()
                else:
                    node_details = Blockchain.get_node_details(form.cleaned_data['address'])
                    request.session['user'] = node_details
                redirect_url = request.POST.get("next", reverse("wsn:home"))
                return redirect(redirect_url)
            except Exception as ex:
                print(ex)
                print('Invalid login information!')
        # Display login with error login message
        messages.error(request, "Invalid address, please check your informations")
        context["login_form"] = form
        return render(request, "WirelessSensorNetwork/login.html", context)

# -------------------------- Logout View --------------------------
class Logout(View):

    # Get method not supported
    def get(self, request, *args, **kwargs):
        return redirect('wsn:home')

    def post(self, request, *args, **kwargs):
        if not request.session.get('user', False):
            return redirect('wsn:login')

        del request.session['user']
        return redirect("wsn:login")

# -------------------------- Profile View --------------------------
class Profile(View):

    # Get method not supported
    def get(self, request, *args, **kwargs):
        if not request.session.get('user', False):
            return redirect('wsn:login')
        context = dict()
        user = request.session['user']
        context['transactions'] = Blockchain.get_node_transactions(user.get('address'))
        return render(request, 'WirelessSensorNetwork/profile.html', context)

    def post(self, request, *args, **kwargs):
        if not request.session.get('user', False):
            return redirect('wsn:login')
        return render(request, 'WirelessSensorNetwork/profile.html')