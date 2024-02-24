from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SupportTicket, SupportPicture
from .forms import SupportTicketForm, SupportPictureForm

@login_required
def create_support_ticket(request):
    if request.method == 'POST':
        ticket_form = SupportTicketForm(request.POST)
        picture_form = SupportPictureForm(request.POST, request.FILES)
        if ticket_form.is_valid() and picture_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.save()
            for picture in request.FILES.getlist('pictures'):
                SupportPicture.objects.create(support_ticket=ticket, picture=picture)
            return redirect('support_home')  # Redirect to the support homepage
    else:
        ticket_form = SupportTicketForm()
        picture_form = SupportPictureForm()
    return render(request, 'support/create_support_ticket.html', {'ticket_form': ticket_form, 'picture_form': picture_form})

@login_required
def support_ticket_detail(request, pk):
    ticket = get_object_or_404(SupportTicket, pk=pk)
    return render(request, 'support/support_ticket_detail.html', {'ticket': ticket})

@login_required
def update_support_ticket(request, pk):
    ticket = get_object_or_404(SupportTicket, pk=pk)
    if request.method == 'POST':
        ticket_form = SupportTicketForm(request.POST, instance=ticket)
        picture_form = SupportPictureForm(request.POST, request.FILES)
        if ticket_form.is_valid() and picture_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.save()
            for picture in request.FILES.getlist('pictures'):
                SupportPicture.objects.create(support_ticket=ticket, picture=picture)
            return redirect('support_ticket_detail', pk=pk)  # Redirect to the ticket detail page
    else:
        ticket_form = SupportTicketForm(instance=ticket)
        picture_form = SupportPictureForm()
    return render(request, 'support/update_support_ticket.html', {'ticket_form': ticket_form, 'picture_form': picture_form})

@login_required
def delete_support_ticket(request, pk):
    ticket = get_object_or_404(SupportTicket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('support_home')  
    return render(request, 'support/delete_support_ticket.html', {'ticket': ticket})

