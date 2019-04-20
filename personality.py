#personality.py
#Create an AI that changes emotion.

def main():
    currentemotion = 3
    action = 0
    emotionword = "happy"
    print("Hello")
    print("I am currently", emotionword)
    while action < 4:
        print("Which action will you do?")
        print("(reward, punish, threaten, joke, quit)")
        useraction = input()
        useraction = useraction.lower()
        if useraction == "reward":
            action = 0
        elif useraction == "punish":
            action = 1
        elif useraction == "threaten":
            action = 2
        elif useraction == "joke":
            action = 3
        elif useraction == "quit":
            action = 4
        emotionmatrix = [[5,1,2,5,3,3],
                         [0,0,4,4,4,0],
                         [0,0,2,0,2,2],
                         [1,5,1,4,4,4]]
        if action is 4:
            pass
        else:
            emotion = emotionmatrix[action][currentemotion]
            if emotion is 0:
                emotionword = "angry"
                currentemotion = 0
                print("I am", emotionword)
            elif emotion is 1:
                emotionword = "disgusted"
                currentemotion = 1
                print("I am", emotionword)
            elif emotion is 2:
                emotionword = "afraid"
                currentemotion = 2
                print("I am", emotionword)
            elif emotion is 3:
                emotionword = "happy"
                currentemotion = 3
                print("I am", emotionword)
            elif emotion is 4:
                emotionword = "sad"
                currentemotion = 4
                print("I am", emotionword)
            elif emotion is 5:
                emotionword = "suprised"
                currentemotion = 5
                print("I am", emotionword)
    print("I am still", emotionword)
    print("Goodbye")

main()
