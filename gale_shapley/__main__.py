from random import sample
from gale_shapley.matches import match

count = 10

nums = range(count)

wishes = [sample(nums, count) for i in nums]

print('\n'.join(list(map(str, wishes))), '\n\n')

preferences = [sample(nums, count) for j in nums]

print('\n'.join(list(map(str, preferences))), '\n\n')

print(match(wishes, preferences))
