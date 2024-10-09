
from django.http import HttpResponse

# As views no Django processam requisições HTTP e retornam respostas ao usuário, conectando dados e templates.

def cars_view(request):
    html = '''
         <html>
             <head>
                  <title>Meus Carros</title>
             </head>
             <body>
                  <h1>Carros do Ulisses</h1>
                  <h3>Só Carro Top!</h3>
             </body>
                 
           
         </html>
    '''
    return HttpResponse(html)