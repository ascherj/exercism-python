def is_pangram(sentence: str):
    cleaned = [char.lower() for char in sentence if char.isalpha()]

    counts = {}
    for char in cleaned:
        counts[char] = counts.get(char, 0) + 1
    return len(counts) == 26
