# link_challenge

This directory includes:

titles.tsv

directors.tsv

actors.tsv

titles_AKA.tsv

names_AKA.tsv

These are all tab-separated files enclosed in quotes. They should be UTF-8 encoded, but some upstream encodings (Cyrillic and 
Chinese) may result in garbled text.

The file titles.tsv contains a 'movie_id', primary title, and 'production year' of a lot of movies. A film is often released in its production year in its home market, but may be released later. The 'movie_id' is used to key to the other tables. The file directors.tsv contains a person id, the movie id, name and gender of directors. A film may have zero, one, or many directors. The gender might be NA. The person id keys into the names_AKA.tsv. The file actors.tsv contains acts-in information for actors and actresses, with person id, movie id, primary name, and gender. Again, the movie id keys into the titles.tsv table, and the person id keys into the names_AKA.tsv. The titles_AKA.tsv file contains 'also known as' (AKA) titles for films--alternate titles in other markets and other languages, working titles, short titles, misspellings and so on. The file names_AKA.tsv contains alternate names for people (directors, actors and actresses). These are aliases, alternate spellings, other language renderings, and so on. The person id keys to the directors.tsv and actors.tsv tables.

If you knew some things about a film--the title, approximate year released, name of the director and some actors, you could use these data tables to find the movie_id and link to other data about the film, which are also keyed to the movie_id. This is your challenge.

In the tar file you should also find a directory of around 500 nyt movie reviews, taken from an obscure publication found sporadically on the east coast. These are raw html files. The job is to produce a list of links from html file name to movie_id. For example, if rendered as a csv, the lookup should probably include the lines:

file,movie_id

./nyt/2007/07/25/movies/25arct.html,60749

./nyt/2007/12/14/movies/14warh.html,26848

./nyt/2007/10/20/movies/20sara.html,615746

Not every movie reviewed will have a hit in the titles.tsv data. You can omit those files from your results, or list their movie_id as 'NA'. While a search on title is likely to be pretty good, titles are not unique over the years, and you may get a false match: using director and actor information is likely to improve the matching.

The point of this exercise is not just to produce this file of links. In fact, the file of links is possibly irrelevant. The goal is to see how you approach a problem, how you write code, and how you present your results. Take care in presenting your solution--how it is packaged and documented, what is required to run it, and how it might integrate with existing tools and generalize to other problems.

------------------

SOLUTION APPROACH

I just wanted to say up front that I was not (so far) able to produce the correct file of links. However, I did want to describe 
how I approached the problem and the corresponding Python code that I wrote.

In order to facilitate the presentation of my approach to solving this coding problem, I've created and used a Python notebook file called "CoreCast_Challenge_Yashar.ipynb" with headings and comment lines, which you can find and access at https://github.com/markyashar/link_challenge/.

In working on this problem with Python, I utilized a number of different libraries/modules, including Pandas, Beautiful Soup, and csv. Below I describe the various steps in my approach in attempting to solve this problem (all of which is included in the Python notebook file):

(1) Loading, reading in, and displaying the given tab-separated data files: I loaded and read in the provided tab-separated data files (i.e., titles.tsv, directors.tsv, actors.tsv, etc.) into Pandas DataFrame objects and then displayed each of them separately within the Python notebook (see, e.g., 'In [4]', 'In [5]', and 'In [6]' in the Python notebook).

(2) Combining tab-separated data sets together with Pandas using various keys: I used Pandas merge operations to combine the data sets by linking rows using various keys such as 'movie_id', or 'person_id'. The results of each of these merges are displayed in the Python notebook (e.g., In [10], Out[10] , etc.)

(3) Writing the resulting merged data file to a CSV file ('merged_data.csv'): I then wrote the final result of the merged data sets, as described in step 2 above, to an output CSV file called "merged_data.csv", which is displayed in the Python notebook (e.g., 'In[63], 'Out[63]', etc.) and can also be found at https://github.com/markyashar/link_challenge/.

At this point, I'd like to point out that all of the technical details in the code and output may not be correct here -- there would be a need for more debugging and trouble-shooting. Again, I am trying to emphasize here the general approach, methods, and algorithm(s) that I've used towards the solution of this problem.

(4) Loading, reading in, and displaying a raw HTML movie review file (e.g., '25arct.html'): I used various python modules/libraries including BeautifulSoup and urllib(2) to load/read in and display the raw (local) HTML movie review files that I had downloaded.

(5) Extracting and parsing data from the raw HTML files, then writing out and appending the extracted data to a CSV file ('html_extracted.csv'): I performed web scraping operations on the HTML files to extract the relevant HTML tags, e.g.,

<meta content="20070725" name="pdate"/>
<meta content="Arctic Tale (Movie)" name="ttl"/>
...  
<meta content="Queen Latifah" name="per"/>

See, e.g., 'In [19]' in the python notebook. Specifically, I searched for, parsed through, and extracted the production dates, titles, and actors playing in the films being reviewed using the "pdate", "ttl", and "per" tags, respectively, for each HTML file, and then wrote and appended that data to a file called 'html_extracted.csv', as displayed in the Python notebook ('Out[21]'). It can also be found in the same Github directory that I pointed out earlier.

Note that I only wrote out the extracted data for three different HTML files for demonstration purposes. In reality, we would needto loop/iterate through all of the different (local) HTML files and extract and append the data to the 'html_extracted.csv' file and the associated Pandas DataFrame object. I left this for further future debugging and troubleshooting. Here, again, I am focusing more on the general approach, methods, and algorithms.

(6) Combining data from merged tab separated files with merged/combined data extracted from HTML files and writing all of this combined data to a separate file ('link_list_lookup.csv'): Next, we combine/merge the already merged data from the tab separated files ('merged_data.csv) with the relevant merged HTML data ('html_extracted.csv') using the appropriate key to link the rows, and we load and read that resulting merged data into another DataFrame object and write the output to another CSV file called 'link_list_lookup.csv', which is also displayed in the Python notebook ('Out[35]'). 

(7) Final Step: Extracting the HTML link file name and 'movie_id' data from 'link_list_lookup.csv' and writing those data columns to 'link_list_lookup_final.csv' in format suggested in coding problem statement: As a final step, I've extracted the HTML linked file names and 'movie_id' data in the 'link_list_lookup.csv' file that was created in step (6) above, and wrote those extracted data columns to another file called 'linked_list_lookup_final.csv' in the format suggested in the coding problem statement. See 'In [58]' in the Python notebook. This final result file is also displayed in the Python notebook ('Out[58]') and can be found in the same GitHub directory. 

Again, the content of my final list of links and movie_id data is clearly incorrect. My emphasis here was more on the approach andmethods used and how I've presented that information to you.



