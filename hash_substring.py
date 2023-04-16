def read_input():
    inn = input().rstrip()
    if "I" in inn:
        pattern = input().rstrip()
        text = input().rstrip()
    elif "F" in inn:
        with open ('06') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    pattern_hash = hash(pattern)
    pattern_length = len(pattern)
    text_length = len(text)
    
    if pattern_length > text_length:
        return occurrences

    text_hash = hash(text[:pattern_length])

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+pattern_length]:
                occurrences.append(i)

        if i < text_length - pattern_length:
            text_hash = hash(text[i+1:i+pattern_length+1])

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
