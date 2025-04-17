import random

fortunes = {
    "happy": [
        "Great things await you, Bhaskar! Keep smiling.",
        "Your joy will be contagious today, Bhaskar!"
    ],
    "sad": [
        "Tough times build strength. Stay determined, Bhaskar.",
        "Every cloud has a silver lining, Bhaskar."
    ],
    "neutral": [
        "Every day is a new chance to shine, Bhaskar!",
        "Take this day at your own pace, Bhaskar."
    ],
    "stressed": [
        "Even in stress, you can find moments of calm, Bhaskar.",
        "Your persistence through stress will lead to new breakthroughs, Bhaskar."
    ],
    "excited": [
        "Your excitement is a magnet for amazing opportunities, Bhaskar!",
        "Embrace the thrill of today, Bhaskar, and let your enthusiasm shine."
    ],
    "anxious": [
        "Every anxious moment is a chance to grow, Bhaskar. Stay strong.",
        "In moments of anxiety, remember you have the strength to overcome, Bhaskar."
    ]
}

def main():
    print("🔮 Welcome to Bhaskar's Fortune Teller (21je0236) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed/excited/anxious): ").strip().lower()
    
    if mood in fortunes:
        message = random.choice(fortunes[mood])
        print(f"✨ Your fortune: {message} ✨")
    else:
        print("✨ Your fortune: Sometimes the unexpected brings new opportunities. Embrace it, Bhaskar. ✨")

if __name__ == '__main__':
    main()
