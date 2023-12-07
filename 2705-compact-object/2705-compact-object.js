/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    return Array.isArray(obj) ? reduceArray(obj) : reduceObj(obj);
    
    function reduceObj(obj) {
        for (el in obj) {
            if (!obj[el]) {
                delete obj[el];
            } else if (Array.isArray(obj[el])) {
                obj[el] = reduceArray(obj[el]);
            } else if (typeof obj[el] == 'object') {
                obj[el] = reduceObj(obj[el]);
            }
        }
        return obj;
    }
    
    function reduceArray(obj) {
        const reducedArr = [];
        obj.forEach(curr => {
            if (!curr) return;
            else if (Array.isArray(curr)) {
                curr = reduceArray(curr);
            }
            else if (typeof curr == 'object') {
                curr = reduceObj(curr);
            }
            if (curr != null) {
                reducedArr.push(curr);
            }
        });
        return reducedArr;
    }
};