# tsteele.py

def my_feature():
    print("Tom's feature")
    print("Numbers 1-10 as percentages")
    nums = [x / 100 for x in range(10)]
    print(list(nums))

def my_feature2():
    l = [
            {'name': 'Tom', 'shoe_size': 9.5} 
            , {'name': 'Taylor', 'shoe_size': 11.5} 
        ]
    print('Bigfoot people')
    print(
        list(
            filter(
                lambda x: x['shoe_size'] > 10
                , l
            )
        )
    )