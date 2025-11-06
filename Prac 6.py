import heapq
import math
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
def huffman_codes(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    root = heap[0]
    codes = {}
    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")
    generate_codes(root, "")
    return codes
if __name__ == "__main__":
    char_freq = {
        'a': 5,
        'b': 9,
        'c': 12,
        'd': 13,
        'e': 16,
        'f': 45
    }
    print("Character Frequencies:", char_freq)
    n = len(char_freq)
    bits_per_char = math.ceil(math.log2(n))
    total_chars = sum(char_freq.values())
    before_cost = total_chars * bits_per_char
    print(f"\nBefore Encoding Cost: {before_cost} bits (each char = {bits_per_char} bits)")
    codes = huffman_codes(char_freq)
    after_cost = sum(len(codes[char]) * freq for char, freq in char_freq.items())
    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(f"{char}: {code}")
    print(f"\nAfter Encoding Cost: {after_cost} bits")
    compression_ratio = after_cost / before_cost
    print(f"\nCompression Ratio: {compression_ratio:.2f}")
