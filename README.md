Project: Basic Cryptography & Brute-Force Simulation
배경 (Context): 암호학 기초를 학습하며, 고전 암호인 카이사르 암호(Caesar Cipher)의 원리를 파악하고자 했습니다.

수행 내용 (Action):

Python을 이용하여 암호화 및 복호화 알고리즘을 직접 구현.

키(Key)를 모르는 상황을 가정하여, 가능한 모든 키(Key Space 1~25)를 대입하는 무차별 대입 공격(Brute-Force Attack) 스크립트 작성.

결과 및 시사점 (Result & Insight):

Key 03에서 평문("I LOVE YOU...")이 노출됨을 확인.

[Insight] 키 공간(Key Space)이 작은 암호 알고리즘은 현대 컴퓨팅 환경에서 순식간에 무력화될 수 있음을 체감하였으며, 이를 통해 강력한 암호화 알고리즘(AES, RSA 등)과 충분한 키 길이의 중요성을 이해하게 됨.
