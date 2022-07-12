# 937. Reorder Data in Log Files

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        풀이
        1. 로그를 숫자, 문자 리스트로 구분한다.
        2. 사전순으로 정렬하고, 동일한 경우에는 id로 정렬한다.
        3. 문자와 숫자 리스트를 합친다.
        """
        digit, letter = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
                
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letter + digit
