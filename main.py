import time

def stop(time_in_seconds: int):
    time.sleep(time_in_seconds)

def main():

    print("I love programming in Python! and I am a cat")
    stop(2)
    print("I want to sleep all day and play with my toys")
    t = time.time()
    local_time = time.localtime(t)
    print("Current time:", local_time)
    
if __name__ == "__main__":
    main()
