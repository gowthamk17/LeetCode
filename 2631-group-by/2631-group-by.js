/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const group = {};
    const arr = this;
    for (let i = 0; i < this.length; i++) {
        const key = fn(arr[i]);
        if (group[key]) {
            group[key].push(arr[i]);
            // console.log(group[key]);
        } else {
            group[key] = [arr[i]];
        }
    }
    return group;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */