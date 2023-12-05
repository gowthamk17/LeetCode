/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const uniqObj = {};
    for(let i = 0; i < arr1.length; i++) {
        const obj = arr1[i];
        uniqObj[obj['id']] = obj;
    }
    for(let i = 0; i < arr2.length; i++) {
        const obj = arr2[i];
        if(uniqObj[obj['id']]) {
            const value = uniqObj[obj['id']];
            for(const key in obj) {
                value[key] = obj[key];
            }
        } else {
            uniqObj[obj['id']] = obj;
        }
    }
    function compareFn(a, b) {
      if (a['id'] < b['id']) {
        return -1;
      } else if (a['id'] > b['id']) {
        return 1;
      }
      return 0;
    }
    const uniqArr = [];
    for(const key in uniqObj) {
        uniqArr.push(uniqObj[key]);
    }
    console.log(uniqArr);
    uniqArr.sort(compareFn)
    return uniqArr;
};