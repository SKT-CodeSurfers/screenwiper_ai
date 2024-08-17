from hanspell import spell_checker
result = spell_checker.check(u'분석 결과를 받아업니다.')
result.as_dict()  # dic
print(result)