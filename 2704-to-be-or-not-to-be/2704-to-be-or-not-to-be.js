/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return{ 
      toBe:function(val2){
          if(val!==val2){throw new Error("Not Equal") }
          return val===val2;
      },
      notToBe:function(val2){
          if(val===val2){throw new Error("Equal") }
          return val!==val2;
      }}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */