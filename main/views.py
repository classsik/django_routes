from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def all_posts(request):
    posts = [
        {
            'id': 0,
            'title': 'Title 1',
            'content': 'Lorem ipsum',
            'likes': 6,
            'comments': [],
            'date': '2022-11-25T07:04:29.422Z',
        },
        {
            'id': 1,
            'title': 'Title 2',
            'content': 'Lorem ipsum',
            'likes': 0,
            'comments': [],
            'date': '2022-11-25T07:04:29.422Z',
        },
        {
            'id': 2,
            'title': 'Title 3',
            'content': 'Lorem ipsum',
            'likes': 0,
            'comments': [],
            'date': '2022-11-25T07:04:29.422Z',
        }
    ]
    return JsonResponse(posts, safe=False)


def popular_posts(request):
    popular = [
        {
            'id': 0,
            'title': 'Title 1',
            'content': 'Lorem ipsum',
            'likes': 6,
            'comments': [],
            'date': '2022-11-25T07:04:29.422Z',
        },
    ]
    return JsonResponse(popular, safe=False)


def latest_posts(request):
    latest = [
        {
            'id': 0,
            'title': 'Title 1',
            'content': 'Lorem ipsum',
            'likes': 0,
            'comments': [],
            'date': '2022-11-25T07:04:29.422Z',
        },
    ]
    return JsonResponse(latest, safe=False)


def post_likes(request, post_id):
    posts = [
        {
            'id': 0,
            'title': 'Title 1',
            'content': 'Lorem ipsum',
            'likes': 6,
            'comments': [],
            'date': '2022-11-25T07:04:29.422Z',
        },
        {
            'id': 1,
            'title': 'Title 2',
            'content': 'Lorem ipsum',
            'likes': 0,
            'comments': [],
            'date': '2022-11-25T07:04:29.422Z',
        },
        {
            'id': 2,
            'title': 'Title 3',
            'content': 'Lorem ipsum',
            'likes': 0,
            'comments': [],
            'date': '2022-11-25T07:04:29.422Z',
        }
    ]

    result = {}

    for post in posts:
        if post['id'] == post_id:
            result = post
    return HttpResponse(f'??????-???? ????????????: {result["likes"]}')


def post_comments(request, post_id):
    posts = [
        {
            'id': 0,
            'title': 'Title 1',
            'content': 'Lorem ipsum',
            'likes': 6,
            'comments': [
                {'author': 0, 'text': 'Test text 1'},
                {'author': 1, 'text': 'Test text 2'},
            ],
            'date': '2022-11-25T07:04:29.422Z',
        },
        {
            'id': 1,
            'title': 'Title 2',
            'content': 'Lorem ipsum',
            'likes': 0,
            'comments': [
                {'author': 0, 'text': 'Test text 1'},
            ],
            'date': '2022-11-25T07:04:29.422Z',
        },
        {
            'id': 2,
            'title': 'Title 3',
            'content': 'Lorem ipsum',
            'likes': 0,
            'comments': [
                {'author': 1, 'text': 'Test text 2'},
            ],
            'date': '2022-11-25T07:04:29.422Z',
        }
    ]

    result = {}

    for post in posts:
        if post['id'] == post_id:
            result = post
    return JsonResponse(result['comments'], safe=False)


def home(request):
    login = request.GET.get('login', None)
    password = request.GET.get('password', None)

    login_text = login if login is not None else '???? ??????????'
    password_text = password if password is not None else '???? ??????????'
    return HttpResponse(f"""
    <p>??????????: {login_text}</p>
    <p>????????????: {password_text}</p>
    """)


def about(request):
    return HttpResponseRedirect('/')


def contacts(request):
    return HttpResponseRedirect('/')


def handle404(request, exception):
    return HttpResponse('<p>???????????????? ???????????????? ???????? ?????????????????? ??????????????</p>', status=404)


def access(request):
    login = request.GET.get('login', None)
    password = request.GET.get('password', None)

    result = '???????????? ????????????????'

    if login == 'admin' and password == 'admin':
        result = '?????? ????????'

    return HttpResponse(f"""<p>{result}</p>""")


def json(request):
    result = {}
    for item in request.GET:
        result[f'{item}'] = request.GET[f'{item}']

    return JsonResponse(result, safe=False)


def get(request):
    for item in request.GET:
        result = request.COOKIES.get(f'{item}', None)
    return HttpResponse(f'{item}: {result}')


def set(request):
    for item in request.GET:
        response = HttpResponse('Cookie ??????????????????????')
        response.set_cookie(key=item, value=request.GET[f'{item}'])
    return response
