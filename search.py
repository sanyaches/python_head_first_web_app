def search4vowels(phrase: str) -> set:
    """Search vowels in 'phrase'"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aoeiu') -> set:
    """Search all 'letters' in 'phrase'"""
    return set(letters).intersection(set(phrase))
