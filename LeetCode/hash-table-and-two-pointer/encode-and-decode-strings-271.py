''' premium problem
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]

'''
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        start_index = 0
        while start_index < len(s):
            start_index_value = start_index
            word_len_str = ""
            count_digit = 0
            while s[start_index_value] != "#":
                word_len_str += s[start_index_value]
                start_index_value += 1
                count_digit += 1
            word_len = int(word_len_str)
            result.append(s[start_index + count_digit +
                          1: start_index + count_digit+1 + word_len])
            start_index = start_index + count_digit+1 + word_len

        return result

# 5#63/Rc 1#h 13#BmI3FS~J9#vmk 8#7uBZ?7*/ 5#24h+X 2#O


# Your Codec object will be instantiated and called as such:
strs = ["BmI3FS~J9#vmk", "63/Rc", "h",
        "BmI3FS~J9#vmk", "7uBZ?7*/", "24h+X", "O "]
codec = Codec()
print(codec.decode(codec.encode(strs))
      )
