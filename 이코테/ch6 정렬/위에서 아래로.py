N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
sorted(arr, reverse=True)

"""
sort vs sorted 
- GPT 답변
🔹 arr.sort(reverse=True)
제자리 정렬 (In-place sorting): 리스트를 직접 정렬하며, 반환값이 None이다.
추가 메모리 사용 없음: 기존 리스트를 변경하므로 새로운 리스트를 생성하지 않는다.
속도가 더 빠름: 불필요한 복사가 없고, 리스트 크기가 클수록 유리하다.
🔹 sorted(arr, reverse=True)
새로운 리스트 반환: 기존 리스트는 그대로 유지되며, 정렬된 새로운 리스트를 반환한다.
추가 메모리 사용: 새로운 리스트를 만들기 때문에 메모리 사용량이 증가한다.
조금 더 느림: 내부적으로 리스트를 복사한 후 정렬을 수행하므로 오버헤드가 있다.

- stack over flow
https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort
Q. 
list.sort() sorts the list and replaces the original list, whereas sorted(list) returns a sorted copy of the list, without changing the original list.

When is one preferred over the other?
Which is more efficient? By how much?
Can a list be reverted to the unsorted state after list.sort() has been performed?

A.
sorted() returns a new sorted list, leaving the original list unaffected. list.sort() sorts the list in-place, mutating the list indices, and returns None (like all in-place operations).
sorted() works on any iterable, not just lists. Strings, tuples, dictionaries (you'll get the keys), generators, etc., returning a list containing all elements, sorted.
Use list.sort() when you want to mutate the list, sorted() when you want a new sorted object back. Use sorted() when you want to sort something that is an iterable, not a list yet.
For lists, list.sort() is faster than sorted() because it doesn't have to create a copy. For any other iterable, you have no choice.
No, you cannot retrieve the original positions. Once you called list.sort() the original order is gone.
"""

for i in arr:
    print(i, end=' ')