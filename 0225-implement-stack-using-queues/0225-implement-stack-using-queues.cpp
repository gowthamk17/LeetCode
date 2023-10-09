class MyStack {
public:
    std::deque<int> stack;
    MyStack() {
        
    }
    
    void push(int x) {
        stack.push_back(x);
    }
    
    int pop() {
        int removedVal = stack.back();
        stack.pop_back();
        return removedVal;
    }
    
    int top() {
        return stack.back();
    }
    
    bool empty() {
        return stack.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */