from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'wordcount/home.html')


def about(request):
    return render(request, 'wordcount/about.html')


def count(request):
    # 이렇게 하면 안되고
    full_text = request.GET['fulltext'] 
    # 아래와 같이 해야됩니다. 참고하세요
    # full_text = request.GET.get('fulltext')
    word_list = full_text.split()

    word_dictionary = {}
    total_count = 0
    for word in word_list:
        total_count += 1
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    context = {
        'fulltext':full_text,
        'dictionary':word_dictionary.items(),
        'totalCount':total_count
    }
    return render(request, 'wordcount/count.html', context)
