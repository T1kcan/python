secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
    if guess_count == 1:
        print('nihaanaa! bilemedin!')
    else:    
        print('nihaanaa! gene bilemedin!')
else:
    print('Sorry, You Failed!')