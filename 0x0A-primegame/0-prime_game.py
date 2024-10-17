#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x: int, nums: list) -> str:
    def sieve_of_eratosthenes(n):
        """ Returns a list of prime numbers up to n using Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        primes = []
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes

    def play_game(n):
        """ Simulate the game for a single round with n numbers """
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        remaining_numbers = set(range(1, n + 1))

        while primes:
            prime = primes.pop(0)
            if prime not in remaining_numbers:
                continue
            # Remove prime and its multiples
            for multiple in range(prime, n + 1, prime):
                remaining_numbers.discard(multiple)
            turn = 1 - turn  # Switch turns

        # If turn is 0, Maria lost (Ben made the last move)
        return "Ben" if turn == 0 else "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
