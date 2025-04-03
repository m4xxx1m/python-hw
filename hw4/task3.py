import multiprocessing as mp
from datetime import datetime
from queue import Empty
import codecs
import time


def print_msg(info, msg=None):
    timestamp = datetime.now().isoformat()
    if msg:
        print(f'[{timestamp}] {info}: {msg}', flush=True)
    else:
        print(f'[{timestamp}] {info}', flush=True)


def a_routine(receive_queue, send_queue):
    while True:
        try:
            msg = receive_queue.get(timeout=1)
            if msg is None:
                break
            send_queue.put(msg.lower())
            time.sleep(5)
        except Empty:
            continue
    send_queue.put(None)
    send_queue.close()


def b_routine(receive_queue, send_queue):
    while True:
        try:
            msg = receive_queue.get(timeout=1)
            if msg is None:
                break
            encoded = codecs.encode(msg, 'rot13')
            print_msg('Encoded in B', encoded)
            send_queue.put(encoded)
        except Empty:
            continue
    send_queue.close()


def main_routine(send_queue):
    try:
        while True:
            user_msg = input()
            print_msg('Main got message from user', user_msg)
            send_queue.put(user_msg)
    except EOFError:
        send_queue.put(None)
        send_queue.close()


if __name__ == '__main__':
    queue_main_to_a = mp.Queue()
    queue_a_to_b = mp.Queue()
    queue_b_to_main = mp.Queue()

    process_a = mp.Process(target=a_routine, args=(queue_main_to_a, queue_a_to_b))
    process_b = mp.Process(target=b_routine, args=(queue_a_to_b, queue_b_to_main))
    process_a.start()
    process_b.start()

    main_routine(queue_main_to_a)

    process_a.join()
    process_b.join()

    print_msg('Program stopped. Output:')
    while True:
        try:
            msg = queue_b_to_main.get_nowait()
            print(msg)
        except Empty:
            break
