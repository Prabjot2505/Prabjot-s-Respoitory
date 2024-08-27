def is_palindrome(text):
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]

while True:
    user_input = input("Enter a word or phrase to check if it's a palindrome: ").strip()

    if not user_input:
        print("You didn't enter anything. Please try again.")
        continue

    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")

    check_again = input("Do you want to check another word or phrase? (yes/no): ").lower()
    if check_again != "yes":
        break

print("Thanks for using the palindrome checker! Goodbye!")
