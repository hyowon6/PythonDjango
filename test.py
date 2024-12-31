topics = [
    {'id':1, 'title':'routing', 'body': 'Routing is ...'},
    {'id':2, 'title':'view', 'body': 'View is ...'},
    {'id':3, 'title':'model', 'body': 'Model is ...'},
]

ol = ''
for topic in topics:
    ol += f'<li>{topic["title"]}</li>'
    print(ol); input()