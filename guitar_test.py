from guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1992)
    another_guitar = Guitar("Another Guitar", 2013)
    print("{} get_age() - Expected 98. Got {}".format(guitar.name, guitar.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage - Expected Ture. Got {}".format(guitar.name, guitar.is_vintage()))
    print("{} is_vintage - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


if __name__ == '__main__':
    main()
