def typing_speed_test():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(prompt_text)

    # Create a basic text-based UI
    print("Press 'Enter' to start the test.")
    input()

    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    total_time = end_time - start_time
    words_per_minute = len(user_input.split()) / (total_time / 60)

    correct_chars = sum(1 for a, b in zip(user_input, prompt_text) if a == b)
    accuracy = (correct_chars / len(prompt_text)) * 100

    print(f"\nTime taken: {total_time:.2f} seconds")
    print(f"Your typing speed: {words_per_minute:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
