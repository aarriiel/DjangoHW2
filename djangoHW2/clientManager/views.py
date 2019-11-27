from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import Client, Manager, ManagerForm
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from .onlineManager import onlineManager


# Create your views here.
class managerSignin(TemplateView):
    template_name = 'managerSignin.html'

    def get(self, request):
        form = ManagerForm()
        alert = ''
        userList = Manager.objects.all().order_by('username')
        return render(request, self.template_name, locals())

    def post(self, request):
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect('/clientSearch/')

        try:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            manager = Manager.objects.get(username=username, password=password)
            onlineManager.add(manager)
            print(onlineManager.get())
            return HttpResponseRedirect('/clientSearch/')

        except ObjectDoesNotExist:
            return render_to_response(self.template_name)


class managerSignUp(TemplateView):
    template_name = 'managerSignup.html'

    def get(self, request):
        form = ManagerForm()
        userList = Manager.objects.all().order_by('username')
        return render(request, self.template_name, locals())

    def post(self, request):
        form = ManagerForm(request.POST)
        if form.is_valid():
            Manager.objects.create(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                department=form.cleaned_data.get('department')
            )
            return render(request, 'signUpSuccess.html', locals())
        return render(request, self.template_name, locals())


class clientSearch(TemplateView):
    template_name = 'clientSearch.html'

    def get(self, request):
        manager = onlineManager.get()
        context = {
            'manager': manager
        }

        return render(request, self.template_name, context)


class add(TemplateView):
    template_name = 'add.html'

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        try:
            name = request.POST.get('name', '')
            client = Client.objects.get(name=name)
            return render_to_response(self.template_name)

        except ObjectDoesNotExist:
            Client.objects.create(
                name=request.POST.get('name', ''),
                sexual=request.POST.get('sexual', ''),
                birthday=request.POST.get('birthday', ''),
                email=request.POST.get('email', ''),
                phone=request.POST.get('phone', ''),
                department=request.POST.get('department', ''),
                description=request.POST.get('description', '')
            )
            context = {
                'action': 'ADD',
            }
            return render(request, 'result.html', context)


class delete(TemplateView):
    template_name = 'delete.html'

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        try:
            clientName = request.POST.get('name', '')
            client = Client.objects.get(name=clientName)
            client.delete()
            context = {
                'action': 'DELETE',
            }
            return render(request, 'result.html', context)

        except ObjectDoesNotExist:
            return render_to_response(self.template_name)


class search(TemplateView):
    template_name = 'search.html'

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        try:
            clientName = request.POST.get('name', '')
            client = Client.objects.get(name=clientName)
            print(client)
            context = {
                'action': 'SEARCH',
                'client': client
            }
            return render(request, 'searchResult.html', context)

        except ObjectDoesNotExist:
            return render_to_response(self.template_name)


class update(TemplateView):
    template_name = 'update.html'

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        try:
            name = request.POST.get('name', '')
            print(name)
            client = Client.objects.get(name=name)
            client.sexual = request.POST.get('sexual', '')
            client.birthday = request.POST.get('birthday', '')
            client.email = request.POST.get('email', '')
            client.phone = request.POST.get('phone', '')
            client.department = request.POST.get('department', '')
            client.description = request.POST.get('description', '')
            client.save()
            context = {
                'action': 'UPDATE',
            }
            return render(request, 'result.html', context)

        except ObjectDoesNotExist:
            return render_to_response(self.template_name)
