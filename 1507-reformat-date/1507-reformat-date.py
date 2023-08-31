class Solution:
    def reformatDate(self, date: str) -> str:
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
        new_date = date[-4:] + "-"
        new_date += monthDict[date[5:8] if len(date)==13 else date[4:7]] + "-"
        new_date += date[0:2] if len(date)==13 else "0"+date[0]
        return new_date
        