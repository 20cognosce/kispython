import re


def main(string):
    s = string.replace("\n", "")
    d = dict()
    li = []

    li_flag = ""
    while li_flag is not None:
        entry = re.search('<block>(.*?)</block>', s).group(1).replace(" ", "")
        li.append(entry)
        s = s.split('.', 1)[1]
        li_flag = re.search('<block>(.*?)</block>', s)

    for i in range(len(li)):
        current_entry = li[i]
        d_flag = ""
        while d_flag is not None:
            key = re.search('(.*?)<-', current_entry).group(1)
            value = re.search('q\\((.*?)\\)', current_entry).group(1)
            d.setdefault(key, []).append(value)
            current_entry = current_entry.replace(value, "")
            current_entry = current_entry.replace("q()", "")
            d_flag = re.search('q\\((.*?)\\)', current_entry)

    return d


if __name__ == "__main__":
    sentence = "[<block> onen_605 <- list(q(orus) ; q(rabiat)) </block>. <block>" \
               "\nerqu_524 <- list(q(rebe) ;q(bice);q(atte) ) </block>.<block> dire <-" \
               "\nlist( q(bisoa_705);q(matire_716) ;q(atge_85)) </block>. ]"
    print(main(sentence))
