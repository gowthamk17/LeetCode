class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int std_count = 0;
        for(int i = 0; i < startTime.length; i++) {
            if(queryTime >= startTime[i] && queryTime <= endTime[i]) {
                std_count++;
            }
        }
        return std_count;
    }
}