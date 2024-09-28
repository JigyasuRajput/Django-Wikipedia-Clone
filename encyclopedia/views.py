from django.shortcuts import render, redirect
from .forms import NewPageForm
import markdown
from . import util
import random
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
     
     
def title(request, title):
    
    text = util.get_entry(title)
    
    if text is None:
        html_content = "<h1>Page not found</h1>"
    else:
        html_content = markdown2.markdown(text)

    return render(request, 'encyclopedia/title.html', {
        "title": title,
        'html_content': html_content
    })
    

def search(request):
    query = request.GET.get('query').lower()
    list_of_entries = util.list_entries()
    
    matching_entries = [entry for entry in list_of_entries if query in entry.lower()]
    
    print(f"Query: {query}")
    print(f"Matching Entries: {matching_entries}")

    return render(request, 'encyclopedia/search.html', {
        "matching_entries": matching_entries,
        "query": query
    })
    
    
def new_page(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)  
            return redirect('index')  
    else:
        form = NewPageForm()
    return render(request, 'encyclopedia/new_page.html', {'form': form})  


def edit_page(request, title):
    if request.method == 'POST':
        # Handle form submission
        content = request.POST['content']
        util.save_entry(title, content)
        return redirect('entry', title=title)
    else:
        # Pre-populate the form with existing content
        content = util.get_entry(title)
        return render(request, 'encyclopedia/edit_page.html', {
            'title': title,
            'content': content
        })
        
        
def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('entry', title=random_entry)

