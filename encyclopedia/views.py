from django.shortcuts import render,redirect
from markdown2 import Markdown
import random
from . import util

# This function is used to convert markdown formatted text to HTML.
# It takes in one argument `title` which is used to retrieve the markdown content.
# The function uses the `util` module to retrieve the content and the `Markdown` class
# to convert the markdown content to HTML.
# If the content is not found, the function returns `None`.
# Otherwise, it returns the converted HTML.

def convert_md_html(title):
    # Get the markdown content for the given title
    content = util.get_entry(title)

    # If the content is not found, return None
    if content == None:
        return None

    # Convert the markdown content to HTML
    markdown = Markdown()
    html = markdown.convert(content)

    # Return the converted HTML
    return html
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "title":title,
            "message":"This entry does not exist.",
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "body": html_content
        })  

def search(request):
    if request.method=='GET':
        query = request.GET['q']
        html_content = convert_md_html(query)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
            "title": query,
            "body": html_content
        })  
        else:   
            return render(request, "encyclopedia/error.html",{
            "title":query,
            "message":"No entries found with the keyword "
        })

def newpage(request):
    if request.method == 'GET':
        return render(request,"encyclopedia/newpage.html") 
    else:
        title = request .POST["title"]
        content = request.POST["content"]
        if util.get_entry(title) is not None :
            return render(request,"encyclopedia/error.html",{
                "title": title,
                "message": "Already exists with keyword "
            })
        else:
            util.save_entry(title,content)
            return render(request,"encyclopedia/entry.html",{
                "title":title,
                "body": convert_md_html(title)
            })
        
def edit(request):
    if request.method == 'POST':
        title = request.POST['data']
        content = util.get_entry(title)
        return render (request,'encyclopedia/edit.html',{
            'title':title,
            'body':content
        })
    
def save_edit(request):
    if request.method=='POST':
        title=request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        return render(request,"encyclopedia/entry.html",{
                "title":title,
                "body": convert_md_html(title)
            })

def random_page(request):
    entries = util.list_entries()
    page = random.choice(entries)
    return render(request,"encyclopedia/entry.html",{
                "title":page,
                "body": convert_md_html(page)
            })
    