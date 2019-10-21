from django.views.generic import TemplateView

index = TemplateView.as_view(template_name='pages/index.html')
create = TemplateView.as_view(template_name='pages/create_task.html')
_list = TemplateView.as_view(template_name='pages/list_task.html')
result = TemplateView.as_view(template_name='pages/result.html')
