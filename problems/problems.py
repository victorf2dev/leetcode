

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        1 Two Sum
        
        Exemplo 1
        >>> nums = [2,7,11,15], target = 9
        >>> [0,1]

        Exemplo 2
        >>> nums = [3,2,4], target = 6
        >>> [1,2]

        Exemplo 3
        >>> nums = [3,3], target = 6
        >>> [0,1]
        """
        for i, x in enumerate(nums):
            for ii, y in enumerate(nums):
                if ii > i:
                    if x + y == target:
                        return [i, ii]


    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        """
        3000 Maximum Area of Longest Diagonal Rectangle

        Exemplo 1
        >>> dimensions = [[9,3],[8,6]]
        >>> 48

        Exemplo 2
        >>> dimensions = [[3,4],[4,3]]
        >>> 12
        """
        areas: list = []
        hipotenusas: list = []

        for index, _ in enumerate(dimensions):
            catetoI, catetoII, *_ = dimensions[index]

            area: int = catetoI * catetoII
            hipotenusa: float = (catetoI**2 + catetoII**2)**0.5 

            areas.append(area)
            hipotenusas.append(hipotenusa)

        maior_hipotenusa = max(hipotenusas)
        contador_maior_hipotenusa = hipotenusas.count(maior_hipotenusa)

        if contador_maior_hipotenusa > 1:
            areas_filtradas: list = [areas[i] for i, d in enumerate(hipotenusas) if d == maior_hipotenusa]
            return max(areas_filtradas)            
        else:
            return areas[hipotenusas.index(maior_hipotenusa)]