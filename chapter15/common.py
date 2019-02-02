import re

# 이메일 주소 정합성 체크를 위한 함수
def email_validation_check(email):
    # 이메일 정합성 검증 정규 표현식
    regex = r'[\w.-]+@[\w.-]+.\w+'

    # 이메일 주소 정합성 유무 확인
    find_result = re.findall(regex, email)

    # 에러 메시지 조건 및 출력
    #$ if len(find_result) != 1:
    if find_result[0] != email :
        print(email, '은 이메일 주소 형식에 맞지 않습니다.')
        return False

    # 성공 메시지 출력
    print(email, '은 이메일 주소로 적당합니다.')
    return True