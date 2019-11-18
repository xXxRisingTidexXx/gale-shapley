from typing import List


def match(
    offers: List[List[int]],
    preferences: List[List[int]]
) -> List[int]:
    _check_count(offers, preferences)

    return []


def _check_count(offers: List[List[int]], preferences: List[List[int]]):
    count = len(offers)
    if len(preferences) != count:
        raise RuntimeError('Offers and preferences must be equal')
    for offer, preference in zip(offers, preferences):
        if len(offer) != count or len(preference) != count:
            raise RuntimeError('Offers and preferences must be equal')
