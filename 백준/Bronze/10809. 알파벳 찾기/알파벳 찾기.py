def main():
    alpabet = [-1 for _ in range(26)]
    S = input()

    for i in range(len(S)):
        if alpabet[ord(S[i])-97] == -1:
            alpabet[ord(S[i])-97] = i
        else:
            continue

    print(' '.join(map(str, alpabet)))

if __name__ == '__main__':
    main()