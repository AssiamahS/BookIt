import openai

# Replace with your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def summarize_book(book_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize this book: {book_text}",
        max_tokens=200
    )
    summary = response['choices'][0]['text']
    return summary.strip()

def answer_questions(book_text, question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Using the context from the book, answer this question: {book_text}\nQuestion: {question}",
        max_tokens=150
    )
    answer = response['choices'][0]['text']
    return answer.strip()

if __name__ == "__main__":
    book_text = "INSERT_BOOK_TEXT_HERE"  # Replace with the text of the book you want to summarize
    question = "INSERT_QUESTION_HERE"  # Replace with the question you want to ask

    summary = summarize_book(book_text)
    print("Summary of the book:")
    print(summary)

    answer = answer_questions(book_text, question)
    print("\nAnswer to the question:")
    print(answer)
