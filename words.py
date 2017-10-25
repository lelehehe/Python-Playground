"""
Retrive and print words from a url. This is based 
on https://app.pluralsight.com/player?course=python-fundamentals&author=robert-smallshire&name=python-fundamentals-m03-modularity&clip=10&mode=live

Usage:
    python3 words.py
"""

from urllib.request import urlopen


def fetch_words(url):
    """
    fetch a list of words from a url
    Args:
        url: the url of a utf-8 text document

    Returns:
        a list of string containing the words from the docuemnt.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(words):
    """
    Print each word.

    Args:
        An iterable series.
    """
    for word in words:
        print(word)


def main():
    """ the main function
    """
    url = 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    main()
