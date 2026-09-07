class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            local, domain = e.split("@")
            local = e.split("+")[0]
            bruv = "".join(local.split("."))
            result = bruv + "@" + domain
            unique.add(result)

        return len(unique)