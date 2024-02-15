from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import Daily_work_api
from rest_framework.response import Response
from . import models


def home(request):
    return render(request, "first.html")


def statistic(request):
    get_day = models.Daily_Works.objects.all()
    date = {"data_for_test": get_day}
    return render(request, "statistic.html", context=date)


class Daily_work_send_api(APIView):
    def get(self, request):
        posts = models.Daily_Works.objects.all()
        serializer = Daily_work_api(posts, many=True)
        return Response(serializer.data)