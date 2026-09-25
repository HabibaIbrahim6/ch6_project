class MergeSort:
    # Because Merge Sort is Private Function to access  this function
    def sort(self, events_list, key_type, reverse=False):
        return self._merge_sort(events_list, key_type, reverse)

    def _merge_sort(self, events_list, key_type, reverse):
        if len(events_list) <= 1:
            return events_list

        mid = len(events_list) // 2
        left_half = self._merge_sort(events_list[:mid], key_type, reverse)
        right_half = self._merge_sort(events_list[mid:], key_type, reverse)

        return self._merge(left_half, right_half, key_type, reverse)

    def _merge(self, left, right, key_type, reverse):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if key_type == "price":
                val1 = left[i].price
                val2 = right[j].price
            else:
                val1 = left[i].rating
                val2 = right[j].rating

            if not reverse:
                condition = val1 <= val2
            else:
                condition = val1 >= val2

            if condition:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list