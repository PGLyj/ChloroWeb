from django.shortcuts import render

# Create your views here.
def post_list(request):
        return render(request, 'blog/post_list.html', {}) 
# url에서 view.post_list를 부르면 blog/post_list.html을 부른다. 부를때 {}안에 변수를 보내준다. 해당 변수는 model.py 에서 가져오게됨.