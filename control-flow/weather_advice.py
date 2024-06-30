user_input = input("What's the weather like today? (sunny/rainy/cold").strip().lower()
sunny = 'Wear a t-shirt and sunglasses'
rainy = 'Don\'t forget your umbrella and a raincoat'
cold  = 'Make sure to wear a warm coat and a scarf'
#####################
if user_input == 'sunny':
    print(sunny)
elif user_input == 'rainy':
    print(rainy)
elif user_input == 'cold':
    print(cold)
else:
    print('Sorry, I don\'t have recommendations for this weather')
