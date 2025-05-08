#Implement any one of the following Expert System Employee performance evaluation


class PerformanceEvaluator:
    def __init__(self):
        self.knowledge_base = {
            'productivity': {
                'low': (0, 60),
                'medium': (61, 80),
                'high': (81, 100)
            },
            'quality': {
                'poor': (0, 70),
                'good': (71, 85),
                'excellent': (86, 100)
            },
            'attendance': {
                'poor': (0, 80),
                'good': (81, 95),
                'excellent': (96, 100)
            }
        }
        
        self.rules = {
            ('high', 'excellent', 'excellent'): 'Outstanding',
            ('high', 'excellent', 'good'): 'Excellent',
            ('medium', 'good', 'good'): 'Good',
            ('medium', 'poor', 'good'): 'Average',
            ('low', 'poor', 'poor'): 'Needs Improvement'
        }
    
    def evaluate_performance(self, productivity, quality, attendance):
        # Categorize inputs
        prod_cat = self._categorize('productivity', productivity)
        qual_cat = self._categorize('quality', quality)
        att_cat = self._categorize('attendance', attendance)
        
        # Evaluate performance based on rules
        for (p, q, a), rating in self.rules.items():
            if prod_cat == p and qual_cat == q and att_cat == a:
                return rating
        
        return 'Average'  # default rating
    
    def _categorize(self, metric, value):
        for category, (min_val, max_val) in self.knowledge_base[metric].items():
            if min_val <= value <= max_val:
                return category
        return 'poor'  # default category

# Example usage
evaluator = PerformanceEvaluator()
rating = evaluator.evaluate_performance(85, 90, 98)  # productivity=85, quality=90, attendance=98
print(f"Performance Rating: {rating}")  # Output: Performance Rating: Outstanding
