class Sortable:
    def __init__(self, array: list[int]) -> None:
        self.array = array

    def partitioning(self, left_pointer: int, right_pointer: int) -> int:
        pivot_pointer = right_pointer
        right_pointer -= 1

        # Keep the loop running:
        while True:

            # Move the left pointer to the right, and stop
            # as soon the value the left pointer is pointing at
            # is equal or greater than the pivot value.
            while not self.array[left_pointer] >= self.array[pivot_pointer]:
                left_pointer += 1

            # Move the right pointer to the left, and stop
            # as soon the value the right pointer is pointing at
            # is equal or smaller than the pivot value.
            while not self.array[right_pointer] <= self.array[pivot_pointer]:
                right_pointer -= 1

            # Once we reach this line, we can decide how to
            # further process this sorting roun, because the
            # right pointer has stopped moving.

            if left_pointer >= right_pointer:
                break

            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                left_pointer += 1

        self.array[left_pointer], self.array[pivot_pointer] = self.array[pivot_pointer], self.array[left_pointer]
        # Once we reach this point, the value
        # that the left pointer was pointing at,
        # will be placed at the correct slot within
        # the array.

        return left_pointer

    def quicksort(self, left_pointer, right_pointer):
        if right_pointer - left_pointer <= 0:
            return

        pivot_pointer = self.partitioning(left_pointer, right_pointer)
        self.quicksort(left_pointer, pivot_pointer - 1)
        self.quicksort(pivot_pointer + 1, right_pointer)


array = [0, 5, 2, 1, 6, 3]
sort_me = Sortable(array)
sort_me.quicksort(0, len(array) - 1)
print(sort_me.array)
