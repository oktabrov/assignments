from abc import ABC, abstractmethod
class Criterion(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def judge(self, value):
        pass
    def evaluate(self, value):
        status = 'PASS' if self.judge(value) else 'FAIL'
        print(f"[{status}] {self.name}: {value}")
        return self.judge(value)
    
class MinWordsCriterion(Criterion):
    def __init__(self, min_words):
        super().__init__(f"MinWords({min_words})")
        self.min_words = min_words
    def judge(self, value):
        return len(value.split()) >= self.min_words
    
class MaxLengthCriterion(Criterion):
    def __init__(self, max_len):
        super().__init__(f"MaxLength({max_len})")
        self.max_len = max_len
    def judge(self, value):
        return len(value.split()) <= self.max_len
    
class NoBannedWordsCriterion(Criterion):
    def __init__(self, banned):
        super().__init__("NoBannedWords")
        self.banned = banned
    def judge(self, value):
        f = True
        for i in value.split():
            if i.lower() in self.banned:
                f = False
                break
        return f
    
class EndsWithPunctuationCriterion:
    def __init__(self):
        self.name = "EndsWithPunctuation"
    def judge(self, value):
        return value and value[-1] in '.!?'
    def evaluate(self, value):
        status = 'PASS' if self.judge(value) else 'FAIL'
        print(f"[{status}] {self.name}: {value}")
        return self.judge(value)
    
class ModerationReport:
    def __init__(self):
        self.entries = []
    def add(self, criterion_name, value, passed):
        self.entries.append((criterion_name, value, passed))
    def summary(self):
        total = len(self.entries)
        passed = sum(1 for i in self.entries if i[-1])
        failed = total-passed
        print(f"Total: {total}, Passed: {passed}, Failed: {failed}")

class ReviewField:
    def __init__(self, field_name):
        self.field_name = field_name
        self.criteria = []
        self.report = ModerationReport()
    def add_criterion(self, criterion):
        self.criteria.append(criterion)
    def moderate(self, value):
        print(f'Moderating {self.field_name}: "{value}"')
        f = True
        for i in self.criteria:
            passed = i.evaluate(value)
            self.report.add(i.name, value, passed)
            if not passed: f = False
        return f
    def show_report(self):
        print(f"--- Report for {self.field_name} ---")
        self.report.summary()



review = ReviewField('comment')
review.add_criterion(MinWordsCriterion(3))
review.add_criterion(MaxLengthCriterion(50))
review.add_criterion(NoBannedWordsCriterion(['spam', 'fake']))
review.add_criterion(EndsWithPunctuationCriterion())

valid1 = review.moderate('Great product overall!')
print(f'Valid: {valid1}')
print()

valid2 = review.moderate('ok')
print(f'Valid: {valid2}')
print()

valid3 = review.moderate('This is spam content')
print(f'Valid: {valid3}')
print()

review.show_report()

try:
    c = Criterion('test')
except TypeError:
    print('Cannot instantiate abstract class')