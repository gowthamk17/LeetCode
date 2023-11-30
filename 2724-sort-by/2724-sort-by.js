/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    function compare(a,b) {
        if (fn(a) > fn(b)) 
            return 1;
        else if (fn(a) < fn(b))
            return -1;
        else
            return 0;
    }
    return arr.sort(compare);
};