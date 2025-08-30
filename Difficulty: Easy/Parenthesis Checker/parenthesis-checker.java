
class Solution {
    static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();
        
        int n = s.length();
        for (int i = 0; i < n; i++) {
            Character c = new Character(s.charAt(i));
            if (c.equals('(') || c.equals('{') || c.equals('[')) {
                stack.push(c);
                continue;
            }
            
            if (stack.size() == 0) {
                return false;
            }
            
            Character x = stack.pop();
            
            switch (c) {
                case ')':
                    if (!x.equals('(')) {
                        return false;
                    }
                    break;
                case '}':
                    if (!x.equals('{')) {
                        return false;
                    }
                    break;
                case ']':
                    if (!x.equals('[')) {
                        return false;
                    }
                    break;
            }
        }
        
        if (stack.size() > 0) {
            return false;
        }
        
        return true;
    }
}
