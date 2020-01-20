one_to_nine = 3+3+5+4+4+3+5+5+4
print(one_to_nine)

teens = 3+6+6+8+8+7+7+9+8+8
print(teens)

twenty_to_ninety_prefixes = 6+6+5+5+5+7+6+6
one_to_ninety_nine = one_to_nine + teens + 10 * twenty_to_ninety_prefixes + 8 * one_to_nine

print(one_to_ninety_nine)

hundreds = one_to_nine + 9 * 7
one_thousand = 11

one_to_one_thousand = 10 * one_to_ninety_nine + 100 * hundreds + 99 * 9 * 3 + one_thousand

print(one_to_one_thousand)