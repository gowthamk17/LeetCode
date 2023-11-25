/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    
	return async function(...args) {
        return new Promise(async (res, rej) => {
            setTimeout(() => rej("Time Limit Exceeded"), t);
            try {
                const result = await fn(...args);
                res(result)
            } catch(err) {
                rej(err)
            }
        });
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */