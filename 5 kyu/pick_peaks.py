def pick_peaks(arr):
    sol = {"pos": [], "peaks": []}
    peak_start, peak_val = None, None
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            peak_start = i
            peak_val = arr[i]
        elif arr[i] < arr[i-1]:
            if peak_start:
                sol["pos"].append(peak_start)
                sol["peaks"].append(peak_val)
                peak_start, peak_val = None, None
    return sol


print(pick_peaks([1,2,3,6,4,1,2,3,2,1]))

