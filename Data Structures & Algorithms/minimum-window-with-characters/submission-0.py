from collections import Counter  # Import Counter to count characters easily

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""  # Edge case: if either string is empty, return empty

        count_t = Counter(t)  # Count frequency of each character in t
        window = {}  # Dictionary to count characters in the current window
        have, need = 0, len(count_t)  # 'have' = how many required characters matched, 'need' = total unique characters in t
        res, res_len = [-1, -1], float("inf")  # To store the best window (start, end) and its length
        l = 0  # Left pointer of the window

        # Move right pointer through the string
        for r in range(len(s)):
            c = s[r]  # Current character
            window[c] = window.get(c, 0) + 1  # Add it to the window count

            # If character is in t and we have required amount in window, increment 'have'
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # Try to shrink the window from the left if all required characters are matched
            while have == need:
                # Update result if this window is smaller than previous best
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Remove the leftmost character from the window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1  # A required character is now missing
                l += 1  # Move left pointer forward

        l, r = res
        # Return the substring if found, else return empty
        return s[l:r+1] if res_len != float("inf") else ""
