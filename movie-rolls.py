import random

####################################################################################################

def movie_night(n, show=True):
    """Pick a movie according to the terrible movie picking rules."""
   
    ## prepare movie sets
    current_movies = set(range(1, n+1))
    eliminated = set()
   
    count = 0
    while len(current_movies) > 1:
       
        ## roll the die
        roll = random.randint(1, n)
 
        if roll in current_movies:
            ## eliminate the movie
            current_movies.remove(roll)
            eliminated.add(roll)
            if show:
                print(f"{roll} is eliminated")
       
        elif roll in eliminated:
            ## revive the movie
            current_movies.add(roll)
            eliminated.remove(roll)
            if show:
                print(f"{roll} is back")
        count += 1
   
    winner = current_movies.pop()
    print(f"\n   ~~ {winner} is the winner after {count} rolls ~~ \n")
 
####################################################################################################

## check whether script is being run directly or imported as a module
if __name__ == "__main__":

    ## continue to prompt user until a valid input is provided
    while True:
        try:
            n = int(input("Enter the number of movies:  "))
            if n <= 0:
                raise ValueError("The number of movies must be a positive integer.")
            break   # escape the `try` block if no errors until here
        except:
            print("Invalid input. Please enter a positive integer.")
   
    movie_night(n)