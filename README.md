# link_challenge
This directory includes:

titles.tsv

directors.tsv

actors.tsv

titles_AKA.tsv

names_AKA.tsv

These are all tab-separated files enclosed in quotes. They should be UTF-8 encoded, but some upstream encodings (Cyrillic and Chinese) may result in garbled text.

The file titles.tsv contains a 'movie_id', primary title, and 'production year' of a lot of movies. A film is often released in its production year in its home market, but may be released later. The 'movie_id' is used to key to the other tables. The file directors.tsv contains a person id, the movie id, name and gender of directors. A film may have zero, one, or many directors. The gender might be NA. The person id keys into the names_AKA.tsv. The file actors.tsv contains acts-in information for actors and actresses, with person id, movie id, primary name, and gender. Again, the movie id keys into the titles.tsv table, and the person id keys into the names_AKA.tsv. The titles_AKA.tsv file contains 'also known as' (AKA) titles for films--alternate titles in other markets and other languages, working titles, short titles, misspellings and so on. The file names_AKA.tsv contains alternate names for people (directors, actors and actresses). These are aliases, alternate spellings, other language renderings, and so on. The person id keys to the directors.tsv and actors.tsv tables.

If you knew some things about a film--the title, approximate year released, name of the director and some actors, you could use these data tables to find the movie_id and link to other data about the film, which are also keyed to the movie_id. This is your challenge.

In the tar file you should also find a directory of around 500 nyt movie reviews, taken from an obscure publication found sporadically on the east coast. These are raw html files. The job is to produce a list of links from html file name to movie_id. For example, if rendered as a csv, the lookup should probably include the lines:

file,movie_id

./nyt/2007/07/25/movies/25arct.html,60749

./nyt/2007/12/14/movies/14warh.html,26848

./nyt/2007/10/20/movies/20sara.html,615746

Not every movie reviewed will have a hit in the titles.tsv data. You can omit those files from your results, or list their movie_id as 'NA'. While a search on title is likely to be pretty good, titles are not unique over the years, and you may get a false match: using director and actor information is likely to improve the matching.

The point of this exercise is not just to produce this file of links. In fact, the file of links is possibly irrelevant. The goal is to see how you approach a problem, how you write code, and how you present your results. Take care in presenting your solution--how it is packaged and documented, what is required to run it, and how it might integrate with existing tools and generalize to other problems.