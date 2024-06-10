# import matplotlib.pyplot as plt
import numpy as np
from movie_rolls import movie_night

###################################################################################################

def run_simulation(n_movies, n_sims=1_000):
    """Run the movie night simulation multiple times and collect results."""
    results = []
    for _ in range(n_sims):
        rolls_needed = movie_night(n_movies, show=False)
        results.append(rolls_needed)
    return results

# def plot_results(n_movies, results):
#     """Plot the distribution of the number of rolls needed."""
#     plt.hist(results, bins=30, edgecolor='black')
#     plt.title(f"Distribution of Rolls Needed for {n_movies} Movies")
#     plt.xlabel("Number of Rolls")
#     plt.ylabel("Frequency")
#     plt.show()

####################################################################################################

if __name__ == "__main__":
    movie_counts = np.arange(2, 16)
    n_sims = 1_000

    for n_movies in movie_counts:
        results = run_simulation(n_movies, n_sims)
        # plot_results(n_movies, results)
        print(f"{n_movies} movies --> {np.mean(results):.2f} rolls needed on average")
