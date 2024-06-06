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

**...continue...**