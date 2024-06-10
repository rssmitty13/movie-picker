# movie-picker

Having trouble deciding what to watch when you have a movie night with your friends or family?
Have everyone bring a few movie ideas, and _Movie Picker_ will do the rest!

Here's what to do:

1. Assign each movie a number
2. Run `python3 movie-rolls.py`
3. Provide the total number of movies on your list
4. Profit

Sounds like you could do that with a single die roll or random number generator, right?
Of course!
However, you must be approaching this as someone who wants to get to the movie quickly.
That's boring.
We need more drama.

Let's define the rules of the movie picking game:

- Each movie is assigned a number
- Roll the (appropriately sided) die
- The resulting number's movie is eliminated from the watch list
- Repeat until just a single number remains
- Watch that movie!

This will take several rolls, thereby keeping everybody on the edge of their seat and leading to a fun time with friends.

What if, instead, you wanted to maximally annoy your friends and make sure nobody has fun?
Perhaps you could even prevent a movie from ever being picked.
Here's how to do that:

- Use the same rules as above
- BUT reintroduce eliminated movies back into the watch list if their number is rolled again

Sounds simple, but it can quickly destroy friendships.

## Quantifying the Inefficiency

To demonstrate how inefficient and annoying this method can be for larger numbers of movies, we can use a Monte Carlo simulation to determine the distribution of the number of rolls necessary to finish the game for different numbers of movies.

To run the simulations and generate the figure:

1. Ensure that `movie-rolls.py` is in the same directory as `movie-stats.py`.
2. Install the required packages if you haven't already:

    ```sh
    pip install matplotlib numpy
    ```

3. Run `movie-stats.py`:

    ```sh
    python3 movie-stats.py
    ```

The `movie-stats.py` script runs multiple simulations for different numbers of movies, collects the results, and generates a figure showing:

- The mean number of rolls needed to finish the game for different numbers of movies.
- The distribution of rolls needed for each scenario.

This visualization helps to quantify the inefficiency and adds more drama to the movie picking process, highlighting how it can keep participants on the edge of their seats—or drive them crazy with suspense!

## Example Output

After running the `movie-stats.py` script, you will see a figure saved as `rolls-count.pdf`. This figure contains:

- A plot of the mean number of rolls needed for different numbers of movies.
- Histograms showing the distribution of rolls needed for each number of movies, with a probability density function overlay.

This additional script provides a fun and analytical way to demonstrate the complexity and potential frustration of the movie picking game.

Enjoy your movie night, and may the best movie win!
