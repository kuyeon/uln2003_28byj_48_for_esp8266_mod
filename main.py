from uln2003 import Stepper

in1 = 16
in2 = 5
in3 = 4
in4 = 0
delay = 1
mode = 0 # 0 for half step, 1 for full step

def main() -> None:
    import time
    s1 = Stepper(in1, in2, in3, in4, delay, mode)
    # s1.step(100)
    # s1.step(100,-1)
    s1.angle(360, 1)
    time.sleep(3)
    s1.angle(360,-1)
    
if __name__ == "__main__":
    main()