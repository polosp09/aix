from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.job import JobForm
from aix.models.entity import EntityModel
from aix.models.job import JobModel
from aix.views.mixins import LoginRequiredMixIn


class JobModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/hr/job.html'
    context_object_name = 'jobs'
    PAGE_TITLE = _('Job List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return JobModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class JobModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/hr/job.html'
    PAGE_TITLE = _('Create New Job')
    form_class = JobForm
    context_object_name = 'job'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return JobForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:job-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        job_model: JobModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        job_model.entity = entity_model
        job_model.save()
        return super().form_valid(form)


class JobModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/hr/job.html'
    PAGE_TITLE = _('Job Update')
    context_object_name = 'job'
    form_class = JobForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'job_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return JobModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:job-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 