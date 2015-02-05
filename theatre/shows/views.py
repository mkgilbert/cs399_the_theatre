from django.shortcuts import render, get_object_or_404
from models import Show, Ticket


def all(request):
    shows = Show.objects.all()
    context = {"shows": shows}
    return render(request, "shows/all.html", context)


def detail(request, id, slug=None):
    show = get_object_or_404(Show, pk=id)
    context = {"show": show, "tickets": show.tickets.all()}
    return render(request, "shows/detail.html", context)


def ticket(request, show_id, ticket_id):
    context = {
        "ticket": get_object_or_404(Ticket, pk=ticket_id),
        "show": get_object_or_404(Show, pk=show_id)
    }
    return render(request, "shows/ticket.html", context)
