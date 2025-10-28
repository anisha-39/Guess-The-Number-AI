import time

def ai_guess_smart():
    print("🤖 Hi! I’m your Smart AI Guess Bot.")
    print("Think of a number between 1 and 100 — I’ll find it fast!")
    input("Press Enter when you're ready... ")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        time.sleep(1)
        guess = (low + high) // 2
        attempts += 1
        print(f"\nAI 🧠: Is your number {guess}?")
        feedback = input("Too High (H), Too Low (L), or Correct (C)? ").strip().lower()

        if feedback == 'h':
            high = guess - 1
            print("AI 🔍: Okay, reducing the range...")
        elif feedback == 'l':
            low = guess + 1
            print("AI 🔎: Hmm, maybe it’s higher...")
        elif feedback == 'c':
            print(f"\n✅ AI 🎉: Found it! Your number is {guess} — guessed in {attempts} tries!")
            break
        else:
            print("⚠️ Please enter only H, L, or C.")

    if low > high:
        print("❌ Seems like you changed your number midway 😅")

if __name__ == "__main__":
    ai_guess_smart()
