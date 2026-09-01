from django.shortcuts import render, get_object_or_404, redirect

# Importamos nuestro modelo Articulo
from .models import Articulo, Perfil

# Importamos el formulario para crear artículos
from .forms import ArticuloForm, PerfilForm, ContactoForm

# Sirve para obligar al usuario a iniciar sesión
from django.contrib.auth.decorators import login_required

# Formularios que Django ya trae preparados
# AuthenticationForm = iniciar sesión
# UserCreationForm = registrar un usuario nuevo
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Funciones de Django para iniciar y cerrar sesión
from django.contrib.auth import login, logout

from django.contrib.auth.models import Group

# ---------------------------------------------------
# PÁGINA PRINCIPAL + BUSCADOR
# ---------------------------------------------------

def inicio(request):

    # Traemos todos los artículos.
    articulos = Articulo.objects.all().order_by('-creado')

    # Tomamos lo que el usuario escribió en el buscador.
    # Si no escribió nada, queda como texto vacío.
    busqueda = request.GET.get('q', '')

    # Si escribió algo...
    if busqueda:

        # Filtramos por título.
        # icontains busca sin importar mayúsculas/minúsculas.
        articulos = articulos.filter(
            titulo__icontains=busqueda
        )

    # Enviamos los artículos y la búsqueda al HTML.
    return render(
        request,
        'blog/inicio.html',
        {
            'articulos': articulos,
            'busqueda': busqueda
        }
    )


# ---------------------------------------------------
# VER UN ARTÍCULO
# ---------------------------------------------------

def detalle(request, pk):

    # Buscamos un artículo usando su ID.
    # Si no existe, Django muestra automáticamente error 404.
    articulo = get_object_or_404(Articulo, pk=pk)

    # Mandamos ese artículo al HTML detalle.html
    return render(
        request,
        'blog/detalle.html',
        {'articulo': articulo}
    )


# ---------------------------------------------------
# CREAR UN ARTÍCULO
# ---------------------------------------------------

# Solo permite entrar si el usuario inició sesión.
# Si no inició sesión, lo manda a iniciar_sesion.
@login_required(login_url='iniciar_sesion')
def crear(request):

    # Si el usuario apretó el botón para enviar el formulario...
    if request.method == 'POST':

        # Recibimos los datos escritos en el formulario.
        form = ArticuloForm(request.POST)

        # Comprobamos que sean válidos.
        if form.is_valid():

            # Creamos el artículo pero todavía no lo guardamos.
            articulo = form.save(commit=False)

            # Ponemos como autor al usuario que está logueado.
            articulo.autor = request.user

            # Ahora sí lo guardamos en la base de datos.
            articulo.save()

            # Después volvemos a la página principal.
            return redirect('inicio')

    else:

        # Si recién entramos a /crear/,
        # mostramos un formulario vacío.
        form = ArticuloForm()

    # Mostramos crear.html y enviamos el formulario.
    return render(
        request,
        'blog/crear.html',
        {'form': form}
    )


# ---------------------------------------------------
# INICIAR SESIÓN
# ---------------------------------------------------

def iniciar_sesion(request):

    # Si el usuario envió usuario y contraseña...
    if request.method == 'POST':

        # Creamos el formulario usando los datos recibidos.
        formulario = AuthenticationForm(
            request,
            data=request.POST
        )

        # Comprobamos que usuario y contraseña sean correctos.
        if formulario.is_valid():

            # Obtenemos el usuario que inició sesión.
            usuario = formulario.get_user()

            # Django inicia la sesión de ese usuario.
            login(request, usuario)

            # Lo mandamos al inicio del blog.
            return redirect('inicio')

    else:

        # Si simplemente entró a /login/,
        # mostramos un formulario vacío.
        formulario = AuthenticationForm()

    # Mostramos el HTML para iniciar sesión.
    return render(
        request,
        'blog/iniciar_sesion.html',
        {'formulario': formulario}
    )


# ---------------------------------------------------
# REGISTRAR UN USUARIO NUEVO
# ---------------------------------------------------

def registrarse(request):

    if request.method == 'POST':

        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():

            # ==========================================
            # 1. CREAMOS EL USUARIO
            # ==========================================

            usuario = formulario.save()


            # ==========================================
            # 2. BUSCAMOS EL GRUPO "AUTORES"
            # ==========================================

            grupo_autores = Group.objects.get(
                name='Autores'
            )


            # ==========================================
            # 3. AGREGAMOS EL USUARIO AL GRUPO
            # ==========================================

            usuario.groups.add(
                grupo_autores
            )


            # ==========================================
            # 4. INICIAMOS SESIÓN AUTOMÁTICAMENTE
            # ==========================================

            login(
                request,
                usuario
            )


            # ==========================================
            # 5. VOLVEMOS AL INICIO
            # ==========================================

            return redirect('inicio')

    else:

        formulario = UserCreationForm()


    return render(
        request,
        'blog/registrarse.html',
        {
            'formulario': formulario
        }
    )


# ---------------------------------------------------
# CERRAR SESIÓN
# ---------------------------------------------------

def cerrar_sesion(request):

    # Cerramos la sesión del usuario actual.
    logout(request)

    # Lo mandamos nuevamente al inicio.
    return redirect('inicio')

# ---------------------------------------------------
# EDITAR UN ARTÍCULO
# ---------------------------------------------------

@login_required(login_url='iniciar_sesion')
def editar(request, pk):

    # Buscamos el artículo por su ID.
    # Si no existe, Django muestra error 404.
    articulo = get_object_or_404(Articulo, pk=pk)

    # Comprobamos que el artículo pertenezca
    # al usuario que inició sesión.
    if articulo.autor != request.user:
        return redirect('inicio')

    # Si el usuario envió el formulario...
    if request.method == 'POST':

        # Creamos el formulario con los nuevos datos.
        # instance=articulo significa que vamos a editar
        # ese artículo existente y no crear uno nuevo.
        form = ArticuloForm(
            request.POST,
            instance=articulo
        )

        # Comprobamos que los datos sean válidos.
        if form.is_valid():

            # Guardamos los cambios.
            form.save()

            # Volvemos al detalle del artículo.
            return redirect(
                'detalle',
                pk=articulo.pk
            )

    else:

        # Si el usuario recién entra a editar,
        # mostramos el formulario cargado con
        # los datos actuales del artículo.
        form = ArticuloForm(
            instance=articulo
        )

    # Mostramos editar.html
    # y enviamos el formulario y el artículo.
    return render(
        request,
        'blog/editar.html',
        {
            'form': form,
            'articulo': articulo
        }
    )

# ---------------------------------------------------
# ELIMINAR UN ARTÍCULO
# ---------------------------------------------------

# El usuario tiene que haber iniciado sesión.
@login_required(login_url='iniciar_sesion')
def eliminar(request, pk):

    # Buscamos el artículo por su ID.
    # Si no existe, Django muestra error 404.
    articulo = get_object_or_404(Articulo, pk=pk)

    # Comprobamos que el usuario que intenta eliminar
    # sea realmente el autor del artículo.
    if articulo.autor != request.user:
        return redirect('inicio')

    # Si el usuario confirmó la eliminación
    # apretando el botón del formulario...
    if request.method == 'POST':

        # Eliminamos el artículo de la base de datos.
        articulo.delete()

        # Después volvemos al inicio.
        return redirect('inicio')

    # Si todavía no confirmó,
    # mostramos la página de confirmación.
    return render(
        request,
        'blog/eliminar.html',
        {'articulo': articulo}
    )

# ==========================================
# MI PERFIL
# ==========================================

# Solo un usuario que inició sesión
# puede entrar a su perfil.
@login_required(login_url='iniciar_sesion')
def mi_perfil(request):

    # Buscamos el perfil del usuario logueado.
    #
    # Si todavía no tiene un perfil,
    # get_or_create lo crea automáticamente.
    perfil, creado = Perfil.objects.get_or_create(
        usuario=request.user
    )

    # Si el usuario apretó el botón Guardar...
    if request.method == 'POST':

        # Cargamos los datos enviados en el formulario
        # sobre el perfil que ya pertenece al usuario.
        form = PerfilForm(
            request.POST,
            instance=perfil
        )

        # Comprobamos que los datos sean válidos.
        if form.is_valid():

            # Guardamos los cambios.
            form.save()

            # Volvemos al mismo perfil.
            return redirect('mi_perfil')

    else:

        # Si simplemente entramos a la página,
        # mostramos el formulario con los datos actuales.
        form = PerfilForm(
            instance=perfil
        )

    # Mostramos mi_perfil.html
    return render(
        request,
        'blog/mi_perfil.html',
        {
            'form': form,
            'perfil': perfil
        }
    )

# ==========================================
# ACERCA DE MÍ
# ==========================================

def acerca_de(request):

    # Esta vista solamente muestra
    # la página acerca_de.html.
    #
    # No necesitamos consultar la base de datos
    # porque es una página estática.
    return render(
        request,
        'blog/acerca_de.html'
    )

# ==========================================
# CONTACTO
# ==========================================

def contacto(request):

    enviado = False

    # Si el usuario envió el formulario...
    if request.method == 'POST':

        form = ContactoForm(request.POST)

        if form.is_valid():

            # Guardamos el mensaje
            form.save()

            # Indicamos que se envió correctamente
            enviado = True

            # Limpiamos el formulario
            form = ContactoForm()

    else:

        form = ContactoForm()

    return render(
        request,
        'blog/contacto.html',
        {
            'form': form,
            'enviado': enviado
        }
    )