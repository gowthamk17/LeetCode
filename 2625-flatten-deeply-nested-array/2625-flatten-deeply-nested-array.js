/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n < 1) 
        return arr;
    const flatArr = [];
    for (let i = 0; i < arr.length; i++) {
        const val = arr[i];
        if (Array.isArray(val)) {
            flatArr.push(...flat(val, n-1));
        } else {
            flatArr.push(val);
        }
    }
    return flatArr;
};