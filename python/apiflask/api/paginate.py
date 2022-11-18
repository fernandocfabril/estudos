from flask import request, url_for

"""
{
    "total": 50,
    "page": 10,
    "next": "/tarefas?page=1&per_page=3",
    "prev": "/tarefas?page=1&per_page=3",
    "results": [
        {
            "data": "1990-01-01",
            "descricao": "efds",
            "titulo": "teste",
            "id": 1
        }
    ]
}
"""


def paginate(model, schema):
    # pega o numero de paginas da requisição,
    # se não tiver o parametro 'page', começa em 1
    page = int(request.args.get('page', 1))
    # numero de registros por pagina, se o parametro
    # não for passado, considera 3 registros
    per_page = int(request.args.get('per_page', 3))
    
    # retorna os registros do modelo
    page_obj = model.query.paginate(page=page, per_page=per_page)

    next = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else page_obj.page, 
        per_page=per_page, 
        **request.view_args
    )

    prev = url_for(
        request.endpoint,
        page=page_obj.prev_num if page_obj.has_prev else page_obj.page, 
        per_page=per_page, 
        **request.view_args
    )

    return {
        'total': page_obj.total,
        'pages': page_obj.pages,
        'next': next,
        'prev': prev,
        'results': schema.dump(page_obj.items)
    }
