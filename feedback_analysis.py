def feedback(ratings):
    if not ratings: 
        return "No ratings available."
    
    positive = [rating for rating in ratings if rating >= 4]  
    positive_percentage = (len(positive) / len(ratings)) * 100  
    
    return f"Positive Feedback: {positive_percentage:.1f}%"  

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(feedback(ratings))
