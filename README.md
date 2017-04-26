# Movie trailer website generator
This is a python generator to automatically create a movie trailer website with your favorite movies.

## Getting started

To get started, fork this repository and download it to your computer.
You also need to have [python 2.7](https://www.python.org/) installed.

## Instructions

1. Create your own python file or use the _template.py_ included in this repository.
2. Make sure you `import` `media` and `fresh_tomatoes`
3. For each movie, create an instance of the class `Movie()`:
```python
movie1 = media.Movie(title,
                     storyline,
                     poster_image_url,
                     youtube_trailer_url,
                     imdb_url,
                     imdb_rating(float))
```
4. Put all your movies into a list `movies`:
```python
movies = [movie1, movie2, movie3]
```
5. Call the `open_movies_page()` function with your list of movies as an argument:
```python
fresh_tomatoes.open_movies_page(movies)
```
6. Run your code, and the website should open.

## Files included:

- **media.py**
Includes the class `Movie()` that stores information about the movie
- **fresh_tomatoes.py**
Includes the function `open_movies_page()` that generates the website
- **README.md**
This readme file
- **sample.py**
A sample pythonfile, showing how to use the `Movie()` class and `open_movies_page()` function to generate a trailer website
- **sample_website.html**
The HTML file generated from the sample.py file
- **template.py**
A python file with all framework set up to make your own Movie Trailer Website
- **LICENSE**
Detailed info about the MIT License


## Licencing
This project is licensed under the [MIT License](LICENSE) terms.