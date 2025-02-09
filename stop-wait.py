import time
import random
import threading

# Shared state to keep track of frame and acknowledgment
frame = 0
ack_received = False


# Sender function
def sender(max_frames):
    global frame, ack_received
    for _ in range(max_frames):
        print(f"Sender: Sending frame {frame}")
        if random.choice([True, False]):  # Simulate frame loss or success
            print(f"Sender: Frame {frame} sent successfully. Waiting for acknowledgment...")
            time.sleep(1)
            ack_received = True
            print(f"Sender: Acknowledgment received for frame {frame}")
            frame += 1  # Move to next frame
        else:
            print(f"Sender: Frame {frame} lost. Resending...")
        time.sleep(2)


# Receiver function
def receiver(max_frames):
    global frame, ack_received
    for _ in range(max_frames):
        time.sleep(2)  # Ensure receiver only processes after sender has sent a frame
        if random.choice([True, False]):  # Simulate receipt success or loss
            print(f"Receiver: Frame {frame} received. Sending acknowledgment...")
            ack_received = False  # Reset acknowledgment for sender
            print(f"Receiver: Acknowledgment sent for frame {frame}")
        else:
            print(f"Receiver: Frame {frame} lost. Waiting for retransmission...")


if __name__ == "__main__":
    max_frames = 10  # Set the number of frames to simulate
    print("1-bit Stop-and-Wait Protocol Simulation\n")

    # Create and start sender and receiver threads
    sender_thread = threading.Thread(target=sender, args=(max_frames,))
    receiver_thread = threading.Thread(target=receiver, args=(max_frames,))

    sender_thread.start()
    receiver_thread.start()

    sender_thread.join()
    receiver_thread.join()

    print("Simulation completed.")
