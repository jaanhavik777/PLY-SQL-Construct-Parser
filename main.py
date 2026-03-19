from lexer_parser import parse_query

def run_tests():
    queries = [
        "DELETE FROM employees WHERE id = 101",
        "SELECT dept FROM employees GROUP BY dept",
        "DELETE FROM employees WHERE",
        "DELETE FROM employees WHERE id == 101",
        "REMOVE FROM employees WHERE id = 101",
        "WHERE FROM employees DELETE id = 101",
        "DELETE FROM employees WHERE id = #101"
    ]

    for q in queries:
        print("=" * 50)
        print("Query:", q)
        try:
            result = parse_query(q)
            print("Parsed successfully:")
            print(result)
        except Exception as e:
            print("Error:", e)

def interactive_mode():
    print("\nEnter SQL queries (type 'exit' to quit):\n")
    while True:
        query = input("SQL > ")
        if query.lower() == "exit":
            break
        try:
            result = parse_query(query)
            print("Parsed:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run_tests()
    interactive_mode()
