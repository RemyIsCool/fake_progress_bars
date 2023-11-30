# Fake Progress Bars

I don't know why you'd want to, but now you can make fake progress bars.

```python
from fake_progress_bars import progress_bar

# Creates a 10 second default progress bar.
progress_bar(10)

# Creates a 10 second customized progress bar.
progress_bar(time=10, size=200, step=2, label='Example', variability=0.1,
    progress='◼️', remaining='·', outside='⏺', percentage=False)
```

All configuration options:

-   **time**: The amount of time the progress bar takes to complete.
-   **size**: The size of the progress bar in characters.
-   **step**: The amount the progress increases every step.
-   **label**: The label before the progress bar, succeeded by ": ".
-   **variability**: The amount of change allowed in the time of each step. This property is limited to the time times the step divided by the size to keep the time consistent.
-   **progress**: The character used to represent the current progress of the progress bar.
-   **remaining**: The character used for the remaining percentage of the progress bar.
-   **outside**: The character used as the border on either side of the progress bar.
-   **percentage**: Whether the percentage competed should be shown on the right side of the progress bar.
