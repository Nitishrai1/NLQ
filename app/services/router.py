def decide_data_source(question: str) -> str:
    """
    Determines whether to use MySQL, MongoDB, or both based on keywords.
    """
    question_lower = question.lower()

    
    if any(keyword in question_lower for keyword in ["portfolio", "stock", "transaction", "transactions", "amount", "value", "manager", "invest", "user_id", "date"]):
        return "mysql"
    

    if any(keyword in question_lower for keyword in ["risk", "preference", "location", "address", "client profile"]):
        return "mongodb"

  
    if "client" in question_lower and "stock" in question_lower:
        return "both"

    return "unknown"
