def decrypt_caesar_bruteforce(ciphertext):
    print(f"🔒 암호문: {ciphertext}\n" + "-"*30)
    
    # 알파벳 대문자 리스트
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # 모든 가능한 키(1~25)를 다 대입해봄 (Brute Force)
    for key in range(1, 26):
        decrypted_text = ""
        for char in ciphertext:
            if char in alphabet:
                # 현재 위치에서 key만큼 뒤로 이동
                idx = alphabet.find(char)
                new_idx = (idx - key) % 26
                decrypted_text += alphabet[new_idx]
            else:
                # 공백이나 특수문자는 그대로 둠
                decrypted_text += char
        
        # 결과 출력 (사람이 보고 말이 되는 문장을 찾음)
        print(f"🔑 Key {key:02d}: {decrypted_text}")

# 님이 만드신 암호문
secret_message = "L ORYH BRX LQ HYHUB XQLYHUVH"
decrypt_caesar_bruteforce(secret_message) 