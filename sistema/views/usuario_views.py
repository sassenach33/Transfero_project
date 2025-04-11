from django.shortcuts import render


def listarUsuarios(request):
    return render(
        request,
        'usuarios/listar.html',
    )


