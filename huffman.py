# Implementação de Codificação de Huffman


import heapq     
from collections import Counter  

# Node representa um nó na árvore de Huffman
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq    # frequência acumulada deste nó/subárvore
        self.char = char    # caractere armazenado (caso seja folha)
        self.left = left    # filho esquerdo
        self.right = right  # filho direito

    def __lt__(self, other):
        # necessário para comparar nós pela frequência na heap
        return self.freq < other.freq

def build_huffman_tree(text):

    frequencia = Counter(text)
    heap = [Node(freq, char) for char, freq in frequencia.items()]
    heapq.heapify(heap)

    # se houver apenas um caractere distinto, cria raiz extra para permitir codificação
    if len(heap) == 1:
        only = heap[0]
        return Node(only.freq, None, left=only)

    while len(heap) > 1:
        # remove os dois nós de menor frequência
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        # cria nó interno com soma das frequências
        merged = Node(node1.freq + node2.freq, None, left=node1, right=node2)
        heapq.heappush(heap, merged)

    return heap[0]  # raiz da árvore

def build_codes(node, prefixo="", code_map=None):

    if code_map is None:
        code_map = {}
    if node.char is not None:
        # nó folha: armazena código; usa '0' se only one leaf
        code_map[node.char] = prefixo or "0"
    else:
        if node.left:
            build_codes(node.left,  prefixo + "0", code_map)
        if node.right:
            build_codes(node.right, prefixo + "1", code_map)
    return code_map

def huffman_encoding(text):

    arvore = build_huffman_tree(text)
    codes = build_codes(arvore)
    encoded = "".join(codes[ch] for ch in text)
    return encoded, codes, arvore

def huffman_decoding(encoded, codes):

    inv_codes = {code: char for char, code in codes.items()}
    decoded_chars = []
    teste = ""
    for bit in encoded:
        teste += bit
        if teste in inv_codes:
            decoded_chars.append(inv_codes[teste])
            teste = ""
    return "".join(decoded_chars)

def compression_stats(text, encoded):

    original_bits   = len(text) * 8
    compressed_bits = len(encoded)
    rate            = compressed_bits / original_bits
    saving_percent  = (original_bits - compressed_bits) / original_bits * 100
    return original_bits, compressed_bits, rate, saving_percent

# Demonstração de uso
if __name__ == "__main__":
    sample = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    enc, codes, _ = huffman_encoding(sample)
    print("Texto Original:   ", sample)
    print("Códigos:          ", codes)
    print("Texto Codificado: ", enc)
    dec = huffman_decoding(enc, codes)
    print("Texto Decodificado:", dec)
    stats = compression_stats(sample, enc)
    print(f"Tamanho Original (bits):   {stats[0]}")
    print(f"Tamanho Comprimido (bits): {stats[1]}")
    print(f"Taxa de Compressão:        {stats[2]:.2f}")
    print(f"Ganho de Espaço:           {stats[3]:.2f}%")
