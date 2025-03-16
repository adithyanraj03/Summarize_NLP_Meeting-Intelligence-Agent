import sys
import time

def loading_animation():
    animation = "|/-\\"
    idx = 0
    while True:
        sys.stdout.write("\r" + "Loading " + animation[idx % len(animation)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)

if __name__ == "__main__":
    loading_animation()
