BUFFER_SIZE = 1024
MAX_SEQ = 7

class Frame:
    def __init__(self, seq, data):
        self.seq = seq
        self.data = data

def send_frame(frame):
    # Simulated send logic (for demo purposes)
    print(f"Sending frame with sequence number: {frame.seq}")

def sliding_window_sender(message):
    window_size = 4
    frames = [Frame(seq, message[i:i + BUFFER_SIZE]) for i, seq in enumerate(range(0, len(message), BUFFER_SIZE))]
    current_frame = 0

    while current_frame < len(frames):
        print("Transmitting frames:")
        for i in range(current_frame, min(current_frame + window_size, len(frames))):
            send_frame(frames[i])

        # Simulated acknowledgment (for demo purposes)
        print(f"Acknowledgment received for frame with sequence number: {frames[current_frame].seq}")
        current_frame += 1

if __name__ == "_main_":
    message = "This is a test message for the sliding window protocol."
    sliding_window_sender(message)