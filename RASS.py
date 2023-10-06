import re

def read_and_sort_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Зчитуємо данні з файлу
            content = file.read()

            # Знаходимо перше речення. Припускаємо що речення закінчується на '.', '!' або '?'
            first_sentence_match = re.search(r'[^.!?]*[.!?]', content)
            if not first_sentence_match:
                return "Couldn't find a complete sentence in the file."

            first_sentence = first_sentence_match.group().strip()
            print(f"First sentence: {first_sentence}")

            # Отримуємо слова та видаляємо розділові знаки
            words = re.findall(r'\b\w+\b', first_sentence)

            # Відділяємо україньські слова від англійських
            english_alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            ukrainian_words = [word for word in words if not any(letter in english_alphabet for letter in word)]
            english_words = [word for word in words if any(letter in english_alphabet for letter in word)]

            # СОртуємо слова
            sorted_ukrainian_words = sorted(ukrainian_words, key=lambda word: word.lower())
            sorted_english_words = sorted(english_words, key=lambda word: word.lower())

            sorted_words = sorted_ukrainian_words + sorted_english_words
            return sorted_words, len(sorted_words)

    except Exception as e:
        return str(e)

sample_file_path = "testfile.txt"
print(read_and_sort_sentence(sample_file_path))
