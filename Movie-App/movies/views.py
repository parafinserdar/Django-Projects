from django.shortcuts import render
from .models import Category,Movie

kategori_liste = ["Bilim Kurgu","Gerilim","Aksiyon","Romantik"]
film_liste = [ 
    {
    "id":1,
    "film_adi":"Whiplash",
    "aciklama":"Whiplash aciklama",
    "resim":"1.jpg",
    "anasayfa": True
    },
    {
    "id":2,
    "film_adi":"Catch Me If You Can",
    "aciklama":"Catch Me If You Can aciklama",
    "resim":"2.jpg",
    "anasayfa": True
    },
    {
    "id":3,
    "film_adi":"The Prestige",
    "aciklama":"The Prestige aciklama",
    "resim":"3.jpg",
    "anasayfa": True
    },
    {
    "id":4,
    "film_adi":"Spider-Man: No Way Home",
    "aciklama":"Spider-Man: No Way Home aciklama",
    "resim":"4.jpg",
    "anasayfa": True
    },
    {
    "id":5,
    "film_adi":"Interstellar",
    "aciklama":"Interstellar aciklama",
    "resim":"5.jpg",
    "anasayfa": True
    },
    {
    "id":6,
    "film_adi":"Dune",
    "aciklama":"Dune aciklama",
    "resim":"6.jpg",
    "anasayfa": True
    },
    {
    "id":7,
    "film_adi":"Oppenheimer",
    "aciklama":"Oppenheimer aciklama",
    "resim":"7.jpg",
    "anasayfa": False
    },
    {
    "id":8,
    "film_adi":"The Shawshank Redemption",
    "aciklama":"The Shawshank Redemption aciklama",
    "resim":"8.jpg",
    "anasayfa": False
    },
    {
    "id":9,
    "film_adi":"Shutter Island",
    "aciklama":"Shutter Island aciklama",
    "resim":"9.jpg",
    "anasayfa": False
    },
    {
    "id":10,
    "film_adi":"Blade Runner 2049",
    "aciklama":"Blade Runner 2049 aciklama",
    "resim":"10.jpg",
    "anasayfa": False
    },
    {
    "id":11,
    "film_adi":"Drive",
    "aciklama":"Drive aciklama",
    "resim":"11.jpg",
    "anasayfa": False
    },
    {
    "id":12,
    "film_adi":"La La Land",
    "aciklama":"La La Land aciklama",
    "resim":"12.jpg",
    "anasayfa": False
    }
    
    ]
    

def home(request):   #data -> sayfaya gidecek olan data
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(anasayfa=True),
    }
    return render(request,"index.html",data) # artık index.html data'ya ulaşabilir.

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all(),
    }
    return render(request,"movies.html",data)


def movieDetails(request, id):
    data = {
       "movie": Movie.objects.get(id=id)
    }
    return render(request,"details.html",data)
