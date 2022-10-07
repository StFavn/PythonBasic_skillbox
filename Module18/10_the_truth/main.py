def caesar_cipher(shift, user_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([
        alphabet[(alphabet.index(letter) + shift) % 26] if letter in alphabet
        else alphabet[(alphabet.index(letter.lower()) + shift) % 26].upper() if letter.isupper()
        else letter
        for letter in user_text
    ])


def text_shift(shift, user_text):
    len_text = len(user_text)
    return ''.join([user_text[(i + shift) % len_text] for i in range(len_text)])


def transformations(user_text):
    list_text = user_text.split()

    new_text, sentence, i = [], [], -3
    for word in list_text:
        sentence.append(word)
        if '/' in word:
            sentence = [text_shift(i, a_word) for a_word in sentence]
            new_text.append(' '.join(sentence))
            sentence = []
            i -= 1
    sentence = [text_shift(i, a_word) for a_word in sentence]
    new_text.append(' '.join(sentence))
    return '\n'.join(new_text)


text = (
    'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt '
    'cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf '
    'dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt '
    'foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip '
    'fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf '
    'sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf'
    ' tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ '
    'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
)

decoder_text = transformations(caesar_cipher(-1, text))
print('\n' + decoder_text)
