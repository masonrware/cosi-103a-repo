Script started on Thu Mar 24 23:35:00 2022

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
[?1034hbash-3.2$ cd destkop/COSI_104[K4[K3A[1Pop/COSI_103Aktop/COSI_103A[C[C[C[C[C[C[C[C[C[C[C[C[C/PA@[K2
bash-3.2$ pytest
[1m=========================== test session starts ===========================[0m
platform darwin -- Python 3.9.5, pytest-7.1.1, pluggy-1.0.0
rootdir: /Users/masonware/Desktop/COSI_103A/PA2, configfile: pytest.ini
plugins: anyio-3.4.0
[1mcollecting ... [0m[1mcollected 12 items                                                        [0m

test_category.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                               [ 33%][0m
test_transactions.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                       [100%][0m

[32m=========================== [32m[1m12 passed[0m[32m in 0.37s[0m[32m ============================[0m
bash-3.2$ pylint transactions.py
************* Module transactions
transactions.py:124:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:19:0: C0115: Missing class docstring (missing-class-docstring)

-----------------------------------
Your code has been rated at 9.64/10

bash-3.2$ pylint tracker.py
************* Module tracker
tracker.py:64:0: R0914: Too many local variables (20/15) (too-many-locals)
tracker.py:64:0: R0915: Too many statements (51/50) (too-many-statements)
tracker.py:163:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:168:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:173:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:178:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

------------------------------------------------------------------
Your code has been rated at 9.29/10 (previous run: 9.29/10, +0.00)

bash-3.2$ python4[K3 tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 4


item       amount     category   date       description                   
----------------------------------------
1          300        boats      03-22-23   i bought this big ass mf yacht
> 5
transaction amount: 500
transaction category: test
transaction date (MM-DD-YY): 00-00-00
transaction description: test desc
> 4


item       amount     category   date       description                   
----------------------------------------
1          300        boats      03-22-23   i bought this big ass mf yacht
1          500        test       00-00-00   test desc                     
> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 7
Filter Date > 22


item       amount     category   date       description                   
----------------------------------------
1          300        boats      03-22-23   i bought this big ass mf yacht
> 7
Filter Date > 00


item       amount     category   date       description                   
----------------------------------------
1          500        test       00-00-00   test desc                     
> 