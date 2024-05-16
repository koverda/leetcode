from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankNames = []

        # build original order lookup and ranks tab
        for i in range(len(score)):
            if i == 0:
                rankNames.append("Gold Medal")
            elif i == 1:
                rankNames.append("Silver Medal")
            elif i == 2:
                rankNames.append("Bronze Medal")
            else:
                rankNames.append(str(i + 1))
            i += 1

        # get ranks for elements
        sortedScores = list(reversed(sorted(score)))
        rankLookup = {}

        for i in range(len(sortedScores)):
            rankLookup[sortedScores[i]] = rankNames[i]
            i += 1

        res = []
        for el in score:
            res.append(rankLookup[el])
        return res


sln = Solution()
res = sln.findRelativeRanks([10, 3, 8, 9, 4])
print(res)
