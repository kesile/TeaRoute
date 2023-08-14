import threading
import json, random, time

def trainFile(file, file_path, instructions, chatFunction, embedFunction, batch_size):
    iterator = 0
    cost = 0

    while iterator < len(file):
        threads = []

        for i in range(iterator, min(iterator + batch_size, len(file))):
            thread = threading.Thread(target=chatFunction, args=(file[i], file_path, instructions, True))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        smallCost = round(batch_size*random.randint(290,310)*(0.002/1000),5)
        cost += smallCost

        # print(f"Epoch {1 + iterator//batch_size}/{(len(file) + batch_size - 1)//batch_size} ~ {smallCost}$")
        iterator += batch_size
        code = 200

    return code, cost
    



