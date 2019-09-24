from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.db.models import Q

from rest_framework import viewsets

from python_test.models import Client
from python_test.forms import ClientForm
from python_test.utils import ApiViewSetMixin
from python_test.serializers import ClientSerializer


###################################################
###################################################
###### Views for bootstrap Kind of framework ######
###################################################
###################################################

class ClientCreateView(CreateView): 
	# In order to provide restricted 
	# access we can use mixins and extend them here 
	form_class = ClientForm
	template_name = "python_test/client_form.html"

	def get_success_url(self):
		# we can have a success url or redirtect url whatever we need, 
		# have made the same url as of now 
		return reverse_lazy('add_client_view')
	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['form_type'] = "CREATE"
		return ctx


class ClientEditView(UpdateView): 
	# In order to provide restricted 
	# access we can use mixins and extend them here 
	form_class = ClientForm
	model = Client
	template_name = "python_test/client_form.html"

	def get_success_url(self):
		# we can have a success url or redirtect url whatever we need, 
		# have made the same url as of now 
		return reverse_lazy('add_client_view')

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['form_type'] = "EDIT"
		return ctx


class ClientListView(ListView): 
	# In order to provide restricted 
	# access we can use mixins and extend them here 
	model = Client

	def get_template_names(self):
		return ["python_test/client_list.html"]

	def get_queryset(self):
		search_text = self.request.GET.get("search", None)
		order_by_text =  self.request.GET.get("order", None)
		if search_text:
			return Client.objects.filter(Q(name__iexact=search_text) | Q(email_address__iexact=search_text) | Q(phone_number__iexact=search_text) | Q(suburb__iexact=search_text))
		elif order_by_text:
			return Client.objects.all().order_by(order_by_text)
		else:
			return Client.objects.all()


###############################################################
###############################################################
###### Views for Advance frameworks like react & angular ######
###############################################################
###############################################################

class ClientViewSet(ApiViewSetMixin,viewsets.ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

	def get_queryset(self):
		search_text = self.request.GET.get("search", None)
		order_by_text =  self.request.GET.get("order", None)
		if search_text:
			return Client.objects.filter(Q(name__iexact=search_text) | Q(email_address__iexact=search_text) | Q(phone_number__iexact=search_text) | Q(suburb__iexact=search_text))
		elif order_by_text:
			return Client.objects.all().order_by(order_by_text)
		else:
			return Client.objects.all() 










