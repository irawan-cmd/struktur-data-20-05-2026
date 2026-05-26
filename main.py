from typing import List, Optional
from collections import deque

# ================= LINKED LIST NODE =================
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# ================= ADVANCED SORTER =================
class AdvancedSorter:

    # ===== ARRAY MERGE SORT =====
    def sort_array(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        tmp = [0] * len(arr)
        self._merge_sort(arr, 0, len(arr) - 1, tmp)
        return arr

    def _merge_sort(self, arr, left, right, tmp):
        if left >= right:
            return
        mid = (left + right) // 2
        self._merge_sort(arr, left, mid, tmp)
        self._merge_sort(arr, mid + 1, right, tmp)
        self._merge(arr, left, mid, right, tmp)

    def _merge(self, arr, left, mid, right, tmp):
        i, j, k = left, mid + 1, left

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                tmp[k] = arr[i]
                i += 1
            else:
                tmp[k] = arr[j]
                j += 1
            k += 1

        while i <= mid:
            tmp[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            tmp[k] = arr[j]
            j += 1
            k += 1

        for x in range(left, right + 1):
            arr[x] = tmp[x]

    # ===== LINKED LIST MERGE SORT =====
    def sort_linked_list(self, head: Optional[ListNode]):
        if not head or not head.next:
            return head

        right = self._split(head)
        left_sorted = self.sort_linked_list(head)
        right_sorted = self.sort_linked_list(right)

        return self._merge_list(left_sorted, right_sorted)

    def _split(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        return right

    def _merge_list(self, a, b):
        dummy = ListNode(0)
        tail = dummy

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        return dummy.next

    # ===== QUICK SORT PARTITION =====
    def partition_quick(self, arr, first, last):
        mid = (first + last) // 2

        if arr[first] > arr[mid]:
            arr[first], arr[mid] = arr[mid], arr[first]
        if arr[first] > arr[last]:
            arr[first], arr[last] = arr[last], arr[first]
        if arr[mid] > arr[last]:
            arr[mid], arr[last] = arr[last], arr[mid]

        arr[first], arr[mid] = arr[mid], arr[first]
        pivot = arr[first]

        left = first + 1
        right = last

        while True:
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left > right:
                break
            arr[left], arr[right] = arr[right], arr[left]

        arr[first], arr[right] = arr[right], arr[first]
        return right


# ================= EXPR + HEAP =================
class ExprHeapSorter:

    def __init__(self, expr: str):
        self.expr = expr

    def parse_and_evaluate(self):
        tokens = deque(self.expr)
        root = self._build_tree(tokens)
        return self._eval(root)

    def _build_tree(self, tokens):
        ch = tokens.popleft()

        if ch == '(':
            left = self._build_tree(tokens)
            op = tokens.popleft()
            right = self._build_tree(tokens)
            tokens.popleft()
            return {'val': op, 'left': left, 'right': right}
        else:
            return {'val': int(ch), 'left': None, 'right': None}

    def _eval(self, node):
        if node['left'] is None:
            return node['val']

        a = self._eval(node['left'])
        b = self._eval(node['right'])

        if node['val'] == '+':
            return a + b
        elif node['val'] == '-':
            return a - b
        elif node['val'] == '*':
            return a * b
        elif node['val'] == '/':
            if b == 0:
                raise ValueError("Division by zero")
            return a // b

    def heapsort_inplace(self, arr: List[int]):
        n = len(arr)

        for i in range(n//2 - 1, -1, -1):
            self._sift_down(arr, n, i)

        for end in range(n-1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            self._sift_down(arr, end, 0)

        return arr

    def _sift_down(self, arr, size, i):
        while True:
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < size and arr[left] > arr[largest]:
                largest = left
            if right < size and arr[right] > arr[largest]:
                largest = right

            if largest == i:
                break

            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest


# ================= TEST =================
if __name__ == "__main__":
    sorter = AdvancedSorter()

    # Array
    arr = [5, 2, 9, 1, 3]
    print("Sorted Array:", sorter.sort_array(arr))

    # Linked List
    head = ListNode(3, ListNode(1, ListNode(2)))
    sorted_head = sorter.sort_linked_list(head)

    print("Sorted Linked List:", end=" ")
    cur = sorted_head
    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next

    # Heap + Expression
    heap = ExprHeapSorter("((8*5)+(9/(7-4)))")

    arr2 = [4, 7, 1, 9, 2]
    print("\nHeapsort:", heap.heapsort_inplace(arr2))

    print("Expression Result:", heap.parse_and_evaluate())
