/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        if (functions.length == 0) {
            resolve([]);
        }
        const len = functions.length;
        const arr = new Array(len).fill(null);
        let resolved = 0;
        functions.forEach(async (fn, i) => {
            try {
                arr[i] = await fn();
                resolved++;
                if (resolved == len) {
                    resolve(arr);
                }
            } catch (e) {
                reject(e);
            }
        });
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */