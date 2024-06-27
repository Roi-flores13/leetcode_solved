def merge(nums1, m, nums2, n):
    for i,v in enumerate(sorted(nums1[:m] + nums2[:n])):
        if i < len(nums1):
            nums1[i] = v
        else:
            nums1.append(v)
    return nums1