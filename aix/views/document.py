import json
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.document import DocumentForm
from aix.models.entity import EntityModel
from aix.models.document import DocumentModel
from aix.views.mixins import LoginRequiredMixIn

class DocumentModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/document.html'
    context_object_name = 'documents'
    PAGE_TITLE = _('Document List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DocumentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class DocumentModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/document.html'
    PAGE_TITLE = _('Create New Document')
    form_class = DocumentForm
    context_object_name = 'document'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    upload_file = None

    def get_queryset(self):
        return DocumentForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if self.upload_file == 'wo':
            reverse_url = reverse('aix:work-order-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_pk': self.kwargs['work_order_pk']
                        })
        elif self.upload_file == 'task':
            reverse_url = reverse('aix:work-order-task-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_task_pk': self.kwargs['work_order_task_pk']
                        })
        elif self.upload_file == 'activity':
            reverse_url = reverse('aix:work-order-activity-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                        })
        return reverse_url

    def form_valid(self, form):
        document_model: DocumentModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        document_model.entity = entity_model
        # document_model.entity = entity_model
        # document_model.work_order_id = self.kwargs['work_order_pk']
        document_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        # files = self.request.FILES.getlist('files[]', None)
        # print("x text x", files)
        # self.upload_files
        request = self.request
        # if request.method == 'POST':
        files = request.FILES.getlist('files[]', None)
        # print("x text x", request.method, "Mk", files.count)
        # document_model.save()
        for f in files:
            # print(f.name, self.upload_file)
            # self.handle_uploaded_file(f)
            with open(f.name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            file_type = f.content_type.split('/')[0]
            charset = f.content_type.split('/')[-1]
            document = DocumentModel.objects.create(name=document_model.name,
                name_on_file=f'/media/{f.name}',
                extension=f.name.split('.')[-1],
                size=f.size,
                mime_type=f.content_type, 
                # charset=charset,
                entity=entity_model,
                # self.kwargs['work_order_pk'] if upload_file == 'wo' else '',
                doc_status_id=document_model.doc_status_id,
                doc_type_id=document_model.doc_type_id,
                description=document_model.description
                )
            # print(f.size, file_type, f.name.split('.')[-1])
            if self.upload_file == 'wo':
                document.work_order_id = self.kwargs['work_order_pk']
            elif self.upload_file == 'task':
                document.task_id = self.kwargs['work_order_task_pk']
            elif self.upload_file == 'activity':
                document.activity_id = self.kwargs['work_order_activity_pk']
                # print('self')
            document.save()
            # print(file_type, 'dxd')
        # document_model.save()
        return super().form_valid(form)


class DocumentModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/document.html'
    PAGE_TITLE = _('Document Update')
    context_object_name = 'document'
    form_class = DocumentForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'document_pk'
    slug_field = 'uuid'
    upload_file = None

    def get_queryset(self):
        return DocumentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if self.upload_file == 'wo':
            reverse_url = reverse('aix:work-order-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_pk': self.kwargs['work_order_pk']
                        })
        elif self.upload_file == 'task':
            reverse_url = reverse('aix:work-order-task-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_task_pk': self.kwargs['work_order_task_pk']
                        })
        elif self.upload_file == 'activity':
            reverse_url = reverse('aix:work-order-activity-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                        })
        return reverse_url
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        document_model: DocumentModel = self.get_object()
        if document_model.work_order_id:
            self.upload_file = 'wo'
            self.kwargs['work_order_pk'] = document_model.work_order_id
        elif document_model.task_id:
            self.upload_file = 'task'
            self.kwargs['work_order_task_pk'] = document_model.task_id
        elif document_model.activity_id:
            self.upload_file = 'activity'
            self.kwargs['work_order_activity_pk'] = document_model.activity_id
        context['upload'] = self.upload_file
        return context

    def form_valid(self, form):
        document_model: DocumentModel = self.get_object()
        if document_model.work_order_id:
            self.upload_file = 'wo'
            self.kwargs['work_order_pk'] = document_model.work_order_id
        elif document_model.task_id:
            self.upload_file = 'task'
            self.kwargs['work_order_task_pk'] = document_model.task_id
        elif document_model.activity_id:
            self.upload_file = 'activity'
            self.kwargs['work_order_activity_pk'] = document_model.activity_id
        form.save()
        return super().form_valid(form) 

class DocumentModelUploadView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/document.html'
    PAGE_TITLE = _('Upload Document')
    form_class = DocumentForm
    context_object_name = 'document'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    doc_files = None
    upload_file = None

    def get_queryset(self):
        return DocumentForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:case-file-detail',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_pk': self.kwargs['work_order_pk']
                       })

    def form_valid(self, form):
        document_model: DocumentModel = form.save(commit=False)
        # if request.method == 'POST':
        files = self.request.FILES.getlist('files')
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        document_model.entity = entity_model
        document_model.work_order = self.kwargs['work_order_pk']
        # document_model.files  = doc_files
        # document_model.save()
        return super().form_valid(form)

    # @ensure_csrf_cookie
    def upload_files(request):
        if request.method == "GET":
            return render(request, 'files_upload.html', )
        if request.method == 'POST':
            files = request.FILES.getlist('files[]', None)
            docs = 9
            for f in files:
                handle_uploaded_file(f)
            doc_files = json.dumps(files)
            print(doc_files)
            # return JsonResponse({'msg':'<span style="color: green;">File successfully uploaded</span>'})
        # else:
        #     return render(request, 'files_upload.html', )

    def handle_uploaded_file(f):
        with open(f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)