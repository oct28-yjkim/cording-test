# 12주 코딩 테스트 커리큘럼

각 주차는 `개념 학습 → 기본 문제 → 응용 문제 → 오답 재풀이` 순서로 진행합니다. 필수 문제는 주당 5개이며, 시간이 남으면 선택 문제를 추가합니다.

## 난도와 시간 규칙

- 기본 문제: 20–30분 안에 풀이 방향을 찾습니다.
- 응용 문제: 40분까지 스스로 시도합니다.
- 제한 시간이 지나면 정답 전체보다 힌트를 먼저 확인합니다.
- 해설을 본 문제는 최소 하루 뒤 빈 파일에서 다시 풉니다.
- 모든 풀이에 시간 복잡도와 공간 복잡도를 적습니다.

## 1주차 — 복잡도, 배열, 문자열

**학습 목표**

- `O(1)`, `O(log N)`, `O(N)`, `O(N log N)`, `O(N²)`을 입력 크기와 연결한다.
- 배열 순회, 인덱스, 문자열 처리에 익숙해진다.
- Python 입력 처리와 기본 내장 함수를 정확히 사용한다.

**필수 문제**

1. [BOJ 10818 최소, 최대](https://www.acmicpc.net/problem/10818)
2. [BOJ 2562 최댓값](https://www.acmicpc.net/problem/2562)
3. [BOJ 2577 숫자의 개수](https://www.acmicpc.net/problem/2577)
4. [BOJ 1152 단어의 개수](https://www.acmicpc.net/problem/1152)
5. [LeetCode 217 Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

**완료 기준**: 각 풀이의 반복 횟수를 근거로 시간 복잡도를 한 문장으로 설명한다.

## 2주차 — 해시와 집합

**학습 목표**

- `dict`, `set`, `Counter`, `defaultdict`의 용도를 구분한다.
- 이중 반복문을 해시 조회로 줄이는 패턴을 익힌다.

**필수 문제**

1. [BOJ 10816 숫자 카드 2](https://www.acmicpc.net/problem/10816)
2. [BOJ 1764 듣보잡](https://www.acmicpc.net/problem/1764)
3. [BOJ 7785 회사에 있는 사람](https://www.acmicpc.net/problem/7785)
4. [LeetCode 1 Two Sum](https://leetcode.com/problems/two-sum/)
5. [LeetCode 49 Group Anagrams](https://leetcode.com/problems/group-anagrams/)

**완료 기준**: 해시를 사용하지 않은 풀이와 사용한 풀이의 복잡도 차이를 비교한다.

## 3주차 — 스택, 큐, 덱

**학습 목표**

- LIFO와 FIFO가 필요한 상황을 구분한다.
- Python의 `list`와 `collections.deque`를 올바르게 선택한다.

**필수 문제**

1. [BOJ 9012 괄호](https://www.acmicpc.net/problem/9012)
2. [BOJ 10773 제로](https://www.acmicpc.net/problem/10773)
3. [BOJ 2164 카드2](https://www.acmicpc.net/problem/2164)
4. [BOJ 18258 큐 2](https://www.acmicpc.net/problem/18258)
5. [LeetCode 20 Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

**완료 기준**: `list.pop(0)`을 피해야 하는 이유와 `deque.popleft()`의 복잡도를 설명한다.

## 4주차 — 정렬과 이분 탐색

**학습 목표**

- 정렬 기준을 `key` 함수로 표현한다.
- 탐색 범위와 불변식을 정의해 이분 탐색을 구현한다.
- 값 탐색과 정답 탐색(parametric search)을 구분한다.

**필수 문제**

1. [BOJ 2751 수 정렬하기 2](https://www.acmicpc.net/problem/2751)
2. [BOJ 1181 단어 정렬](https://www.acmicpc.net/problem/1181)
3. [BOJ 1920 수 찾기](https://www.acmicpc.net/problem/1920)
4. [BOJ 2805 나무 자르기](https://www.acmicpc.net/problem/2805)
5. [LeetCode 704 Binary Search](https://leetcode.com/problems/binary-search/)

**완료 기준**: 직접 작성한 이분 탐색에서 `left`, `right`, `mid`의 의미를 설명한다.

## 5주차 — 투 포인터와 슬라이딩 윈도우

**학습 목표**

- 완전 탐색의 중복 계산을 제거한다.
- 고정 길이와 가변 길이 윈도우를 구분한다.

**필수 문제**

1. [BOJ 2003 수들의 합 2](https://www.acmicpc.net/problem/2003)
2. [BOJ 1806 부분합](https://www.acmicpc.net/problem/1806)
3. [BOJ 2559 수열](https://www.acmicpc.net/problem/2559)
4. [BOJ 2470 두 용액](https://www.acmicpc.net/problem/2470)
5. [LeetCode 3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**완료 기준**: 포인터가 전체 실행 동안 각각 최대 몇 번 이동하는지 설명한다.

## 6주차 — 재귀와 백트래킹

**학습 목표**

- 종료 조건, 선택, 재귀 호출, 선택 취소의 구조를 익힌다.
- 유망하지 않은 상태를 조기에 제거한다.

**필수 문제**

1. [BOJ 15649 N과 M (1)](https://www.acmicpc.net/problem/15649)
2. [BOJ 15650 N과 M (2)](https://www.acmicpc.net/problem/15650)
3. [BOJ 1182 부분수열의 합](https://www.acmicpc.net/problem/1182)
4. [BOJ 9663 N-Queen](https://www.acmicpc.net/problem/9663)
5. [LeetCode 46 Permutations](https://leetcode.com/problems/permutations/)

**완료 기준**: 탐색 트리를 손으로 그리고 가지치기 지점을 표시한다.

## 7주차 — 연결 리스트와 힙

**학습 목표**

- 연결 리스트의 노드 변경 순서를 안전하게 다룬다.
- 최솟값/최댓값을 반복해서 꺼낼 때 힙을 선택한다.

**필수 문제**

1. [BOJ 1927 최소 힙](https://www.acmicpc.net/problem/1927)
2. [BOJ 11279 최대 힙](https://www.acmicpc.net/problem/11279)
3. [BOJ 1655 가운데를 말해요](https://www.acmicpc.net/problem/1655)
4. [LeetCode 206 Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
5. [LeetCode 21 Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

**완료 기준**: 힙 삽입/삭제 복잡도와 연결 리스트 역순 처리의 포인터 변화를 설명한다.

## 8주차 — 트리와 이진 탐색 트리

**학습 목표**

- 전위, 중위, 후위, 레벨 순회를 구현한다.
- 트리의 부분 문제를 재귀적으로 정의한다.

**필수 문제**

1. [BOJ 11725 트리의 부모 찾기](https://www.acmicpc.net/problem/11725)
2. [BOJ 1991 트리 순회](https://www.acmicpc.net/problem/1991)
3. [BOJ 5639 이진 검색 트리](https://www.acmicpc.net/problem/5639)
4. [BOJ 9934 완전 이진 트리](https://www.acmicpc.net/problem/9934)
5. [LeetCode 104 Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**완료 기준**: 같은 트리를 네 가지 순회 방식으로 방문한 결과를 직접 작성한다.

## 9주차 — 그래프와 BFS/DFS

**학습 목표**

- 인접 행렬과 인접 리스트를 선택한다.
- 방문 배열의 갱신 시점을 정확히 정한다.
- 최단 이동 횟수에는 BFS를 적용한다.

**필수 문제**

1. [BOJ 1260 DFS와 BFS](https://www.acmicpc.net/problem/1260)
2. [BOJ 2178 미로 탐색](https://www.acmicpc.net/problem/2178)
3. [BOJ 2667 단지번호붙이기](https://www.acmicpc.net/problem/2667)
4. [BOJ 1012 유기농 배추](https://www.acmicpc.net/problem/1012)
5. [LeetCode 200 Number of Islands](https://leetcode.com/problems/number-of-islands/)

**완료 기준**: 같은 그래프를 BFS와 DFS로 탐색하고 결과와 메모리 사용을 비교한다.

## 10주차 — 그래프 응용

**학습 목표**

- 가중치가 음수가 없는 그래프에 다익스트라를 적용한다.
- 유니온 파인드로 집합의 연결 여부를 관리한다.
- 선행 관계가 있는 작업을 위상 정렬한다.

**필수 문제**

1. [BOJ 1753 최단경로](https://www.acmicpc.net/problem/1753)
2. [BOJ 1916 최소비용 구하기](https://www.acmicpc.net/problem/1916)
3. [BOJ 1717 집합의 표현](https://www.acmicpc.net/problem/1717)
4. [BOJ 2252 줄 세우기](https://www.acmicpc.net/problem/2252)
5. [BOJ 11779 최소비용 구하기 2](https://www.acmicpc.net/problem/11779)

**완료 기준**: 각 문제의 그래프 유형, 핵심 자료구조, 전체 복잡도를 표로 정리한다.

## 11주차 — 그리디와 동적 계획법

**학습 목표**

- 그리디 선택이 이후 선택을 막지 않는 이유를 설명한다.
- DP의 상태, 점화식, 초기값, 계산 순서를 정의한다.

**필수 문제**

1. [BOJ 11399 ATM](https://www.acmicpc.net/problem/11399)
2. [BOJ 1931 회의실 배정](https://www.acmicpc.net/problem/1931)
3. [BOJ 9095 1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)
4. [BOJ 1463 1로 만들기](https://www.acmicpc.net/problem/1463)
5. [BOJ 2579 계단 오르기](https://www.acmicpc.net/problem/2579)

**완료 기준**: 그리디 문제는 선택의 근거를, DP 문제는 점화식을 코드보다 먼저 적는다.

## 12주차 — 종합 복습과 모의 테스트

**학습 목표**

- 문제 유형을 빠르게 분류하되 섣불리 한 알고리즘에 고정하지 않는다.
- 제한 시간 안에서 읽기, 구현, 검증 시간을 배분한다.

**진행 방법**

1. 취약 주제 두 개를 골라 오답 5개를 다시 푼다.
2. 서로 다른 날에 120분 모의 테스트를 3회 진행한다.
3. 매 회차 쉬운 문제부터 읽고 `40분 이상 진전 없음` 규칙으로 전환한다.
4. 종료 후 정답 여부와 무관하게 접근, 실수, 시간 사용을 기록한다.

**모의 테스트 구성**

- 1번: 구현 또는 자료구조, 목표 30분
- 2번: 탐색 또는 정렬 응용, 목표 40분
- 3번: 그래프 또는 DP, 목표 50분

**완료 기준**: 마지막 두 회차에서 각각 2문제 이상 해결하고, 실패 원인을 알고리즘·구현·시간 관리 중 하나로 분류한다.

## 수료 후 다음 단계

- 지원 회사의 기출 유형을 분석해 4주 심화 계획을 만든다.
- 취약 유형 문제를 난도 순으로 10개씩 추가한다.
- 주 1회 모의 테스트와 주 1회 오답 재풀이를 유지한다.
- 풀이를 말로 설명하거나 코드 리뷰를 받아 가독성과 검증 능력을 높인다.
