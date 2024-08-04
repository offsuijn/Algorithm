# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import Counter, defaultdict

def solution(genres, plays):
    
    gdict = defaultdict(int) # 장르 정렬을 위한 dict
    pdict = defaultdict(dict) # 곡 정렬을 위한 dict
    answer = []
    

    for i, (g, p) in enumerate(zip(genres, plays)):
        # 장르 정렬 전처리
        gdict[g] += p
        
        # 곡 정렬 전처리
        pdict[g][i] = p
    
    # 장르 정렬
    gorder = [x for x, y in Counter(gdict).most_common()]
    
    # 장르마다 곡 정렬
    for g in gorder:
        answer.extend([x for x, y in Counter(pdict[g]).most_common(2)])
        
    return answer


    '''
    <주의 사항>
    장르에 속한 곡이 하나라면, 하나의 곡만 선택한다.
    재생 횟수가 같다면 고유 번호가 낮은 노래를 먼저 수록한다. -> Counter 고유 기능
    
    <필요한 값>
    - 장르마다 총합 -> 정렬
        dict->Counter로 총합 구하기 -> 장르 순서 list에 저장
    - 장르 내 정렬 후 2곡 선정
        dict 내 dict: 장르마다 dict 만들어서 (고유 번호:재생횟수) 집어넣기
        Counter로 재생횟수 기준으로 정렬하고 2곡 자르기
    '''
