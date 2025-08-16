from django.shortcuts import render
from django.views.generic import TemplateView

# Serve the static todo app
class TodoAppView(TemplateView):
    template_name = "todo_app.html"
