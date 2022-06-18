# Copyright 2022 Masamichi J. Miyama

from concurrent import futures
import numpy as np
import openjij as oj


def optimize(Q: np.ndarray):
    sampler = oj.SASampler()
    return sampler.sample_qubo(Q, num_reads=1000)


def main():
    N: int = 1000
    D: int = 10

    Qs: np.ndarray = [np.random.normal(0.0, 1.0, (N, N)) for _ in range(D)]

    with futures.ProcessPoolExecutor(max_workers=4) as e:
        result = list(e.map(optimize, Qs))

    print(result)


if __name__ == "__main__":
    main()
