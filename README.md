# amogus-sort

The Amogus Sort is a sorting algorithm inspired on the popular game amongus us. The algorithm works as follows:

```
procedure amogus_sort(arr):
  array_copy <- array

  check if the sorting is feasible for the given criteria
  if not, invert the criteria

  while array is not sorted:
    for each element in array:
      counter <- number of elements that break the sorting criteria
      if counter >= |array| / 2 or array is sorted:
        exit for
      end if

      votes <- x | 0 <= x <= |array|
      if votes >= |array| / 2:
        (optional) print "element ejected: {element}; votes: {votes}/{arr_size}"
        array <- array - { element }
      end if
    end for
    if arr is not sorted:
      counter <- number of elements that break the sorting criteria
      if counter >= |array| / 2:
        (optional) print "the imposters have won! restarting the sorting procedure..."
        array <- array_copy
      end if
    end if
  end while
  (optional) print "the crewmates have won! the array is sorted!"
  return array
end procedure
```

## Proof of correctness

The algorithm's stopping criteria guarantees that the sorting process must continue until one of the following conditions are met:

a) The array is sorted

b) The array contains a larger number of elements that break the sorting criteria, in which case the Among Us sort is invoked again with the original array to be sorted. Thus, the algorithm must eventually hit (a) or (b) again.

Let us assume that the algorithm terminates with an unsorted array and doesn't invoke Among Us sort again. This scenario implies that either the implementation is sus or the author of the code is a sussy baka trying to sabotage the proof of correctness. Therefore, the algorithm should terminate correctly if the author of the code is not an imposter.

## Time complexity

- Best case scenario: all of the elements are ordered, meaning that the array is not sus. $O(n)$
- Worst case scenario: this case is trivial and is left as an exercise for the reader
