def popular_words(text:str, words:list) -> dict:

    text = text.lower().split()
    words_lower = [word.lower() for word in words]
    result = {}

    for word in words_lower:
        result[word] = text.count(word)
    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
