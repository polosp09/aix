import json
import simplejson
import requests
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.asset import AssetForm
from aix.models.entity import EntityModel
from aix.models.asset import AssetModel
from aix.models.work_order import WorkOrderModel
from aix.models.work_order_jobcard import WorkOrderJobcardModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader

fleetioapi = "https://secure.fleetio.com/api/"
wialonapi = "https://hst-api.wialon.com/wialon/ajax.html?svc=route/get_all_rounds"
wialontoken = '1a6a566a58c00cd04e8167b6e9b77ee10BF9F26687BD640F8AA466943DD076EFB1DD9CDD'
wialonpayload = {}
wialonheaders = {
    'Accept': 'application/json',
    'Authorization': wialontoken,
}
payload = {}
headers = {
    'Accept': 'application/json',
    'Authorization': 'Token 49fa2de23bd41a2e3b1f997cc212c1dbadb421ac',
    'Account-Token': '9914508da2'
}

class AssetModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/asset.html'
    context_object_name = 'assets'
    PAGE_TITLE = _('Asset List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }

    def get_queryset(self):
        qs = AssetModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                ).order_by('-updated')
        qs = qs.exclude(group_name='CNOOC')  
        qs = qs.exclude(group_name='SLB')   
        return qs


class AssetModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/asset.html'
    PAGE_TITLE = _('Create New Asset')
    form_class = AssetForm
    context_object_name = 'asset'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }

    def get_queryset(self):
        return AssetForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:asset-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        asset_model: AssetModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        asset_model.entity = entity_model
        asset_model.save()
        return super().form_valid(form)


class AssetModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/asset.html'
    PAGE_TITLE = _('Asset Update')
    context_object_name = 'asset'
    form_class = AssetForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }
    slug_url_kwarg = 'asset_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return AssetModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:asset-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PullFleetioAssetsView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/asset_fleetio.html'
    context_object_name = 'assets'
    PAGE_TITLE = _('Fleetio Asset List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }

    def get_queryset(self):
        qs = AssetModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                ).order_by('-updated')
        qs = qs.exclude(group_name='CNOOC')
        qs = qs.exclude(group_name='SLB')
        return qs

    def get_success_url(self):
        return reverse('aix:asset-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def get(self, request, entity_slug):
        self.request = request
        return super(PullFleetioAssetsView, self).get(request, self)

    def post(self, request, entity_slug,*args, **kwargs):
        self.request = request
        # url = "https://secure.fleetio.com/api/v1/equipment"
        # url = "https://secure.fleetio.com/api/v1/vehicles"

        # payload={}
        # headers = {
        # 'Accept': 'application/json',
        # 'Authorization': 'Token 49fa2de23bd41a2e3b1f997cc212c1dbadb421ac',
        # 'Account-Token': '9914508da2'
        # }

        # response = requests.request("GET", url, headers=headers, data=payload)
        # print(response.text)
        # url = "https://hst-api.wialon.com/"
        # url = "https://hst-api.wialon.com/wialon/ajax.html?svc=token/login"
        # url = 'https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&params={"spec":{"itemsType":"avl_unit","propName":"sys_user_creator","propValueMask":"948","sortType":"sys_name","propType":"creatortree"},"force":1,"flags":1,"from":0,"to":200}}],"flags":0}'
        # url = 'https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&params={spec:{itemsType:"avl_unit",propName:"sys_user_creator",propValueMask:948,sortType:"sys_name",propType:"creatortree"},force:1,flags:1,from:0,to:200}}],flags:0}&sid=098dddad2427cbd4a49162c3a5b44392'
        # url = "https://hst-api.wialon.com/wialon/ajax.html?svc=route/get_all_rounds"
        # url = 'https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_item&itemId=48&flags=1025&ssid=098dddad2427cbd4a49162c3a5b44392'
        url = 'https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_item&params={"id":27193164, "flags":1024}'
        svc = ''
        params = '?svc=core/search_item&itemId=48&flags=1025&ssid=09f8ebf64c10c54e21b0b2c5bdfab526'
        # payload = {
        #     'token': '1a6a566a58c00cd04e8167b6e9b77ee10D761553F17D2117B8DBE897F9561DCBFF8BAC5D',
        #     'sid': '09f8ebf64c10c54e21b0b2c5bdfab526',
        #     # 'svc': 'core/search_items&params={"id":27193164, "flags":1024}'
        # }
        # headers = {
        #     'Accept': 'application/json',
        #     'Authorization': '1a6a566a58c00cd04e8167b6e9b77ee10D761553F17D2117B8DBE897F9561DCBFF8BAC5D',
        #     # 'Authorization': 'd66b44f678ab4954a23ee10d61a89612',
        # }
        response = requests.request("POST", url, headers=wialonheaders, data=wialonpayload)
        print(response.text)
        
        return super(PullFleetioAssetsView, self).get(request, self)


class AssetModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'asset_pk'
    slug_field = 'uuid'
    context_object_name = 'asset'
    #template_name = 'aix/advanced/work_order/asset_detail.html'
    template_name = 'aix/app/operations/asset_details.html'
    extra_context = {
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        asset_model: AssetModel = self.object
        title = f'Asset: {asset_model.license_plate}'
        context['page_title'] = title
        context['header_title'] = title
        asset_qs = AssetModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )[0:10]

        wos_qs = WorkOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )[0:10]
        
        jcd_qs = WorkOrderJobcardModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                # work_order=work_order_model
            )

        wo_qs = jcd_qs.select_related('work_order')

        context['asset'] = self.object
        context['asset_qs'] = asset_qs
        context['wo_qs'] = wo_qs
        asset_digest = {}
        asset_digest['inspections'] = 0
        asset_digest['incidents'] = 0
        asset_digest['days_active'] = 14
        asset_digest['days_inactive'] = 7
        asset_digest['last_location'] = 'DSB-TANGI'
        asset_digest['last_status'] = 'Imobilized'
        asset_digest['distance'] = 5748
        asset_digest['fuel'] = 2567
        asset_digest['odometer'] = 378463
        asset_digest['wos'] = 2567
        asset_digest['tasks'] = 5
        asset_digest['activities'] = 7
        context['asset_digest'] = asset_digest

        # url = f"https://secure.fleetio.com/api/v1/equipment/{asset_model.vehicle_id}/assignments"
        url = f'{fleetioapi}v1/vehicles/{asset_model.vehicle_id}/assignments'
        # print(fleetioapi, headers)
        res = requests.request("GET", url, headers=headers, data=payload)
        context['asset_assignments'] = 'NA'
        if res.status_code == 200:
            context['asset_assignments'] = res.text
        
        # wailon assets
        # url = f'{fleetioapi}v1/vehicles/{asset_model.vehicle_id}/assignments'
        # # print(fleetioapi, headers)
        # res = requests.request("GET", url, headers=headers, data=payload)
        # context['asset_status'] = 'NA'
        # if res.status_code == 200:
        #     context['asset_status'] = res.text
        
        # sessionid = self.getWialonSession() 
        # wialonsess = {"sid":sessionid, "params": '', "payload": {}, "headers": {}}
        # vid = asset_model.vehicle_id
        # # print(vid)
        # # wialonsess['params'] = ''.join('params={"id":').join([f'{vid}, ',])

        # pars = ''.join('params={"id":')
        # pars = ''.join([pars, f'{vid}, "flags": 1024', '}'])
        # wialonsess['params'] = pars
        # wialonsess['payload'] = {
        #                 'sid': sessionid,
        #             }
        # wialonsess['headers'] = {
        #                 'Accept': 'application/json',
        #                 'Authorization': wialontoken,
        #             }
        # context['wasset_details'] = self.getAssetDetails(sess=wialonsess)
        # # context['wasset_details'] = sessionid

        # update_assets = self.updateAssetData()
        
        return context

    def get_queryset(self):
        return AssetModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get(self, request, *args, **kwargs):
        response = super(AssetModelDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        # print('data', self.dwn_report_file)
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/asset_rpt.html")
            
            data = context['wo_qs']
            # print(data)
            df = pd.DataFrame.from_dict(data)
            # df = pd.DataFrame.from_dict(data.values('order_no'))
            # df = pd.DataFrame(list(data))
            # context['asset'] = df.to_html()
            html  = template.render(context)
            result = BytesIO()
            # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
            pdf = pisa.pisaDocument(BytesIO(html.encode()), result)
            if not pdf.err:
                return HttpResponse(result.getvalue(), content_type='application/pdf')
            return None
        
         # rendering the template
        # return HttpResponse(pdf, content_type='application/pdf')
        return response

    def getAssetDetails(self, sess=None, **kwargs):
        paramsx = sess['params']
        url = f'https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_item&{sess["params"]}&sid={sess["sid"]}'
        # url = 'https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_item&params={"id":2516374, "flags":1024}&sid=09387a257a20f0c51f1d862c368b4f4c'
        # url = 'https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_item&svc=report/get_report_data&params={"itemId":15, "col":[]}'
        print(url)
        response = requests.request("GET", url, headers=sess['headers'], data=sess['payload'])
        res = []
        print(type(response.text))
        # if(type(response.text)=="str"):
        res = json.loads(response.text)
        disp = ''
        disp = res
        if res['error'] == 7:
            disp = 'Access Denied'
        return disp

    def getWialonSession(self):
        wltoken = f'"token":"{ wialontoken}"'
        wltkn = f'{wltoken}'
        wlparams = 'params={'+wltkn+'}'
        wlurl = f'https://hst-api.wialon.com/wialon/ajax.html?svc=token/login&{wlparams}'
        print(wlurl)
        wialonpayload = {}
        # response = requests.request("GET", wlurl, headers=wialonheaders, data=wialonpayload)
        response = requests.request("GET", wlurl)
        resjson = json.loads(response.text)
        # if resjson:
        #     print(resjson['eid'])
        return resjson['eid']

    def updateAssetData(self):
        f = open('aix/templates/aix/reports/wialon_assets.json', 'r')
        obj = simplejson.load(f)
        # print(obj)
        asset_qs = AssetModel.objects.all() 
        # for asset in asset_qs:
            # # print(asset.name)
            # for o in obj:
            # #     # print(o['nm'])
            #     print(asset.name)
            #     nm = o['nm']
            #     if nm == asset.name:
            #         print(o['nm'])
        assets = []
        objs = []
        x = 0
        for o in obj:
            record = {'wialon_id': 0, 'name': "", "pk": x}
            record['wialon_id'] = o['id']
            record['name'] = o['nm']
            assets.append(record)
            nm = o['nm']
            # rec = AssetModel(name=nm).update_or_create(wialon_id=id)
            # objs.append(rec)
            x = x+1
            # asset_qs.filter(name__exact=nm).update(wialon_id=id)
            # record = asset_qs.filter(name__exact=nm).update(wialon_id=id)
            # try:
                # record: AssetModel  = get_object_or_404(asset_qs, name=o['nm'])
                # record = AssetModel.objects.get(name=o['nm'])
                # print(o['nm'])
                # record = AssetModel.objects.filter(name=o['nm']).first()
                # ast, record = AssetModel.objects.get(name=nm)
                # nm = o['nm']
                # id = o['id']
                # record = asset_qs.filter(name__exact=nm).update(wialon_id=id)
                # record = get_object_or_404(AssetModel, name=nm)
                # print(record)
                # if not record == None:
                #     record.id = o['id']
                #     print(record.name)
                #     # print(record.vehicle_id)
                #     record.objects.update_or_create(id=o['id'])
                    # record.save(update_fields=['id',])
            # except AssetModel.DoesNotExist:
            #     record = None
        # for asset in objs:
        #     record = asset_qs.filter(name=asset['nm'])
        #     assets.append(record)
        # AssetModel.objects.bulk_update(objs, ['name'])
        # print(objs)
        # AssetModel.objects.bulk_update(assets, update_fields=['name'])

        # for asset in asset_qs:
        #     ast = AssetModel.objects.in_bulk(['WT20C-001-UBN 201X'], field_name='uuid') 
        #     print(ast)

        return None
