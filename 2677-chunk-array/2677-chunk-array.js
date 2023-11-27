/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if (arr.length == 0) return arr
    const chunked = []
    let temp = []
    for (let i = 0; i < arr.length; i++) {
        if (i % size == 0 && i != 0) {
            chunked.push(temp)
            temp = []
            temp.push(arr[i])
        } else {
            temp.push(arr[i])
        }
    }
    chunked.push(temp)
    return chunked
};
