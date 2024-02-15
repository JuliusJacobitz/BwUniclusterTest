import time

def project_main():
    # open a text file and write current time to it
    with open('time.txt', 'w') as f:
        f.write(str(time.time()))

if __name__ == "__main__":
    project_main()