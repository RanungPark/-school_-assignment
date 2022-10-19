import collections
import string

# 파일을 열고 평문을 읽어 소문자로만든다
with open("original_text.txt", "r") as f:
    plain_text = f.read().lower()
    plain_text_list = list(plain_text)

# collection내부라이브러리를 이용하여 ket count하기
key_count = collections.Counter(plain_text_list)
# 알파벳이 아니면 제거하기
for char in list(key_count):
    if not char.isalpha():
        del key_count[char]

# 키 딕셔너리로 정렬하기
sort_key_dict = {k: v for k, v in sorted(key_count.items(), key=lambda item: item[1], reverse=True)}

# 키값 파일에 적기
with open("key_count.txt", "w") as f:
    f.write(str(sort_key_dict))

sort_key_list = list(sort_key_dict)
alphabet_list = list(string.ascii_lowercase)

# 키와 중복되는 알파벳 제거하기
for alphabet in alphabet_list:
    if alphabet not in sort_key_dict:
        alphabet_list.remove(alphabet)

# 일대일 대응 딕셔너리
correspond_alphabet_dict = dict(zip(alphabet_list, sort_key_list))

# 암호화하기
for idx, text in enumerate(plain_text_list):
    if text in correspond_alphabet_dict:
        plain_text_list[idx] = correspond_alphabet_dict[text]

# 암호문에서 ''없이 연결하기
cipher_text = ''.join(plain_text_list)

# 암호문 파일에 쓰기
with open("cipher_text.txt", "w") as f:
    f.write(cipher_text)

# 반대로 일대일 대응하기
correspond_alphabet_dict = dict(zip(sort_key_list, alphabet_list))
cipher_text_list = list(cipher_text)

# 복호화하기
for idx, text in enumerate(cipher_text_list):
    if text in correspond_alphabet_dict:
        cipher_text_list[idx] = correspond_alphabet_dict[text]

# 복호문에서 ''없이 연결하기
decryption_text = ''.join(cipher_text_list)

# 복호문 파일에 쓰기
with open("decryption_text.txt", "w") as f:
    f.write(decryption_text)
