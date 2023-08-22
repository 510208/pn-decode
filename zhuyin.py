import argparse

# 建立一个完整的一对一映射表
mapping = {
    '1': 'ㄅ',
    '2': 'ㄉ',
    '3': 'ˇ',
    '4': 'ˋ',
    '5': 'ㄓ',
    '6': 'ˊ',
    '7': '˙',
    '8': 'ㄚ',
    '9': 'ㄞ',
    '0': 'ㄢ',
    '-': 'ㄦ',
    'q': 'ㄆ',
    'w': 'ㄊ',
    'e': 'ㄍ',
    'r': 'ㄐ',
    't': 'ㄔ',
    'y': 'ㄗ',
    'u': 'ㄧ',
    'i': 'ㄛ',
    'o': 'ㄟ',
    'p': 'ㄣ',
    'a': 'ㄇ',
    's': 'ㄋ',
    'd': 'ㄎ',
    'f': 'ㄑ',
    'g': 'ㄕ',
    'h': 'ㄘ',
    'j': 'ㄨ',
    'k': 'ㄜ',
    'l': 'ㄠ',
    ';': 'ㄤ',
    'z': 'ㄈ',
    'x': 'ㄌ',
    'c': 'ㄏ',
    'v': 'ㄒ',
    'b': 'ㄖ',
    'n': 'ㄙ',
    'm': 'ㄩ',
    ',': 'ㄝ',
    '.': 'ㄡ',
    '/': 'ㄥ'
}

def zhuyin_to_english(input_str):
    output_str = ""
    for char in input_str:
        if char in mapping:
            output_str += mapping[char]
        else:
            output_str += char
    return output_str

def english_to_zhuyin(input_str):
    output_str = ""
    for char in input_str:
        for key, value in mapping.items():
            if char == value:
                output_str += key
                break
        else:
            output_str += char
    return output_str

def main():
    parser = argparse.ArgumentParser(description="Translate between Zhuyin and English characters.")
    parser.add_argument("input_string", help="The input string to be translated.")
    parser.add_argument("-t", "--to_zhuyin", action="store_true", help="Translate to Zhuyin.")
    parser.add_argument("-e", "--to_english", action="store_true", help="Translate to English.")
    
    args = parser.parse_args()
    
    input_str = args.input_string
    
    if args.to_zhuyin:
        result = english_to_zhuyin(input_str)
        print("=" * 20)
        print(result)
        print("=" * 20)
    elif args.to_english:
        result = zhuyin_to_english(input_str)
        print("=" * 20)
        print(result)
        print("=" * 20)
    else:
        print("Please specify translation direction with -t or -e.")
        
if __name__ == "__main__":
    main()
