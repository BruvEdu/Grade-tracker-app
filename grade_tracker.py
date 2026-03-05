def analyze_grades(grade_list):
    """
    Filters for passing grades and calculates their average.
    """
    # 1. Define the passing threshold
    passing_score = 60
    
    # 2. Filter the list for scores 60 and above
    passing_grades = [score for score in grade_list if score >= passing_score]
    
    # 3. Calculate the average of passing grades
    # We check 'if passing_grades' to ensure the list isn't empty
    if passing_grades:
        average = sum(passing_grades) / len(passing_grades)
    else:
        average = 0  # Default to zero if no one passed
        
    return passing_grades, average

# --- Testing the logic ---
student_scores = [95, 42, 78, 55, 88, 60, 30, 100]

# Unpack the two results from our function
passing_list, passing_avg = analyze_grades(student_scores)

print(f"Passing Grades: {passing_list}")
print(f"Average of Passing Grades: {passing_avg}")
