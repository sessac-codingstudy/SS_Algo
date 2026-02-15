'''
문제 설명
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
'''
str = input()
# result = ""
# for ch in str:
#     if ch.isupper():
#         result += ch.lower()
#     else:
#         result += ch.upper()
print(str.swapcase())


# 대소문자 바꾸는 메서드 ====> swapcae()