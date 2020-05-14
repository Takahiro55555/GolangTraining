import random
import sys

def random_testcase_generator(length=100):
    result = []
    while len(result) < length:
        val = random.randint(0, 10000000)
        if val in result: continue
        result.append(val)
    result.sort()
    val = random.randint(0, 1000000)
    k = result[length-1] + val

    print(f"{k} {length}")
    print(' '.join(map(str, result)))

    # 正解データを作成
    m = result[-1] - result[0]
    for i in range(1,length):
        m = min(m,result[i-1]+k-result[i])
    print(f"answer: {m}")

def sequential_testcase_generator(length=100):
    result = [i for i in range(length)]
    print(f"{length} {length}")
    print(' '.join(map(str, result)))

    # 正解データを作成（ここは愚直にする）
    k = length
    m = result[-1] - result[0]
    for i in range(1,length):
        m = min(m,result[i-1]+k-result[i])
    print(f"answer: {m}")

def get_option(option, func=lambda x:x):
    before_val = None
    for val in sys.argv:
        if before_val == option:
            return func(val)
        before_val = val

if __name__ == "__main__":
    if get_option("--type") == "seq":
        sequential_testcase_generator(get_option("--len", int))
    elif get_option("--type") == "rand":
        random_testcase_generator(get_option("--len", int))
