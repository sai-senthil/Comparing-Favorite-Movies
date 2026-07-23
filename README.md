This project uses Python, Pandas, and Matplotlib to analyze movie data from Rotten Tomatoes. It compares my favorite movie, Avengers: Infinity War, with other Action & Adventure movies in the dataset by calculating statistics and creating visualizations.

The program demonstrates how data can be filtered, analyzed, and displayed using graphs to better understand how one movie compares to others in its genre.

Features
Loads movie data from a CSV file using Pandas.
Stores and displays information about my favorite movie.
Filters the dataset to only include Action & Adventure movies.
Calculates:
Minimum audience rating
Maximum audience rating
Mean audience rating
Median audience rating
Compares my favorite movie's audience rating with these statistics.
Creates a histogram showing the distribution of audience ratings.
Creates a scatter plot comparing audience ratings and critic ratings.
Provides written explanations of each visualization.
Technologies Used
Python
Pandas
Matplotlib
Dataset

The project uses the rotten_tomatoes_movies.csv dataset, which contains:

Movie title
Year released
Critic rating
Audience rating
Genres

The original dataset was created by Stefano Leone and published on Kaggle under the CC0 Public Domain License.

How to Run
Download or clone this repository.
Make sure Python is installed.

Install the required libraries if needed:

pip install pandas matplotlib

Run the program:

python main.py
What I Learned

Through this project, I practiced:

Reading CSV files with Pandas
Filtering data using .loc
Calculating descriptive statistics
Creating histograms and scatter plots
Interpreting data visualizations
Writing clean, organized Python code
Future Improvements
Compare multiple favorite movies.
Add more genres for comparison.
Create additional charts such as box plots or bar graphs.
Allow the user to choose a movie and genre as input.
Attribution

Dataset:
Rotten Tomatoes Movies and Critic Reviews Dataset by Stefano Leone (Kaggle, CC0 Public Domain).

All program code was written by me for this educational project.
