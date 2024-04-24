from django.shortcuts import render, redirect
from django.contrib import messages
# import todo form and models


from .models import Todo
from .forms import Todo_Form, TodoCategoryForm


def categorize_todos(request):
    if request.method == 'POST':
        form = TodoCategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            custom_category = form.cleaned_data['custom_category']
            if custom_category:
                category = Todo.TodoCategory(int(category), custom_category)
            todos = Todo.objects.all()
            for todo in todos:
                todo.category = category
                todo.save()
            return redirect('todo_list')
    else:
        form = TodoCategoryForm()
    return render(request, 'categorize_todos.html', {'form': form})

def index(request):

	item_list = Todo.objects.order_by("-date")
	if request.method == "POST":
		form = Todo_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = Todo_Form()

	page = {
		"forms": form,
		"list": item_list,
		"title": "TODO LIST",
	}
	return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')
