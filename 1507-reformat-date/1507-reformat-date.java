class Solution {
    public String reformatDate(String date) {
        StringBuilder sb = new StringBuilder();
        sb.append(date.substring(date.length()-4)).append("-");
        String m = date.length()==13 ? date.substring(5,8) : date.substring(4,7);
        switch(m){
             case "Jan": sb.append("01-"); break;
             case "Feb": sb.append("02-"); break;
             case "Mar": sb.append("03-"); break;
             case "Apr": sb.append("04-"); break;
             case "May": sb.append("05-"); break;
             case "Jun": sb.append("06-"); break;
             case "Jul": sb.append("07-"); break;
             case "Aug": sb.append("08-"); break;
             case "Sep": sb.append("09-"); break;
             case "Oct": sb.append("10-"); break;
             case "Nov": sb.append("11-"); break;
             case "Dec": sb.append("12-"); break;
         }
        String day = date.length()==13 ? date.substring(0,2) : "0"+date.substring(0,1);
        sb.append(day);
        return sb.toString();
    }
}