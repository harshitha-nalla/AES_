import time
import random

def sender():
    frame = 0
    while True:
        print(f"Sender: Sending frame {frame}")
        if random.choice([True, False]):
            print(f"Sender: Frame {frame} sent successfully. Waiting for acknowledgment...")
            time.sleep(1)
            print(f"Sender: Acknowledgment received for frame {frame}")
            frame = 1 - frame
        else:
            print(f"Sender: Frame {frame} lost. Resending...")
        time.sleep(2)

def receiver():
    expected_frame = 0
    while True:
        if random.choice([True, False]):
            print(f"Receiver: Frame {expected_frame} received. Sending acknowledgment...")
            time.sleep(1)
            print(f"Receiver: Acknowledgment sent for frame {expected_frame}")
            expected_frame = 1 - expected_frame
        else:
            print(f"Receiver: Frame {expected_frame} lost. Waiting for retransmission...")
        time.sleep(2)

if __name__ == "__main__":
    print("1-bit Stop-and-Wait Protocol Simulation\n")
    sender()
    receiver()


