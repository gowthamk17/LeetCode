/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
	return function(x) {
        for (let i = 0; i < functions.length; i++) {
            x = functions[functions.length - 1 - i](x)
        }
        // if (functions.length) {
        //     return functions.reverse().reduce((x, fn) => fn(x), x)
        // }
        return x
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */