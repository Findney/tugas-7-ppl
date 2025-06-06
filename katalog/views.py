from django.http import HttpResponse

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Home - Katalog Produk</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    nav a {
                        margin-right: 15px;
                        text-decoration: none;
                        color: white;
                        background-color: #007bff;
                        padding: 8px 12px;
                        border-radius: 4px;
                    }
                    nav a:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <h1>Selamat Datang di Katalog Produk</h1>
                <nav>
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/kontak/">Kontak</a>
                </nav>
                <p>Gunakan menu di atas untuk menjelajahi halaman.</p>
            </body>
        </html>
    """)


def produk_list(request):
    return HttpResponse("""
        <h2>Daftar Produk</h2>
        <ul>
            <li><a href='/produk/1/'>Laptop ASUS</a></li>
            <li><a href='/produk/2/'>Headphone Sony</a></li>
            <li><a href='/produk/3/'>Smartphone Samsung</a></li>
        </ul>
    """)

def produk_detail(request, id):
    data = {
        1: "Laptop ASUS - Laptop gaming performa tinggi",
        2: "Headphone Sony - Suara jernih dan bass mantap",
        3: "Smartphone Samsung - Kamera canggih dan baterai awet"
    }
    konten = data.get(id, "Produk tidak ditemukan.")
    return HttpResponse(f"<h2>Detail Produk</h2><p>{konten}</p>")

def kontak(request):
    return HttpResponse("""
        <h2>Kontak Kami</h2>
        <p>Email: support@produkku.com</p>
        <p>Telp: 0812-3456-7890</p>
    """)
