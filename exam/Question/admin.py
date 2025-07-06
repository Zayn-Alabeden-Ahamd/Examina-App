from django.contrib import admin

from .models import Question , Teacher , Answer

admin.site.register(Question)
admin.site.register(Teacher)
admin.site.register(Answer)
