from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.fields import NullBooleanField
from mptt.admin import MPTTModelAdmin
from .models import Worker
from .forms import PersonForm

from mptt.exceptions import InvalidMove
from mptt.forms import MoveNodeForm

@admin.action(description='Remove sum salaries data from selected users')
def remove_sumsalaries(modeladmin, request, queryset):
    queryset.update(sum_salaries=0)

class AdminW(MPTTModelAdmin):  

    form = PersonForm
    actions = [remove_sumsalaries]
    mptt_indent_field = "name"
    list_display = (
        'name',
        'position',
        'date_start',
        'salary',
        'sum_salaries',
        'parent',
    )
    list_filter = ('position', 'level')
    list_display_links = ('parent',)

    def adminview(self, request):
        if request.method == 'POST':
            subject_f = self.form(request.POST)
            if subject_f.is_valid():
                Worker.objects.create(subject_f.cleaned_data.get(user=request.user))

    def move_category(request, category_pk):
        category = get_object_or_404(Worker, pk=category_pk)
        if request.method == 'POST':
            form = MoveNodeForm(category, request.POST)
            if form.is_valid():
                try:
                    category = form.save()
                except InvalidMove:
                    pass
        else:
            form = MoveNodeForm(category)

admin.site.register(Worker, AdminW)