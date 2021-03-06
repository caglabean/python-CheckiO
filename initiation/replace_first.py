from typing import Iterable


def replace_first(items: list) -> Iterable:
    # Use slicing to modify the list
    if(items == []):
        return items
    else:
        return (items[1:]+[items[0]])   # Concatenate two lists


if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
