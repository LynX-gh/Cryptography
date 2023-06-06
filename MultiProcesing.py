import sympy as smp
from multiprocessing import Process, pool


def test(e: int, s: int = 0) -> int:
    passed_case = 0
    for i in range(s, e):
        if not smp.isprime(i):
            passed_case += 1
    return passed_case


if __name__ == "__main__":
    cases = [(100000, 2), (200000, 100001), (300000, 200001),
             (400000, 300001), (500000, 400001), (600000, 500001),
             (700000, 600001), (800000, 700001), (900000, 800001), (1000000, 900001)]
    with pool.Pool(16) as p:
        res = p.starmap_async(test, cases)
        p.close()
        p.join()
    print(f"Success Rate = {(sum(res.get())/1000000)*100} %")
