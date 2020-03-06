"""
Return a slice object
---------------------

Params:     start   (int)   [optional] which position to start slicing
                            default: 0
            end     (int)   [optional] which position to end slicing
            step    (int)   [optional] step of slicing
                            default: 1

Return:             (obj)   slice object
"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
slice_1 = slice(7)
print('Original letters: {}\nSlice: {}\n'.format(letters, letters[slice_1]))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
slice_2 = slice(1,7)
print('Original letters: {}\nSlice: {}\n'.format(letters, letters[slice_2]))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
slice_3 = slice(1,7,2)
print('Original letters: {}\nSlice: {}'.format(letters, letters[slice_3]))