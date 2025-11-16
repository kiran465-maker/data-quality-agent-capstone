from tools.autofix_helper import attempt_fixes
class AutoFixAgent:
    def run(self, df, issues):
        fixed = attempt_fixes(df, issues)
        fixes = {'auto_fixed': True, 'notes': 'Applied safe fixes (coercion, normalize, deduce, fill).'}
        return fixed, fixes
