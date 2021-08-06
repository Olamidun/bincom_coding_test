from django.urls import path
from . import views

app_name = 'election_results'

urlpatterns = [
    path('results/<int:id>', views.polling_unit_result, name="polling_unit_result"),
    path('total_result/<int:lga_id>', views.total_result, name="total_result")
]