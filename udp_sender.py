import socket
import time

def send_udp_message(message, host, port):
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # Send the message to the specified host and port
        client_socket.sendto(message.encode('utf-8'), (host, port))

if __name__ == "__main__":
    # Set the host and port of the UDP server
    server_host = "192.168.1.12"  # Replace with the actual server IP
    server_port = 4444         # Replace with the actual server port

    # Message to be sent
    message_to_send = "Hello, UDP Server!"

    # Send the UDP message
    while(1):
        time.sleep(1)
        send_udp_message(message_to_send, server_host, server_port)
