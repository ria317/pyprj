# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#### 역량인증 study Day _1 #######


# time complexity 시간복잡도

#Big-O 표기법
# 항상 worst case를 기준으로 time 산정

#O(logN)
# EX binary search / quick sort / upper bound / low bound?

#O(N^2)
# Quick sort ( ) 에서는 pivot 을 잡는 기준에 따라 time이 달라지는데,
# 보통의 STL 에서는 PIVOT 을 합리적으로 잡기 때문에,, 본질적으로는 N^2 이지만 일반적으로는 NlogN 으로 간다.

## 보통 nlogn, n


def dfs(x, y, visit, a, b ):

    # 범위 벗어나면 false
    if x>= a or y >= b :
        return False

    #종료지점까지 왔을 때
    if x == a-1 and y == b-1 :
        visit.append([x,y])
        #tot_list.append(visit)
        print(visit)
        return True

    while 1:
        if len(visit) == 0 :
            visit.append([x,y])
            break
        cmp = visit.pop()
        c_x = cmp[0]
        c_y = cmp[1]

        if x+y == c_x + c_y +1 :
            visit.append([c_x, c_y])
            visit.append([x,y])
            break



    dfs(x+1, y, visit, a, b)
    dfs(x, y+1, visit, a, b)

def solve(a, b):

    visit = []
    #footprint = [[False]*b]*a
    dfs( 0, 0, visit, a , b)

solve(3,4)
