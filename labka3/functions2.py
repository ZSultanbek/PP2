# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def GoodMovie(Movie):
    if Movie["imdb"] > 5.5:
        return True

    return False

def GoodMovies(Movies):
    list = []
    for Movie in Movies:
        if Movie["imdb"] > 5.5:
            list.append(Movie)
    
    return list

def MoviesOfCategory(Movies, category):
    list = []
    for Movie in Movies:
        if Movie["category"] == category:
            list.append(Movie)

    return list

def AvarageScore(Movies):
    avrg = 0
    counter = 0
    for Movie in Movies:
        avrg += Movie["imdb"]
        counter+=1
    
    return (avrg/counter)

def AvarageScorebyCategory(Movies, category):
    avrg = 0
    counter = 0
    for Movie in Movies:
        if Movie["category"] == category:
            avrg += Movie["imdb"]
            counter+=1
    
    return (avrg/counter)

print(GoodMovie(movies[1]))
print(GoodMovies(movies))
print(MoviesOfCategory(movies, "Romance"))
print(AvarageScore(movies[0:5]))
print(AvarageScorebyCategory(movies, "Romance"))