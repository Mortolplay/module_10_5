import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding="utf-8") as file:
        while True:
            data = file.readlines()
            all_data.append(data)
            if not data:
                break

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_time = time.time()
    for i in filenames:
        read_info(i)
    end_time = time.time()
    print(end_time - start_time, "(линейный)")
    start_time = time.time()
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(end_time - start_time, "(многопроцессный)")