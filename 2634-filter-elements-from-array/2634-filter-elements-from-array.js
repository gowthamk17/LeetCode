/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArr = []
    for(let i = 0; i < arr.length; i++) {
        if(fn(arr[i], i, arr)) {
            newArr.push(arr[i]);
        }
    }
    return newArr
};