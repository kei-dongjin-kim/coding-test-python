class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        population = [0] * 2051

        for birth, death in logs:
            population[birth] += 1
            population[death] -= 1

        max_population = 0
        year = 1950
        current = 0

        for i in range(1950, 2051):
            current += population[i]
            if current > max_population:
                max_population = current
                year = i

        return year