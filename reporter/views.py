from django.shortcuts import render,HttpResponse
from django.core.serializers import serialize
from .models import *
from django.db.models import Count
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.morris import DonutChart

# Create your views here.
def three_D(request):
    point=Incidence.objects.first()
    point=str(point.location).split(" ")
    laititude=float(point[2][:-1])
    longitude=float(point[1][1:])
    return render(request,'geodjango/3d.html',{"lat":laititude,"long":longitude,})

def main (request):
    status_content=['Collapsed','Unsafe','Bad']
    bad = Incidence.objects.filter(status='1').annotate(count=Count('status'))
    mod = Incidence.objects.filter(status='2').annotate(count=Count('status'))
    worse = Incidence.objects.filter(status='3').annotate(count=Count('status'))
    count_per_status=[worse.count(),mod.count(),bad.count()]
    print(count_per_status)
    data = [[]] * (len(status_content) + 1)
    # create a lst of lists with lists equal to the number of objects plus one
    # ....to cater for headings
    data[0] = ["Severity_Level", "Count"]
    for x in range(len(status_content)):
        mylist = [0, 0]
        mylist[0] = str(status_content[x])
        mylist[1] = count_per_status[x]
        data[x + 1] = mylist  # populate list with the 2 item array
    dataSource = SimpleDataSource(data=data)
    donut_chart = DonutChart(dataSource)

    return render(request,'geodjango/index.html',{"chart1":donut_chart})

def county_dataset(request):
    data=serialize('geojson',Counties.objects.all())
    return HttpResponse(data,content_type='json')


def incidence_dataset(request,stat):
    if stat=='1':
        stat=int(stat)
        data = serialize('geojson', Incidence.objects.filter(status=stat))
        return HttpResponse(data, content_type='json')

    if stat=='2':
        stat=int(stat)
        data = serialize('geojson', Incidence.objects.filter(status=stat))
        return HttpResponse(data, content_type='json')

    if stat == '3':
        stat = int(stat)
        data = serialize('geojson', Incidence.objects.filter(status=stat))
        return HttpResponse(data, content_type='json')
