import time


def main():
    i = 0
    while True:
        print('third try: {}'.format(i))
        i += 1
        time.sleep(1)


if __name__ == "__main__":
    main()
