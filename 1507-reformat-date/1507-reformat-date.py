class Solution:
    def reformatDate(self, date: str) -> str:
        dates = date.split(' ')
        dates[0] = dates[0].replace("st","").replace("rd","").replace("th","").replace("nd", "")
        if len(dates[0]) == 1:
            dates[0] = "0"+dates[0]
        monthDict = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        dates[1] = monthDict[dates[1]]
        return "-".join(dates[::-1])
        