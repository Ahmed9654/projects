import random
import higher_lower_data as dt
first = random.choice(dt.data)
score = 0
while True:
    print(dt.logo)
    second = random.choice(dt.data)

    # compare text
    print(f"current score = {score}")
    print(f"Compare A: {first['name']}, {first['description']}, {first['country']}")
    print(dt.vs)
    print(f"Against B: {second['name']}, {second['description']}, {second['country']}")
    # the real compare
    choice = input('who has more followers,type "B" or "A": ').lower()
    if choice == 'a':
# compare the followers of first and second
        if first['follower_count'] > second['follower_count']:
            score+=1
            first = second
        else:
            print(f'wrong answer; your score is {score}')
            break
    else:
# compare the followers of first and second
        if first['follower_count'] < second['follower_count']:
            score+=1
            first = second
        else:
            print(f'wrong answer; your score is {score}')
            break
    print('\n'*20)