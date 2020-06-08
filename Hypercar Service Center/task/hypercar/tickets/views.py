from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

def get_next_ticket():
    # print(settings.LINE_OF_CARS)
    if len(settings.LINE_OF_CARS["change_oil"]) > 0:
        return settings.LINE_OF_CARS["change_oil"][0]
    elif len(settings.LINE_OF_CARS["inflate_tires"]) > 0:
        return settings.LINE_OF_CARS["inflate_tires"][0]
    elif len(settings.LINE_OF_CARS["diagnostic"]) > 0:
        return settings.LINE_OF_CARS["diagnostic"][0]
    else:
        return 0




class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/menu/menu.html')


class ChangeOilView(View):
    def get(self, request, *args, **kwargs):
        print(settings.LINE_OF_CARS)
        settings.COUNTER += 1
        time = len(settings.LINE_OF_CARS["change_oil"]) * 2
        settings.LINE_OF_CARS["change_oil"].append(settings.COUNTER)
        return render(request, 'tickets/get_ticket/ticket.html', context={
            'counter': settings.COUNTER,
            'time_to_wait': time
        })


class InflateTiresView(View):
    def get(self, request, *args, **kwargs):
        # print(settings.LINE_OF_CARS)
        settings.COUNTER += 1
        time = len(settings.LINE_OF_CARS["change_oil"]) * 2 + \
               len(settings.LINE_OF_CARS["inflate_tires"]) * 5
        settings.LINE_OF_CARS["inflate_tires"].append(settings.COUNTER)
        return render(request, 'tickets/get_ticket/ticket.html', context={
            'counter': settings.COUNTER,
            'time_to_wait': time
        })


class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        # print(settings.LINE_OF_CARS)
        settings.COUNTER += 1
        time = len(settings.LINE_OF_CARS["change_oil"]) * 2 + \
               len(settings.LINE_OF_CARS["inflate_tires"]) * 5 + \
               len(settings.LINE_OF_CARS["diagnostic"]) * 30
        settings.LINE_OF_CARS["diagnostic"].append(settings.COUNTER)
        return render(request, 'tickets/get_ticket/ticket.html', context={
            'counter': settings.COUNTER,
            'time_to_wait': time
        })


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        # print(settings.LINE_OF_CARS)
        return render(request, 'tickets/processing/processing.html', context={
            'change_oil': len(settings.LINE_OF_CARS["change_oil"]),
            'inflate_tires': len(settings.LINE_OF_CARS["inflate_tires"]),
            'diagnostic': len(settings.LINE_OF_CARS["diagnostic"])
        })

    def post(self, request, *args, **kwargs):
        # print(settings.LINE_OF_CARS)
        if len(settings.LINE_OF_CARS["change_oil"]) > 0:
            settings.TICKET_NO = get_next_ticket()
            settings.LINE_OF_CARS["change_oil"].popleft()
            settings.COUNTER -= 1
        elif len(settings.LINE_OF_CARS["inflate_tires"]) > 0:
            settings.TICKET_NO = get_next_ticket()
            settings.LINE_OF_CARS["inflate_tires"].popleft()
            settings.COUNTER -= 1
        elif len(settings.LINE_OF_CARS["diagnostic"]) > 0:
            settings.TICKET_NO = get_next_ticket()
            settings.LINE_OF_CARS["diagnostic"].popleft()
            settings.COUNTER -= 1
        else:
            settings.TICKET_NO = get_next_ticket()
        return redirect('/next')


class NextView(View):
    def get(self, request, *args, **kwargs):
        # print(settings.LINE_OF_CARS)
        return render(request, 'tickets/next/next.html', context={
            'ticket_no': settings.TICKET_NO})
