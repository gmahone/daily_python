def title_case(title, minor_words=''):
    if len(title) == 0:
        return ""
    title_lower = title.lower().split()
    exception_lower = minor_words.lower().split()
    out = [title_lower[0].capitalize()]
    for i in range(1, len(title_lower)):
        if title_lower[i] in exception_lower:
            out.append(title_lower[i])
        else:
            out.append(title_lower[i].capitalize())
    return " ".join(out)


# other solutions

def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])


def title_case(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)

def title_case(title, minor_words=''):
    return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))
