from typing import List


def match(
    wishes: List[List[int]],
    preferences: List[List[int]]
) -> List[int]:
    loners = count = _check_count(wishes, preferences)
    matches, proposals, choices = [-1] * count, [0] * count, [-1] * count
    while loners > 0:
        for man in range(count):
            if matches[man] == -1:
                woman = wishes[man][proposals[man]]
                admirer = choices[woman]
                if admirer == -1:
                    matches[man] = woman
                    choices[woman] = man
                    loners -= 1
                elif preferences[woman][man] < preferences[woman][admirer]:
                    matches[man] = woman
                    choices[woman] = man
                    matches[admirer] = -1
                else:
                    proposals[man] += 1
    return matches


def _check_count(wishes: List[List[int]], preferences: List[List[int]]) -> int:
    count = len(wishes)
    if len(preferences) != count:
        raise RuntimeError('Wishes and preferences must be equal')
    for wish, preference in zip(wishes, preferences):
        if len(wish) != count or len(preference) != count:
            raise RuntimeError('Wish and preference must be equal')
    return count
