
class Solution {
    static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();
        
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
                continue;
            }
            
            if (stack.isEmpty()) {
                return false;
            }
            
            char top = stack.pop();
            if ((top == '(' && c != ')') ||
                (top == '{' && c != '}') ||
                (top == '[' && c != ']')) {
                return false;
            }
        }
        
        return stack.isEmpty();
    }
}
