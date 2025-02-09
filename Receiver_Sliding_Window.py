class SlidingWindow:
    def _init_(self, window_size):
        self.window_size = window_size
        self.base = 0  # First frame in window
        self.next_seq = 0  # Next frame to send
        self.buffer = []  # Buffer for frames
        self.ack_received = []  # Track received acknowledgments

    def send_data(self, data):
        print(f"\nSending data with window size: {self.window_size}")
        self.buffer = list(data)
        total_frames = len(data)

        while self.base < total_frames:
            # Send frames within window
            while self.next_seq < total_frames and self.next_seq < self.base + self.window_size:
                self.send_frame(self.next_seq)
                self.next_seq += 1

            # Simulate receiving ACK
            ack = self.receive_ack()
            if ack >= 0:
                self.handle_ack(ack)
            else:
                self.handle_timeout()

            self.print_window_status()

    def send_frame(self, seq_num):
        print(f"Sending Frame {seq_num}: {self.buffer[seq_num]}")

    def receive_ack(self):
        # Simulate ACK reception (could be modified for real network)
        import random
        if random.random() < 0.15:  # 15% chance of timeout/loss
            return -1
        return self.base

    def handle_ack(self, ack):
        print(f"Received ACK for frame {ack}")
        self.base = ack + 1
        self.ack_received.append(ack)

    def handle_timeout(self):
        print(f"\nTimeout occurred! Resending frames from {self.base}")
        self.next_seq = self.base

    def print_window_status(self):
        print("\nWindow Status:")
        print(f"Base: {self.base}")
        print(f"Next Sequence: {self.next_seq}")
        print("Current Window:", end=" ")
        for i in range(self.base, min(self.base + self.window_size, len(self.buffer))):
            print(self.buffer[i], end=" ")
        print("\n" + "-" * 50)


def main():
    # Test the sliding window protocol
    window_size = 4
    data = "ABCDEFGHIJKLMNOP"  # Test data

    print("Sliding Window Protocol Simulation")
    print("Data to send:", data)
    print("Window size:", window_size)

    protocol = SlidingWindow(window_size)
    protocol.send_data(data)

    print("\nTransmission Complete!")
    print("Successfully sent frames:", sorted(set(protocol.ack_received)))

