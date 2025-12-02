import threading

from config.accounts import ACCOUNTS
from hamster_client import HamsterClient, sleep

clients = [HamsterClient(**options) for options in ACCOUNTS]


def main():
    threads = []

    def worker():
        client.execute()
        sleep(60)

    while True:
        for client in clients:
            t = threading.Thread(target=worker)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
        print(' ')


if __name__ == "__main__":
    main()
