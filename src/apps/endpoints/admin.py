from django.contrib import admin
from apps.endpoints.models import MLAlgorithm, MLAlgorithmStatus, MLRequest, Endpoint, ABTest


# Register your models here.

MLModels = [MLAlgorithm, MLAlgorithmStatus, MLRequest, Endpoint, ABTest]

for Model in MLModels:
    admin.site.register(Model)

# @admin.register(Endpoint)
# class MLAdmin(admin.ModelAdmin):
#     list_display = ('name', 'owner', 'created_at')
