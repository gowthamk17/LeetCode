/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if (arr.length == 0) return arr
    const chunked = []
    for (let i = 0; i < arr.length; i = i + size) {
        chunked.push(arr.slice(i, i+size))
    }
    return chunked
};
