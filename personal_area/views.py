from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from .forms import RegistrationUserForm, AddSkillsForm, AddHobbyForm, AddLanguageForm
from .models import Skills, Hobby, Language

User = get_user_model()


class RegistrationFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegistrationUserForm

    def post(self, request, *args, **kwargs):
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password_1'])
            user.save()
            login_user = authenticate(request, username=user.username, password=form.cleaned_data['password_1'])
            login(request, login_user)
            return redirect(reverse('personal_area:home'))
        return render(request, self.template_name, context={'form':form})


class HomeView(generic.ListView):
    model = User
    template_name = 'home.html'
    context_object_name = 'users'


class PersonalAreaView(generic.DetailView):
    model = User
    template_name = 'personal_area.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get(self, request, pk=None):
        return super().get(request, pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill_form'] = AddSkillsForm
        context['hobby_form'] = AddHobbyForm
        context['language_form'] = AddLanguageForm
        return context


class AddSkillsView(generic.CreateView):
    template_name = 'personal_area.html'
    form_class = AddSkillsForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            skill, created = Skills.objects.get_or_create(skill=form.cleaned_data['skills'])
            skill.user.add(request.user)
            return redirect('/personal_area/')
        return render(request, self.template_name, {'form': form})


class AddHobbyView(generic.CreateView):
    template_name = 'personal_area.html'
    form_class = AddHobbyForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            hobby, created = Hobby.objects.get_or_create(hobby=form.cleaned_data['hobby'])
            hobby.user.add(request.user)
            return redirect('/personal_area/')
        return render(request, self.template_name, {'form': form})


class AddLanguageView(generic.CreateView):
    template_name = 'personal_area.html'
    form_class = AddLanguageForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            language, created = Language.objects.get_or_create(language=form.cleaned_data['language'])
            language.user.add(request.user)
            return redirect('/personal_area/')
        return render(request, self.template_name, {'form': form})


class EditUserHobbyView(generic.UpdateView):
    model = Hobby

    def get(self, request, *args, **kwargs):
        hobby = self.get_object()
        request.user.user_hobby.remove(hobby)
        return redirect(reverse('personal_area:personal_area'))


class EditUserSkillsView(generic.UpdateView):
    model = Skills

    def get(self, request, *args, **kwargs):
        skill = self.get_object()
        request.user.user_skill.remove(skill)
        return redirect(reverse('personal_area:personal_area'))


class EditUserLanguagesView(generic.UpdateView):
    model = Language

    def get(self, request, *args, **kwargs):
        language = self.get_object()
        request.user.user_language.remove(language)
        return redirect(reverse('personal_area:personal_area'))


