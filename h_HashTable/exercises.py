from collections import defaultdict
from typing import List, Dict, Union

from b_LinkedList.single_linked_list import LinkedList


class HashingExercises:
    def __init__(self):
        ...

    @staticmethod
    def is_subset(list1: List[int], list2: List[int]):
        """
        takes two lists as input and checks whether one list is the subset of the other
        :param list1: The input lists do not contain duplicate values.
        :param list2: The input lists do not contain duplicate values.
        :return:
        >>> HashingExercises.is_subset([1, 2, 3, 4, 5, 6], [1, 2, 3])
        >>> True
        """
        s = set(list1)
        for elem in list2:
            if elem not in s:
                return False
        return True

    @staticmethod
    def is_disjoint(list1: List[int], list2: List[int]) -> bool:
        """
        Checks whether two given lists are disjoint or not.
        Two lists are disjoint if there are no common elements between them.
        The assumption is that there are no duplicate elements in each list.
        :param list1:
        :param list2:
        :return:
        >>> HashingExercises.is_disjoint([9,4,3,1,-2,6,5], [7,10,8])
        >>> True

        >>> HashingExercises.is_disjoint([9,4,3,1,-2,6,5], [1, 12])
        >>> True
        """
        set1 = set(list1)
        set2 = set(list2)
        intersection = set1 & set2

        return True if not intersection else False

    @staticmethod
    def find_symmetric(my_list: List[List[int]]):
        """
        By definition, (a, b) and (c, d) are symmetric pairs iff, a = d and b = c.
        >>> HashingExercises.find_symmetric([[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]])
        >>> [[3, 4], [4, 3], [5, 9], [9, 5]]
        :param my_list:
        :return:

        """
        checked = set()
        result = []
        for pair in my_list:
            tuple_pair = tuple(pair)
            pair.reverse()
            reversed_pair = tuple(pair)

            if reversed_pair in checked:
                result.append(list(tuple_pair))
                result.append(list(reversed_pair))
            else:
                checked.add(tuple_pair)

        return result

    @staticmethod
    def trace_path(my_dict: Dict[str, str]) -> List[List[str, str]]:
        """
        take in a list of source-destination pairs and return the correct sequence of the whole journey
        from the first city to the last.
        :param my_dict:
        :return:
        >>> dict_ = {"NewYork": "Chicago","Boston": "Texas","Missouri": "NewYork","Texas": "Missouri"}
        >>> HashingExercises.trace_path(dict_)
        >>> [["Boston", "Texas"] , ["Texas", "Missouri"] , ["Missouri", "NewYork"] , ["NewYork", "Chicago"]]
        """
        result = []
        reversed_dict = {value: key for key, value in my_dict.items()}
        from_loc = None
        for key in my_dict:
            if key not in reversed_dict:
                from_loc = key
                break

        to = my_dict.get(from_loc)
        while to is not None:
            result.append([from_loc, to])
            from_loc, to = to, my_dict.get(to)

        return result

    @staticmethod
    def find_pair(my_list: List[int]) -> List[List[int, int]]:
        """
        find two pairs, [a, b] and [c, d], in a list such that:
        a + b = c + d
        :param my_list:
        :return:
        >>> HashingExercises.find_pair([3, 4, 7, 1, 12, 9])
        >>> [[4,12],[7,9]]
        """
        result = []
        checked = {}  # key: added sum, value: a pair of two digits

        for i in range(len(my_list)):
            for j in range(i + 1, len(my_list)):
                added = my_list[i] + my_list[j]
                if checked.get(added) is None:
                    checked[added] = [my_list[i], my_list[j]]
                else:
                    first_pair = checked[added]
                    second_pair = [my_list[i], my_list[j]]
                    result.append(first_pair)
                    result.append(second_pair)
                    return result

        return result

    @staticmethod
    def find_sum(lst: List[int], k: int) -> Union[List[int, int], bool]:
        """
        k as input and return two numbers that add up to k.
        :param lst:
        :param k:
        :return:
        >>> HashingExercises.find_sum([1,21,3,14,5,60,7,6], 81)
        >>> [21, 60]
        """
        seen = set()
        for ele in lst:
            if k - ele in seen:
                return [k - ele, ele]
            seen.add(ele)
        return False

    @staticmethod
    def find_first_unique(lst: List[int]) -> Union[int, None]:
        """
        returns the first unique integer in the list.
        Unique means the number does not repeat and appears only once in the whole list.
        :param lst:
        :return:
        >>> HashingExercises.find_first_unique([9,2,3,2,6,6])
        >>> 9
        """
        checked = defaultdict(int)
        for l in lst:
            checked[l] += 1

        for ele in lst:
            if checked[ele] == 1:
                return ele

    @staticmethod
    def detect_loop(lst: LinkedList) -> bool:
        """
        take a linked list as input and deduce whether a loop is present.
        :param lst:
        :return:
        LinkedList = 7->14->21->7
        return True
        """
        checked = {}
        root = lst.get_head()

        while root is not None:
            print(checked)
            if checked.get(root.data):
                return True
            else:
                checked[root.data] = root

            root = root.next_element

        return False

    @staticmethod
    def remove_duplicate(lst: LinkedList) -> LinkedList:
        """
        When a linked list is passed to this function,
        it removes any node which is a duplicate of another existing node.
        :param lst:
        :return:
        """
        seen = set()
        prev = None
        current = lst.get_head()

        while current:
            if current.data not in seen:
                seen.add(current.data)
                prev = current
                current = current.next_element
            else:
                while current.data in seen:
                    current = current.next_element
                    if current is None:
                        break
                prev.next_element = current

        return lst.get_head()

    @staticmethod
    def union_linked_list(list1: LinkedList, list2: LinkedList) -> LinkedList:
        if list1.is_empty():
            return list2
        elif list2.is_empty():
            return list1

        unique_values = set()
        result = LinkedList()

        h1 = list1.get_head()

        while h1:
            unique_values.add(h1.data)
            h1 = h1.next_element

        h2 = list2.get_head()

        while h2:
            unique_values.add(h2.data)
            h2 = h2.next_element

        for x in unique_values:
            result.insert_at_head(x)
        return result

    @staticmethod
    def intersection_linked_list(list1: LinkedList, list2: LinkedList) -> LinkedList:
        result = LinkedList()
        visited_nodes = set()
        current_node = list1.get_head()

        while current_node is not None:
            value = current_node.data
            if value not in visited_nodes:
                visited_nodes.add(value)
            current_node = current_node.next_element

        start = list2.get_head()
        while start is not None:
            value = start.data
            if value in visited_nodes:
                result.insert_at_head(start.data)
            start = start.next_element
        result.remove_duplicates()

        return result