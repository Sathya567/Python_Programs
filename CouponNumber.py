'''
@Author: Kodandi Sathya Sriman Narayana
@Date: 2021-11-11 12:36:00
@Title : To generate distinct coupons using random
'''

import random

class CouponNumber():

    def __init__(self, coupon_number):
        """
            constructor initialize using parameter
        """
        self.take_number = coupon_number

    def calculateDistinctNumber(self):

        distinct_number = []
        while len(distinct_number) < self.take_number:
            rand = random.randrange(1001, 9999)
            if rand not in distinct_number:
                distinct_number.append(rand)
            else:
                pass
        return distinct_number


while True:
    try:
        take_number = int(input("Enter the number of distinct coupon you want to generate : "))
        if take_number < 0:
            raise ValueError
            continue

        coupon_number_object = CouponNumber(take_number)
        total_random_number = coupon_number_object.calculateDistinctNumber()

        print("Total Distinct Coupon Number : ", total_random_number)
        break

    except ValueError:
        print("Invalid Input The number of coupon you want to generate should be in positive")

    except Exception as e:
        print(e)