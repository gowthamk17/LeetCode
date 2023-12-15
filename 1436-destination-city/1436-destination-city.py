class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        for p in paths:
            source.add(p[0])
        for p in paths:
            if p[1] not in source:
                return p[1]