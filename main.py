#Part 1 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Avengers: Infinity War"
print("My favorite movie is " + favMovie);



#Part 2 Investigate the data
#print(movieData.head()) - prints first 5 rows
#print(movieData["movie_title"]) - prints title column

#Part 3 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)
favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)


print("\n\n")

#Create a new variable to store a new data set with a certain genre
actionMovieBooleanList = movieData["genres"].str.contains("Action & Adventure")

actionMovieData = movieData.loc[actionMovieBooleanList]


numOfMovies = actionMovieBooleanList.shape[0] #returns total number of rows


print("We will be comparing " + favMovie +
      " to other movies under the genre Action & Adventure in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Action & Adventure.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 4 Describe data
#min
min = actionMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 91 points higher than the lowest rated movie.")
print()

#find max
max = actionMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 7 points lower than the highest rated movie.")
print()

#find mean
mean = actionMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " lower than the mean movie rating.")
print()

#find median
median = actionMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " lower than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 5 Create graphs
#Create histogram
plt.hist(actionMovieData["audience_rating"], range = (0, 100), bins = 20) # bins - how many intervals data is divided into

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Action & Adventure Movies")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Action & Adventure Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most of the audience ratings are between 50 and 80, creating a roughly bell-shaped distribution with few very low or very high ratings."
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

#Create scatterplot
plt.scatter(data = actionMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Reading")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between audience ratings and critic ratings, meaning movies with higher audience ratings tend to have higher critic ratings."
)
print()


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
