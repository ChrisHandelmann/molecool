"""
functions.py
A python package for analyzing and visualzing xyz files.

Handles the primary functions
"""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "This code is a mole of cool."
    if with_attribution:
        quote += "\n\t- Adapted from BennyP"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
