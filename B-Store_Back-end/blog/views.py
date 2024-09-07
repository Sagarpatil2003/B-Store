from django.shortcuts import render
from .models import Book
from .forms import BookForm , UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login 


def book_list(request):
    books = Book.objects.all().order_by("-created_at")
    return render(request, "book_list.html", {"books": books, 'user':request.user})

@login_required
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "book_form.html", {"form": form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "book_confirm_delete.html", {"book": book})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserRegistrationForm()  # Ensure form is instantiated
    return render(request, 'registration/register.html', {'form': form})

            
        








