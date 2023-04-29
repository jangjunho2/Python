from time import sleep
from multiprocessing import Pool


def start_function_for_process(n):
    result_sent_back_to_parent = n*n
    return result_sent_back_to_parent


if __name__ == '__main__':  # 멀티프로세싱을 사용하려면 꼭 넣자 안쓰면 난리남
    print("hi")
    with Pool(processes=2) as p:
        result = p.map(start_function_for_process, range(200), chunksize=10)
    print(result)

# 참고한 유트브: https://www.youtube.com/watch?v=s1SkCYMnfbY&ab_channel=Programming
