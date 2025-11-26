def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def word_count(word_text):
    words = word_text.split()
    return len(words)

def count_characters(word_text):
    word_dict = {}
    for char in word_text:
        for i in char.lower():
            if i in word_dict:
                word_dict[i] += 1
            else:
                word_dict[i] = 1
    return word_dict

def sorted_dict(dic):
    def sort_on(item):
        return item['num']
    dic_list = []
    for i in dic:
        dic_list.append({"char" : i ,"num" :dic[i]})
    dic_list.sort(key=sort_on, reverse=True)
    return dic_list
