from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Home Page</h1>
        <p>Bienvenido a nuestra página de inicio.</p>
        <a href="/about/">About</a><br>
        <a href="/contact/">Contact</a>
    """)

def about(request):
    return HttpResponse("""
        <h1>About Page</h1>
        <p>Acerca de nosotros: Somos una empresa dedicada a...</p>
        <a href="/">Home</a><br>
        <a href="/contact/">Contact</a>
    """)

def contact(request):
    if request.method == 'POST':
        return HttpResponse("<h1>Formulario de contacto enviado</h1>")
    return HttpResponse("""
        <h1>Contact Page</h1>
        <form method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" rows="4" required></textarea><br><br>
            <input type="submit" value="Submit">
        </form>
        <a href="/">Home</a><br>
        <a href="/about/">About</a>
    """)

