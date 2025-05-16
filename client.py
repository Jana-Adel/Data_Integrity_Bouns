import hashpumpy # type: ignore
from server import verify # type: ignore

original_message = b"amount=100&to=alice"
original_mac = "614d28d808af46d3702fe35fae67267c"
data_to_append = b"&admin=true"

print("=== Trying key lengths ===")
for key_len in range(10, 26):
    new_mac, new_message = hashpumpy.hashpump(
        original_mac,
        original_message.decode(),
        data_to_append.decode(),
        key_len
    )

    if verify(new_message, new_mac):
        print(f"\n>>> Attack Successful with key length = {key_len}!")
        print("Forged Message:", new_message)
        print("Forged MAC:", new_mac)
        break
else:
    print("\n>>> Attack Failed for all key lengths.")


