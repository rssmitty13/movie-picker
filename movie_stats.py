import matplotlib.pyplot as plt
import numpy as np
from movie_rolls import movie_night

###################################################################################################

def run_simulation(n_movies, n_sims=1_000):
    """Run the movie night simulation multiple times and collect results."""
    results = []
    for _ in range(n_sims):
        rolls_needed = movie_night(n_movies, show=False)
        results.append(rolls_needed)
    return np.array(results)

####################################################################################################

if __name__ == "__main__":
    ## prepare to run Monte-Carlo simulations and plot the results
    movie_counts = np.arange(2, 16)
    n_sims = 1_000
    fig, axs = plt.subplots(figsize=(5,7), nrows=2)

    ## run the sims
    for n_movies in movie_counts:
        results = run_simulation(n_movies, n_sims)
        print(f"{n_movies} movies --> {results.mean():.2f} rolls needed on average")
        axs[0].plot(n_movies, results.mean(), 'o')
        axs[1].hist(results, density=False, bins=20, ec='k', alpha=0.5,) # label=f"{n_movies} movies")

    ## customize and save the figure
    axs[0].set_xlabel("# of movies")
    axs[0].set_ylabel("Mean # of rolls")
    axs[0].set_xticks(np.arange(2, 18, 2))
    
    axs[1].set_xlabel("# of rolls")
    axs[1].set_ylabel("Count")

    plt.tight_layout()
    plt.savefig("rolls-count.pdf")
