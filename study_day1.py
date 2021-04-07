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


def dfs(x, y, visited, a, b ):
    # 범위 벗어나면 false
    print("idx:", x,",", y)
    if( x>= a or y >= b ):
        return False

    # 이미 방문한 경로 fail
    if visited[x][y] == True:
        return False

    visited[x][y] = True
    print(x,",", y)

    dfs(x+1, y, visited, a, b)
    dfs(x, y+1, visited, a, b)
    return True
 

def solve(a, b):

    visited = [[False]*b]*a
    graph = []

    print(visited)
    dfs( 0, 0, visited, a , b)

solve(3,4)

