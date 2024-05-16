import hashlib
import datetime

# Block class with PoW functionality
class Block:
    def __init__(self, index, data, previous_hash, nonce=0):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.datetime.now()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.index}{self.data}{self.previous_hash}{self.nonce}".encode()).hexdigest()

    def mine(self, target_prefix):
        while not self.hash.startswith(target_prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

# Blockchain class with PoW and no-PoW options
class Blockchain:
    def __init__(self, use_pow, target_prefix="00"):
        self.use_pow = use_pow
        self.target_prefix = target_prefix
        self.chain = []

    def add_block(self, data):
        previous_hash = self.chain[-1].hash if self.chain else None
        new_block = Block(len(self.chain), data, previous_hash)
        if self.use_pow:
            new_block.mine(self.target_prefix)
        self.chain.append(new_block)

    def validate(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].hash != self.chain[i].calculate_hash() or self.chain[i].previous_hash != self.chain[i-1].hash:
                return False
        return True

# Create and tamper with blockchain without PoW
non_pow_chain = Blockchain(False)
for i in range(10):
    non_pow_chain.add_block(f"Block {i + 1}")
print("Original non-PoW chain:", non_pow_chain.chain)

tampered_block = non_pow_chain.chain[1]
tampered_block.data = "Tampered Data"
non_pow_chain.chain[1] = tampered_block

print("Tampered non-PoW chain:", non_pow_chain.chain)

# Create and tamper with blockchain with PoW
pow_chain = Blockchain(True)
for i in range(10):
    pow_chain.add_block(f"Block {i + 1}")
print("Original PoW chain:", pow_chain.chain)

tampered_block = pow_chain.chain[1]
tampered_block.data = "Tampered Data"
pow_chain.chain[1] = tampered_block

try:
    pow_chain.validate()
    print("Tampered PoW chain accepted?! (This should not happen)")
except:
    print("Tampering detected in PoW chain!")

# Test different difficulty levels (prefix length)
for prefix_length in range(1, 5):
    target_prefix = "0" * prefix_length
    pow_chain = Blockchain(True, target_prefix)

    start_time = datetime.datetime.now()
    for i in range(10):
        pow_chain.add_block(f"Block {i + 1}")
    end_time = datetime.datetime.now()

    print(f"Difficulty level: {prefix_length} '0' prefix")
    print(f"Mining time: {end_time - start_time}")

