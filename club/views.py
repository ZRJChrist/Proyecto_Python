from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member, Court, Book
from .forms import MemberForm, CourtForm , BookForm


def member_all(request):
    members = Member.objects.all()
    category_badges = {
        'Infant': 'primary',
        'Junior': 'secondary',
        'Adult': 'success',
        'Senior': 'dark',
    }
    return render(request, 'member/member_All.html', {'members': members, 'category_badges': category_badges})

def member_new(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_all')
    else:
        form = MemberForm()

    return render(request, 'member/member_New.html',{'form': form})


def member_edit(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_all')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member/member_Edit.html', {'form': form, 'member': member})

def member_delete(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.delete()
    return redirect('member_all')


def court_all(request):
    courts = Court.objects.all()
    return render(request, 'court/court_All.html', {'courts': courts})

def court_new(request):
    if request.method == 'POST':
        form = CourtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('court_all')
    else:
        form = CourtForm()
    
    return render(request, 'court/court_New.html', {'form': form})

def court_edit(request, court_id):
    court = get_object_or_404(Court, id=court_id)
    if request.method == 'POST':
        form = CourtForm(request.POST, instance=court)
        if form.is_valid():
            form.save()
            return redirect('court_all')
    else:
        form = CourtForm(instance=court)
    return render(request, 'court/court_Edit.html', {'form': form, 'member': court})


def court_delete(request, court_id):
    court = get_object_or_404(Court, id=court_id)
    court.delete()
    return redirect('court_all')

def book_all(request):
    books = Book.objects.all()
    return render(request, 'book/book_all.html', {'books': books})


def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_all')
    else:
        form = BookForm()
    
    return render(request, 'book/book_New.html', {'form': form})

def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_all')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_Edit.html', {'form': form, 'member': book})

def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_all')