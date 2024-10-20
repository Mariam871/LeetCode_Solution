class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Helper function to evaluate the expression recursively
        def evaluate(expr):
            if expr == 't':
                return True
            elif expr == 'f':
                return False
            elif expr[0] == '!':
                return not evaluate(expr[2:-1])  # Skip the outer parentheses
            elif expr[0] == '&':
                sub_exprs = split_expr(expr[2:-1])
                return all(evaluate(sub_expr) for sub_expr in sub_exprs)
            elif expr[0] == '|':
                sub_exprs = split_expr(expr[2:-1])
                return any(evaluate(sub_expr) for sub_expr in sub_exprs)

        # Helper function to split the sub-expressions correctly
        def split_expr(expr):
            sub_exprs = []
            balance = 0
            start = 0
            for i, char in enumerate(expr):
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                elif char == ',' and balance == 0:
                    sub_exprs.append(expr[start:i])
                    start = i + 1
            sub_exprs.append(expr[start:])  # Append the last part
            return sub_exprs

        # Call the helper function on the whole expression
        return evaluate(expression)
