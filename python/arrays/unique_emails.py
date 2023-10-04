"""
Every valid email consists of a local name and a domain name, separated by the '@' sign.
Besides lowercase letters, the email may contain one or more '.' or '+'.
For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

If you add periods '.' between some characters in the local name part of an email address,
mail sent there will be forwarded to the same address without dots in the local name.
Note that this rule does not apply to domain names.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
This allows certain emails to be filtered. Note that this rule does not apply to domain names.
For example, "m.y+name@email.com" will be forwarded to "my@email.com".

It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i],
return the number of different addresses that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
"""

import re


class Solution:
    def __init__(self) -> None:
        pass

    def numUniqueEmails(self, emails: list[str]) -> int:
        addy_dict = {}
        loc_pat = re.compile(r"(?=^)\b[a-zA-Z0-9.+]{1,}\b")
        domain_pat = re.compile(r"(?<=.)@[a-zA-Z0-9.+]{1,}\.com$")
        rm_after = re.compile(r"\+.*")  # Anything after '+' can go

        for i, address in enumerate(emails):
            loc_match = re.search(loc_pat, address).group()
            domain_match = re.search(domain_pat, address).group()
            addy_dict[i] = re.sub(rm_after, "", loc_match).replace(".", "") + domain_match

        return len(set(addy_dict.values()))


x = Solution()
print(
    x.numUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
    )
)
print(x.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
print(
    x.numUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
            "b@leetcode.com",
            "c@leetcode.com",
        ]
    )
)
