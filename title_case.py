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
